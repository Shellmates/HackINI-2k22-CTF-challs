#!/bin/zsh

exec socat -v tcp-listen:1337,reuseaddr,fork,keepalive, EXEC:"./nutshell2",stderr
