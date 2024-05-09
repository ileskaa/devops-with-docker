FROM ubuntu

EXPOSE 8080

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y install curl

RUN curl -sLO https://go.dev/dl/go1.16.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf ./go1.16.linux-amd64.tar.gz

ENV PATH="$PATH:/usr/local/go/bin"
ENV REQUEST_ORIGIN="http://localhost:5000"

COPY exercise-1-13/example-backend .

RUN go build

CMD ["./server"]
