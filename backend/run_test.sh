#!/bin/sh
ENTRYPOINT="python -m pytest --cov=backend --html=test/report/report.html -W ignore::DeprecationWarning -s --capture=fd --log-cli-level=INFO" 
(cd backend && docker build -t pytest-runner .)
(cd backend && docker run --rm -it -v $(pwd):/backend pytest-runner $ENTRYPOINT)