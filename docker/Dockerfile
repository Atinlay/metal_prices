FROM python:3.6.4-alpine3.7

RUN apt-get update
RUN apt-get install -y cron

RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

RUN apk update

RUN apk add --update --no-cache \
    libgfortran

RUN apk add --update --no-cache \
    linux-headers \
    python \
    py2-numpy@community py2-scipy@community

RUN pip install --upgrade pip

RUN pip install requests sqlalchemy bs4 mysqlclient

ADD ../*.py /host/codebase/

COPY ../cronjob /etc/cron.d/cronjob

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
# RUN crontab /etc/cron.d/cronjob

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
