FROM python:3
EXPOSE 5000
WORKDIR /src
RUN apt-get update && apt-get -y install joe
RUN pip install --no-cache-dir requests pytz schedule
RUN touch /var/log/cron.log
RUN chown 1000720000:1000720000 /var/log/cron.log
COPY maxmeter.py /src
COPY cron.py /src
CMD ["/bin/sh", "-c", "python -u cron.py > /var/log/cron.log 2>&1"]
