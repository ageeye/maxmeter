FROM python:3
EXPOSE 5000
WORKDIR /src
RUN apt-get update && apt-get -y install joe
RUN pip install --no-cache-dir requests pytz schedule
COPY maxmeter-test.py /src
COPY cron.py /src
CMD ["/src/cron.py"]
