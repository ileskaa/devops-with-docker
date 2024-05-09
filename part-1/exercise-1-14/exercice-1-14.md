## Commands used in this exercise

Run from the `part-1` directory (that is, the parent directory of this exercise's directory):
```console
docker build -t frontend -f exercise-1-14/frontend/Dockerfile . &&
    docker build -t backend -f exercise-1-14/backend/Dockerfile . &&
    (docker run -p 8080:8080 backend &) &&
    docker run -p 5000:5000 frontend
```
