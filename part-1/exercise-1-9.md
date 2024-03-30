```console
[akseli@aybabtu part-1]$ touch text.log
[akseli@aybabtu part-1]$ docker run -v "$(pwd)/text.log:/usr/src/app/text.log" devopsdockeruh/simple-web-service
Starting log output
Wrote text to /usr/src/app/text.log
Wrote text to /usr/src/app/text.log
Wrote text to /usr/src/app/text.log
^C[akseli@aybabtu part-1]$ cat text.log
2024-03-30 21:00:24 +0000 UTC
2024-03-30 21:00:26 +0000 UTC
2024-03-30 21:00:28 +0000 UTC
```
