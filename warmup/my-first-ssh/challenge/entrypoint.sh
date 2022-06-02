#!/bin/sh

EXEC="./chall.sh"
PORT=1337

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
