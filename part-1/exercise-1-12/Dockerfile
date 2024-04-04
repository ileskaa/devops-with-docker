FROM ubuntu

EXPOSE 5000

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y install curl

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash
RUN apt-get install -y nodejs

COPY example-frontend .

RUN npm i
RUN npm run build
RUN npm install -g serve

CMD ["serve", "-s", "-l", "5000", "build"]
