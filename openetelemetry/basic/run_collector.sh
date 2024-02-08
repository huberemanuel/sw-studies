#!/bin/bash
docker run -p 4317:4317 \
    -v $(pwd)/collector.yml:/etc/otel-collector-config.yaml \
    otel/opentelemetry-collector:latest \
    --config=/etc/otel-collector-config.yaml