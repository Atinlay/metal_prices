FROM python:3.7-alpine

RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
#RUN apk add --update --no-cache cron

RUN pip install --upgrade pip

#COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install pandas requests sqlalchemy bs4 mysqlclient
COPY . /opt/app

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
# RUN crontab /etc/cron.d/cronjob

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
