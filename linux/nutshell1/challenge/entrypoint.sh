#!/bin/zsh

exec socat -v tcp-listen:1337,reuseaddr,fork,keepalive, EXEC:"./nutshell1",stderr
