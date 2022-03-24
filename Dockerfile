FROM python:3.9 as builder

ENV WORKDIR=/usr/src/app
ENV APP_HOME=/app/src

ENV UNAME=testuser
ENV PATH="/home/$UNAME/.local/bin:${PATH}"
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

RUN apt-get update
RUN apt-get -yqq install gunicorn3

USER $UNAME
CMD /bin/bash

WORKDIR $WORKDIR

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

COPY src/requirements.txt .

RUN pip install -r requirements.txt

WORKDIR $APP_HOME

FROM builder as app
