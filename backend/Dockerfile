FROM revolutionsystems/python:3.6.6-wee-optimized-lto


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
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ENV LC_ALL="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

COPY ./backend/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /backend
WORKDIR /backend
COPY ./backend /backend

