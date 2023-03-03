#!/bin/sh
ENTRYPOINT="python -m pytest --html=./test/report/report.html -W ignore::DeprecationWarning"
docker build -t pytest-runner .
docker run --rm -it -v $(pwd):/app pytest-runner $ENTRYPOINT