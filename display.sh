#!/bin/bash

file=$1

uid=$(ngrep -W byline -I $file "uid" | grep -oP "uid=\K[^&]+")
passw=$(ngrep -W byline -I $file "passw" | grep -oP "passw=\K[^&]+")
echo "The username:$uid"
echo "The password:$passw"
