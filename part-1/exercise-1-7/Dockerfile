FROM ubuntu:22.04

# Set /usr/src/app as workdir. Coming instructions will be executed in this location
WORKDIR /usr/src/app

# We use apt-get since with apt we get warned about an unstable CLI interface
RUN apt-get update && apt-get -y install curl

# Copy the script file into the image
COPY script.sh .

# If we skipped chmod earlier, we can add execution permissions during the build.
RUN chmod +x script.sh

# This command is called upon executing docker run
CMD ./script.sh