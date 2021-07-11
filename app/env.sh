#!/bin/bash
function main(){
    docker image build -t docker-flask-api .
    docker run -p 5000:5000 docker-flask-api
}

main