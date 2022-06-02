#!/bin/sh

EXEC="./stronk-boi"
PORT=1337

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
