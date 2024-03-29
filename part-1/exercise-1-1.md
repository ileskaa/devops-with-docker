```sh
[akseli@aybabtu part-1]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
da3b83985f1d   nginx     "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    80/tcp    tender_neumann
4077397cb3b2   nginx     "/docker-entrypoint.…"   8 seconds ago    Up 7 seconds    80/tcp    pedantic_gauss
e2060fcac20e   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   80/tcp    flamboyant_lamarr
[akseli@aybabtu part-1]$ docker container stop da 40
da
40
[akseli@aybabtu part-1]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
da3b83985f1d   nginx     "/docker-entrypoint.…"   2 minutes ago    Exited (0) 4 seconds ago             tender_neumann
4077397cb3b2   nginx     "/docker-entrypoint.…"   2 minutes ago    Exited (0) 4 seconds ago             pedantic_gauss
e2060fcac20e   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes              80/tcp    flamboyant_lamarr
```
