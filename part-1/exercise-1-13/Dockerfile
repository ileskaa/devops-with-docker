FROM ubuntu

EXPOSE 8080

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y install curl

RUN curl -sLO https://go.dev/dl/go1.16.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf ./go1.16.linux-amd64.tar.gz

# ENV is used to set an environment variable to a specific value
ENV PATH="$PATH:/usr/local/go/bin"

COPY example-backend .

RUN go build

CMD ["./server"]
