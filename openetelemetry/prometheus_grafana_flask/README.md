# Simplest example with Prometheus and Grafana

Prometheus is a monitoring system that allows to store metrics collected by otel SDK (manual or automatic instrumentation).
It works with a pull model, meaning that a Prometheus server will query our application for metrics (at /metrics).

For that, we need to install the Prometheus intrumentation from otel:

`pip install opentelemetry-exporter-prometheus==0.43b0`

We need to manually define the route with:

```py
from prometheus_client import REGISTRY, generate_latest

@app.route("/metrics")
def handle_metrics():
    return generate_latest(REGISTRY)
```

`generate_latest` just grabs latest metrics from a Registry. 
A registry is a client implementation (from prometheus_client) that knows how to get relevant metrics.

Since the Prometheus server will hit out application for the metrics, we just need to inform the server where our application is located.
Let's do it and start the prometheus server:

`docker compose up -d prometheus`

This service will use the `prometheus.yml` configuration file that informs where our application is:

`- targets: ['host.docker.internal:8084']`

> 'host.docker.internal' is used to search for the app in the host machine (I'm using wsl2).

By running `docker compose up -d` you should be able to access the application at `localhost:8084` and to see the metrics in a grafana dashboard `localhost:3000`.