#!/bin/sh

EXEC="./challenge"
socat -d -T60 tcp-l:1337,reuseaddr,fork,keepalive,su=nobody exec:$EXEC,stderr
