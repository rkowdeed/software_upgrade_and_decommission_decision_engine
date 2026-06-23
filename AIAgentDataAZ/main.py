import json
import os
import time
from pathlib import Path

from agents import CleanserAgent, ExplorerAgent, LoaderAgent
from database import SemiconductorDatabase
from mock_s3 import MockS3Bucket

BASE_DIR = Path(__file__).resolve().parent
MOCK_S3_DIR = BASE_DIR / "mock_s3_bucket"
DB_PATH = BASE_DIR / "data" / "semiconductor.db"
STATE_FILE = BASE_DIR / "processed_state.json"
POLL_INTERVAL_SECONDS = 5


def load_state() -> dict[str, dict[str, str]]:
    if not STATE_FILE.exists():
        return {}
    with open(STATE_FILE, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_state(state: dict[str, dict[str, str]]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)


def seed_synthetic_data(bucket: MockS3Bucket) -> None:
    valid_data = """lot_id,operation_step,equipment_id,process_date,status,quantity,yield_pct,metadata
LOT123,etch,EQ-1,2026-06-23,completed,120,98.6,"{""execution_time_ms"":120,""process_specification"":{""name"":""etch-A"",""version"":""1.0""},""equipment_conditions"":{""temperature"":{""setpoint"":20,""unit"":""C""},""pressure"":""1atm"",""active"":true}}"
LOT124,implant,EQ-2,2026-06-23,completed,95,97.1,"{""execution_time_ms"":95,""process_specification"":{""name"":""implant-B"",""version"":""2.1""},""equipment_conditions"":{""temperature"":{""setpoint"":25,""unit"":""C""},""pressure"":""0.95atm"",""active"":false}}"
LOT125,deposit,EQ-3,2026-06-23,failed,78,87.3,"{""execution_time_ms"":110,""process_specification"":{""name"":""deposit-C"",""version"":""1.5""},""equipment_conditions"":{""temperature"":{""setpoint"":18,""unit"":""C""},""pressure"":""1.05atm"",""active"":true}}"
LOT126,inspection,EQ-4,2026-06-23,completed,145,99.2,"{""execution_time_ms"":60,""process_specification"":{""name"":""inspection-D"",""version"":""3.0""},""equipment_conditions"":{""temperature"":{""setpoint"":22,""unit"":""C""},""pressure"":""1atm"",""active"":false}}"
"""
    bucket.write_text("semiconductor_operations_20260623.csv", valid_data)

    invalid_data = """lot_id,operation_step,equipment_id,process_date,status,quantity,yield_pct,metadata
LOT200,implant,EQ-5,2026-06-24,completed,not_a_number,95.4,"{""execution_time_ms"":105,""process_specification"":{""name"":""implant-B"",""version"":""2.1""},""equipment_conditions"":{""temperature"":{""setpoint"":25,""unit"":""C""},""pressure"":""0.95atm"",""active"":false}}"
LOT201,etch,EQ-6,2026-06-24,completed,100,,"{""execution_time_ms"":75,""process_specification"":{""name"":""etch-A"",""version"":""1.2""},""equipment_conditions"":{""temperature"":{""setpoint"":20,""unit"":""C""},""pressure"":""1atm"",""active"":"not_boolean"}}"
"""
    bucket.write_text("semiconductor_operations_20260624_invalid.csv", invalid_data)


def process_bucket(bucket: MockS3Bucket, db: SemiconductorDatabase, state: dict[str, dict[str, str]]) -> None:
    explorer = ExplorerAgent()
    cleanser = CleanserAgent()
    loader = LoaderAgent()

    objects = explorer.discover(bucket)
    if not objects:
        print("No files found in the mock S3 bucket.")
        return

    print(f"Discovered {len(objects)} file(s) in mock S3 bucket.")
    for obj in objects:
        current_hash = bucket.compute_hash(obj.key)
        previous = state.get(obj.key)
        if previous and previous.get("file_hash") == current_hash:
            print(f"Skipping unchanged object: {obj.key}")
            continue

        print(f"Processing new or updated object: {obj.key}")
        validation = cleanser.validate(bucket, obj)
        if validation["ok"]:
            load_result = loader.load(db, bucket, obj, validation["rows"])
            state[obj.key] = {
                "file_hash": current_hash,
                "status": "loaded",
                "row_count": str(load_result["row_count"]),
            }
            print(f"Loaded {load_result['row_count']} row(s) from {obj.key} into the database.")
        else:
            print(f"Validation failed for {obj.key}:")
            for issue in validation["issues"]:
                print(f"  - {issue}")
            state[obj.key] = {
                "file_hash": current_hash,
                "status": "validation_failed",
                "issues": "; ".join(validation["issues"]),
            }

    save_state(state)


def main() -> None:
    bucket = MockS3Bucket(str(MOCK_S3_DIR))
    db = SemiconductorDatabase(str(DB_PATH))
    state = load_state()
    seed_synthetic_data(bucket)
    print("Mock S3 bucket directory:", bucket.bucket_dir)
    print("SQLite database path:", db.db_path)
    print("Starting pipeline. Add or update files in the mock S3 bucket to trigger processing.")

    try:
        while True:
            process_bucket(bucket, db, state)
            print("Waiting for new or updated files...\n")
            time.sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("Stopping pipeline.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
