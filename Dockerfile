FROM ubuntu:22.04
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends gcc libffi-dev musl-dev ffmpeg aria2 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

    #Don't change anything otherwise Code not working properly

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement Installer
CMD python3 modules/main.py