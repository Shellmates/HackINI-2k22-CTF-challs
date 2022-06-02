#!/bin/zsh

exec socat -v tcp-listen:1337,reuseaddr,fork,keepalive, EXEC:"/home/supreme/supreme",stderr
