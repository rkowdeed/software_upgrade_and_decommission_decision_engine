## GitHub Copilot Chat

- Extension: 0.44.0 (prod)
- VS Code: 1.116.0 (560a9dba96f961efea7b1612916f89e5d5d4d679)
- OS: win32 10.0.26200 x64
- GitHub Account: rkowdeed

## Network

User Settings:
```json
  "http.systemCertificatesNode": true,
  "github.copilot.advanced.debug.useElectronFetcher": true,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": true
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: Error (6519 ms): getaddrinfo ENOTFOUND api.github.com
- DNS ipv6 Lookup: timed out after 10 seconds
- Proxy URL: None (3 ms)
- Electron fetch (configured): timed out after 10 seconds
- Node.js https: Error (31 ms): Error: getaddrinfo ENOTFOUND api.github.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (48 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14902:13
	at process.processTicksAndRejections (node:internal/process/task_queues:103:5)
	at async t._fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:5229)
	at async t.fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:4541)
	at async u (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5330:186)
	at async xg._executeContributedCommand (file:///c:/Users/ravik/AppData/Local/Programs/Microsoft%20VS%20Code/560a9dba96/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:501:48675)
  Error: getaddrinfo ENOTFOUND api.github.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://api.githubcopilot.com/_ping:
- DNS ipv4 Lookup: Error (1 ms): getaddrinfo ENOTFOUND api.githubcopilot.com
- DNS ipv6 Lookup: timed out after 10 seconds
- Proxy URL: None (6 ms)
- Electron fetch (configured): timed out after 10 seconds
- Node.js https: Error (3966 ms): Error: getaddrinfo ENOTFOUND api.githubcopilot.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (52 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14902:13
	at process.processTicksAndRejections (node:internal/process/task_queues:103:5)
	at async t._fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:5229)
	at async t.fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:4541)
	at async u (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5330:186)
	at async xg._executeContributedCommand (file:///c:/Users/ravik/AppData/Local/Programs/Microsoft%20VS%20Code/560a9dba96/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:501:48675)
  Error: getaddrinfo ENOTFOUND api.githubcopilot.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://copilot-proxy.githubusercontent.com/_ping:
- DNS ipv4 Lookup: Error (1 ms): getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
- DNS ipv6 Lookup: timed out after 10 seconds
- Proxy URL: None (6 ms)
- Electron fetch (configured): Error (6882 ms): Error: net::ERR_NETWORK_CHANGED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  {"is_request_error":true,"network_process_crashed":false}
- Node.js https: Error (35 ms): Error: getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
- Node.js fetch: Error (61 ms): TypeError: fetch failed
	at node:internal/deps/undici/undici:14902:13
	at process.processTicksAndRejections (node:internal/process/task_queues:103:5)
	at async t._fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:5229)
	at async t.fetch (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5298:4541)
	at async u (c:\Users\ravik\AppData\Local\Programs\Microsoft VS Code\560a9dba96\resources\app\extensions\copilot\dist\extension.js:5330:186)
	at async xg._executeContributedCommand (file:///c:/Users/ravik/AppData/Local/Programs/Microsoft%20VS%20Code/560a9dba96/resources/app/out/vs/workbench/api/node/extensionHostProcess.js:501:48675)
  Error: getaddrinfo ENOTFOUND copilot-proxy.githubusercontent.com
  	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Connecting to https://mobile.events.data.microsoft.com: Error (4320 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  {"is_request_error":true,"network_process_crashed":false}
Connecting to https://dc.services.visualstudio.com: Error (4 ms): Error: net::ERR_NAME_NOT_RESOLVED
	at SimpleURLLoaderWrapper.<anonymous> (node:electron/js2c/utility_init:2:10684)
	at SimpleURLLoaderWrapper.emit (node:events:519:28)
  {"is_request_error":true,"network_process_crashed":false}
Connecting to https://copilot-telemetry.githubusercontent.com/_ping: Error (35 ms): Error: getaddrinfo ENOTFOUND copilot-telemetry.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
Connecting to https://copilot-telemetry.githubusercontent.com/_ping: Error (30 ms): Error: getaddrinfo ENOTFOUND copilot-telemetry.githubusercontent.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)
Connecting to https://default.exp-tas.com: Error (35 ms): Error: getaddrinfo ENOTFOUND default.exp-tas.com
	at GetAddrInfoReqWrap.onlookupall [as oncomplete] (node:dns:122:26)

Number of system certificates: 101

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).
