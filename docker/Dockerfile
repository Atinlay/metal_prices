FROM balenalib/amd64-alpine-python:latest

RUN apt-get update -y
RUN apt-get install -y cron

RUN pip install --upgrade pip

RUN pip install pandas=0.24.2 requests sqlalchemy bs4 mysqlclient

# ADD *.py /host/codebase/

COPY cronjob /etc/cron.d/cronjob

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
# RUN crontab /etc/cron.d/cronjob

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
