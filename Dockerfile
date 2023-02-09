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
RUN groupadd crond-users && \
    chgrp crond-users /var/run/crond.pid && \
    usermod -a -G crond-users 1000810000
RUN /usr/bin/crontab /etc/cron.d/crontab
USER 1000810000
CMD ["cron", "-f"]
