#!/bin/sh
ENTRYPOINT="python -m pytest --cov=backend --html=test/report/report.html -W ignore::DeprecationWarning"
docker build -f ./app/backend/Dockerfile -t pytest-runner .
docker run --rm -it -v $(pwd)/app:/app pytest-runner $ENTRYPOINT