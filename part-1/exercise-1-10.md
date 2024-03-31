```console
[akseli@aybabtu part-1]$ docker run -p 8000:8080 devopsdockeruh/simple-web-service server
[GIN-debug] [WARNING] Creating an Engine instance with the Logger and Recovery middleware already attached.

[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:	export GIN_MODE=release
 - using code:	gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /*path                    --> server.Start.func1 (3 handlers)
[GIN-debug] Listening and serving HTTP on :8080
[GIN] 2024/03/31 - 11:52:52 | 200 |      59.942µs |      172.17.0.1 | GET      "/"
[GIN] 2024/03/31 - 11:52:52 | 200 |      39.985µs |      172.17.0.1 | GET      "/favicon.ico"
```
