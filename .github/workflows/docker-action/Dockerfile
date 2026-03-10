FROM mcr.microsoft.com/devcontainers/python:3.12

RUN pip install --upgrade pip && pip install -r requirements.txt

# RUN apk add --no-cache bash coreutils

COPY entrypoint.py /entrypoint.py
COPY post.py /post.py

RUN chmod +x /entrypoint.py /post.py
