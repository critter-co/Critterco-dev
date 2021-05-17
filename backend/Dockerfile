FROM python:3.6.13-slim-buster


ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
# ENV GDAL_SKIP=DODS

# Install GDAL dependencies
RUN echo deb http://deb.debian.org/debian testing main contrib non-free >> /etc/apt/sources.list && \
        apt-get update && \
        apt-get install -y libgdal-dev tk g++ --no-install-recommends && \
        apt-get install -y postgresql-client && \
        pip install gunicorn && \
        apt-get clean -y

# Update C env vars so compiler can find gdal
#ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
#ENV C_INCLUDE_PATH=/usr/include/gdal

#RUN apk update
#RUN apk update && \
#    apk add --no-cache --virtual build-deps python3-dev musl-dev postgresql-dev && \
#    apk add --no-cache postgresql-dev tzdata && \
#    apk del --no-cache build-deps

ENV LC_ALL="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"
ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

COPY ./backend/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./backend /backend

RUN echo "Asia/Tehran" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata