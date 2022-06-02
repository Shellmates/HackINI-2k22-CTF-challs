#! /usr/bin/python3

import logging
import sys

logging.basicConfig(stream = sys.stderr)
sys.path.insert(0, '/var/www/main-app')

from app import app as application