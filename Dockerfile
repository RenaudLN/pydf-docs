FROM python:3.12-slim-buster

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN curl -fsSL https://pixi.sh/install.sh | bash

# Install package and its dependencies.
RUN pixi install

CMD gunicorn --timeout 0 run:server
