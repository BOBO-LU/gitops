#!/bin/sh
ENTRYPOINT="python -m pytest --cov=backend --html=.app/backend/test/report/report.html -W ignore::DeprecationWarning"
docker build -t pytest-runner .
docker run --rm -it -v $(pwd)/app:/app pytest-runner $ENTRYPOINT