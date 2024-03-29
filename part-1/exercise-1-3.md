```bash session
[akseli@aybabtu part-1]$ docker run -d --name ubu devopsdockeruh/simple-web-service:ubuntu
f3f05eba0b0ec375198a365c792de855b7836b50cd05cf34e0a83df8d9544adf
[akseli@aybabtu part-1]$ docker exec -it ubu bash
root@f3f05eba0b0e:/usr/src/app# tail -f ./text.log
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
2024-03-29 16:35:28 +0000 UTC
2024-03-29 16:35:30 +0000 UTC
2024-03-29 16:35:32 +0000 UTC
2024-03-29 16:35:34 +0000 UTC
2024-03-29 16:35:36 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
```
