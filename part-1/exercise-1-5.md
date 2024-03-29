Comparing image sizes:
```console
[akseli@aybabtu part-1]$ docker pull devopsdockeruh/simple-web-service:alpine
alpine: Pulling from devopsdockeruh/simple-web-service
ba3557a56b15: Pull complete 
1dace236434b: Pull complete 
4f4fb700ef54: Pull complete 
Digest: sha256:dd4d367476f86b7d7579d3379fe446ae5dfce25480903fb0966fc2e5257e0543
Status: Downloaded newer image for devopsdockeruh/simple-web-service:alpine
docker.io/devopsdockeruh/simple-web-service:alpine
[akseli@aybabtu part-1]$ docker image ls
REPOSITORY                          TAG       IMAGE ID       CREATED       SIZE
ubuntu                              latest    ca2b0f26964c   4 weeks ago   77.9MB
devopsdockeruh/simple-web-service   ubuntu    4e3362e907d5   3 years ago   83MB
devopsdockeruh/simple-web-service   alpine    fd312adc88e0   3 years ago   15.7MB
```
We can see that the Alpine image is much smaller in size.

Making sure the secret image functionality is the same:
```console
[akseli@aybabtu part-1]$ docker run -d --name alp devopsdockeruh/simple-web-service:alpine
c58f88f3792a4b1d6684c1146572a9e699af32d3556f2f09fd1f223d1bd26847
[akseli@aybabtu part-1]$ docker exec -it alp sh
/usr/src/app # tail -f ./text.log
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
2024-03-29 20:00:37 +0000 UTC
2024-03-29 20:00:39 +0000 UTC
2024-03-29 20:00:41 +0000 UTC
2024-03-29 20:00:43 +0000 UTC
2024-03-29 20:00:45 +0000 UTC
Secret message is: 'You can find the source code here: https://github.com/docker-hy'
```
