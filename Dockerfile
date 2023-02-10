FROM python:3
EXPOSE 5000
WORKDIR /src
RUN apt-get update && apt-get -y install cron joe
RUN pip install --no-cache-dir requests pytz
COPY crontab /etc/cron.d/crontab
COPY maxmeter-test.py /src
RUN chmod 0600 /etc/cron.d/crontab
RUN chmod a+s /usr/sbin/cron
RUN /usr/bin/crontab /etc/cron.d/crontab
CMD ["cron", "-f"]
