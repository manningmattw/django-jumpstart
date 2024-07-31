# Pull base image (based on debian:bookworm-slim and python3)
FROM python:3-slim-bookworm

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /project_name

# Copy project and install dependencies
COPY . .
RUN pip install -r requirements.txt
