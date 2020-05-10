FROM python:3

WORKDIR /app

RUN apt update && \
    apt install bash vim -y

RUN useradd -u 10012 -d /home/appuser appuser
RUN mkdir /home/appuser && chown -R appuser /home/appuser
RUN chown -R appuser /app
USER appuser

ADD . /app

RUN pip install -r requirements.txt --user

CMD ["/bin/bash", "-c", "set -e && ./entrypoint.sh"]

# docker build . -t c_bot 
# docker run --network="host" --rm -d --name cb c_bot