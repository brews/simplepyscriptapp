# simplepyscriptapp

Example of a Docker application image based on a very simple Python script.

Running this container simply prints "simplescript.py is running" to stdout, with some logging metadata.


## Building and running

Build the Docker image with
```
docker build -t simplepyscriptapp .
```

Run the built image with
```
docker run simplepyscriptapp
```
