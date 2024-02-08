#!/bin/bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export FLASK_APP=app2.py
opentelemetry-instrument \
    --logs_exporter otlp \
    flask run -p 8084