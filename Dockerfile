FROM ubuntu:14.04

RUN apt-get install software-properties-common

RUN add-apt-repository ppa:jonathonf/python-3.6

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python3.6 -y

RUN pip install --upgrade pip

# RUN sudo apt install default-libmysqlclient-dev

#COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install --upgrade cython pandas requests sqlalchemy bs4 mysqlclient
COPY . /opt/app

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
# RUN crontab /etc/cron.d/cronjob

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
# CMD cron && tail -f /var/log/cron.log
