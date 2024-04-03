FROM amazoncorretto:8

# describe which port your app is listening on
EXPOSE 8080

# Set working dit for any RUN, CMD, ENTRYPOINT, COPy and ADD
# instructions that follow.
WORKDIR /usr/src/app

# copy the content of spring-example-project into the container working dir
COPY spring-example-project .

# build the project
RUN ./mvnw package

# command to run the application
CMD ["java", "-jar", "./target/docker-example-1.1.3.jar"]
