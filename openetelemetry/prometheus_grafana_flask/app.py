from flask import Flask

from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware

from prometheus_client import REGISTRY, generate_latest

app = Flask(__name__)

app.wsgi_app = OpenTelemetryMiddleware(app.wsgi_app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/metrics")
def handle_metrics():
    return generate_latest(REGISTRY)