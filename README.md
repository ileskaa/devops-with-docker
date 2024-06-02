# Part 1

Exercises 1 through 14, as well as exercise 16 are provided in the [part-1](https://github.com/ileskaa/devops-with-docker/tree/master/part-1) directory. For exercises that only asked to run commands, the answers are written to a simple markdown file. For exercises that asked for a Dockerfile, with possibly some other elements, a directory named after that exercise has been created.  
My answer to exercise 15 is given in the present Readme.

## Exercise 15

[Docker Hub project link](https://hub.docker.com/repository/docker/ileska/hello-hy/general)

To run this application, use `docker run --rm ileska/hello-hy`

The `--rm` option will automatically remove the container once it has finished running.

You know this app works, if it outputs a sentence starting with "Hello" to your command prompt.

Since this image is quite large, I recommend you remove it once you've tested it by running  
`docker rmi ileska/hello-hy`
