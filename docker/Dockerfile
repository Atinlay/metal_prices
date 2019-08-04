FROM python:3.6.9-buster

RUN apt-get update && apt-get -y install cron

RUN pip install pandas numpy requests sqlalchemy bs4 mysqlclient

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
