#!/bin/bash

socat -dd -T60 TCP-LISTEN:8000,reuseaddr,fork,su=ctf EXEC:/home/ctf/challenge.py,stderr
