#!/bin/bash

set -e

echo ""
echo "begin deployment"

# login to aws ecr
aws ecr get-login --region=us-east-1 | bash -

# get the latest git hash
githash=`git rev-parse --short=7 HEAD`

# aws docker registry
docker_registry="505171167036.dkr.ecr.us-east-1.amazonaws.com/magic8"
image="$docker_registry:$githash"

# build and push each docker container
docker build -t $image .
docker push $image
