#! /bin/bash 
read $URL
curl $URL | grep "mailto"
