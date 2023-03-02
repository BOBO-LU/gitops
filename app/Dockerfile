FROM python:3.9 as requirements-stage 
WORKDIR /tmp 
RUN pip install poetry 
COPY ./pyproject.toml ./poetry.lock* /tmp/ 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes 


FROM python:3.9 
WORKDIR /app/backend 
COPY --from=requirements-stage /tmp/requirements.txt ./requirements.txt 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt 
CMD ["python", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app", "--reload"]
