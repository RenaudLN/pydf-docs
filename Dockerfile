FROM ghcr.io/prefix-dev/pixi:latest

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install package and its dependencies.
RUN pixi install

CMD pixi run gunicorn --timeout 0 run:server
