# We're using Alpine stable
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/v3.9/community;http\1/v3.9/community;g' -i /etc/apk/repositories

# Installing Python
RUN apk add --no-cache --update \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    git \
    sudo \
    util-linux \
    chromium \
    chromium-chromedriver \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    py-lxml \
    py-pillow \
    py-pip \
    py-requests \
    py-sqlalchemy \
    py-tz \
    py3-aiohttp \
    python-dev \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    sqlite-dev \
    sudo \
    zlib-dev \
    curl-dev \
    libressl-dev \



RUN pip3 install --upgrade pip setuptools

# Copy Python Requirements to /root/nana

RUN git clone https://github.com/legenhand/covid-bot.git /root/covidinfobot
WORKDIR /root/covidinfobot

#Copy config file to /root/nana/nana
COPY ./covidinfo/config.example.py ./covidinfo/config.py* /root/covidinfobot/covidinfo/


RUN sudo pip3 install -r requirements.txt
CMD ["python3","-m","covidinfo"]
