FROM debian:stretch-slim

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install python3.5 python3-dev python3-pip cython3
RUN apt-get -y install python3-numpy
RUN apt-get -y install python3-pandas cron

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
