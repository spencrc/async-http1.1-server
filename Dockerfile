FROM alpine:3.24.1

RUN apk add --no-cache \
    clang \
    g++ \
    make \
    liburing-dev \
    linux-headers

WORKDIR /app
COPY . .

RUN make all -j
ENTRYPOINT ["./bin/release/server"]