#!/usr/bin/env bash

#Build docker image
docker build --tag=capstone

# List docker images
docker image list

# Run django app
docker run -p 8000:8000 capstone