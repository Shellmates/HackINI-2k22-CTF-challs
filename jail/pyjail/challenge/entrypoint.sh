#!/bin/sh

USER="nobody"
EXEC="./challenge.py"
PORT=1337

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive,su="$USER" exec:"$EXEC",stderr
