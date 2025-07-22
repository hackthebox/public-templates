#!/bin/bash
NAME="challenge_name"
CAT="category"
docker rm -f $CAT_$NAME
docker build --tag=$CAT_$NAME . 
docker run -p 1337:1337 --rm --name=$CAT_$NAME --detach $CAT_$NAME