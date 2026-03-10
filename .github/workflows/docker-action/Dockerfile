FROM alpine:3.20

RUN apk add --no-cache bash coreutils

COPY entrypoint.sh /entrypoint.sh
COPY post.sh /post.sh

RUN chmod +x /entrypoint.sh /post.sh
