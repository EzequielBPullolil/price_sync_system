#!/bin/bash


service nginx start


gunicorn -b 0.0.0.0:8000 "src.app:create_app()"


tail -f /dev/null
