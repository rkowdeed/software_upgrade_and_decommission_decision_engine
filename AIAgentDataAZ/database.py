import os
import sqlite3
from datetime import datetime

class SemiconductorDatabase:
    def __init__(self, db_path: str):
        self.db_path = os.path.abspath(db_path)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.create_tables()

    def create_tables(self) -> None:
        create_sql = """
        CREATE TABLE IF NOT EXISTS file_ingest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            s3_key TEXT NOT NULL,
            processed_at TEXT NOT NULL,
            file_hash TEXT NOT NULL,
            record_count INTEGER NOT NULL,
            status TEXT NOT NULL,
            error_message TEXT
        );

        CREATE TABLE IF NOT EXISTS semiconductor_operation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_ingest_id INTEGER NOT NULL,
            lot_id TEXT NOT NULL,
            operation_step TEXT NOT NULL,
            equipment_id TEXT NOT NULL,
            process_date TEXT NOT NULL,
            status TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            yield_pct REAL NOT NULL,
            metadata TEXT NOT NULL,
            FOREIGN KEY(file_ingest_id) REFERENCES file_ingest(id)
        );
        """
        cursor = self.connection.cursor()
        cursor.executescript(create_sql)
        # If the table already exists, ensure the metadata column is present.
        cursor.execute("PRAGMA table_info(semiconductor_operation)")
        columns = [row[1] for row in cursor.fetchall()]
        if "metadata" not in columns:
            cursor.execute(
                "ALTER TABLE semiconductor_operation ADD COLUMN metadata TEXT NOT NULL DEFAULT '{}'"
            )
        self.connection.commit()

    def insert_ingest_summary(
        self,
        file_name: str,
        s3_key: str,
        file_hash: str,
        record_count: int,
        status: str,
        error_message: str | None = None,
    ) -> int:
        processed_at = datetime.utcnow().isoformat() + "Z"
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO file_ingest (file_name, s3_key, processed_at, file_hash, record_count, status, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (file_name, s3_key, processed_at, file_hash, record_count, status, error_message),
        )
        self.connection.commit()
        return cursor.lastrowid

    def insert_operation_rows(self, ingest_id: int, rows: list[tuple]) -> None:
        cursor = self.connection.cursor()
        cursor.executemany(
            """
            INSERT INTO semiconductor_operation (
                file_ingest_id,
                lot_id,
                operation_step,
                equipment_id,
                process_date,
                status,
                quantity,
                yield_pct,
                metadata
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
