```console
docker build . -t spring-project && docker run -p 8080:8080 spring-project
```

If you just want to inspect what's inside the container:
```console
docker build . -t spring-project && docker run -it spring-project
```