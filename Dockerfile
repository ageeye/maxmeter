FROM python:3
EXPOSE 5000
WORKDIR /src
RUN apt-get update && apt-get -y install cron joe
RUN pip install --no-cache-dir requests
COPY crontab /etc/cron.d/crontab
COPY maxmeter-test.py /src
RUN useradd -l -u 1000810000 -c "1000810000" 1000810000
RUN chmod 0644 /etc/cron.d/crontab
RUN touch /var/run/crond.pid
RUN chmod 744 /var/run/crond.pid
RUN /usr/bin/crontab /etc/cron.d/crontab
CMD ["tail", "-f", "/dev/null"]
