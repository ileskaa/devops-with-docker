# Slim Buster is a popular Python docker image
FROM python:3.10.0-slim-buster

# Set the working dir inside the container.
# If the dir does not yet exist, it is created
WORKDIR /flask-simple-app

COPY . .

RUN pip3 install -r requirements.txt

# Tell fly.io which port to use for services. 5000 is the default Flask port
EXPOSE 5000

# Run Flask development server
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
