# Simplest otel example

This as a Flask API with one endpoint following [this](https://opentelemetry.io/docs/languages/python/getting-started/) tutorial.

Requirements:
* Python 3.10.11

## Tutorial as it is

Install flask and werkzeug (why?):

`pip install 'flask<3' 'werkzeug<3'`

Install opentelemetry:

`pip install opentelemetry-distro # SDK, API` 

Bootstrap it (witchcraft?):

`opentelemetry-bootstrap -a install # Automatic Instrumentation`

### Automatic Instrumentation

A running python program that injects bytecode into your application to capture telemetry from [popular](https://opentelemetry.io/ecosystem/registry/?language=python&component=instrumentation) frameworks and libraries.

### Bootstrap

The command `opentelemetry-bootstrap -a install` scans the `site-packages` folder and install needed telemtry packages such as `opentelemetry-instrumentation-flask`.
Therefore, in a new project, first set up your application and then bootstrap otel.

Run it:

```bash
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8084
```

> Note that we can configure different exporters for traces, metrics and logs.

Your terminal should be printing out the events (metrics, logs and traces) in the temrinal, such as:

```
 * Debug mode: off
{
    "body": "\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n * Running on http://127.0.0.1:8084",
    "severity_number": "<SeverityNumber.INFO: 9>",
    "severity_text": "INFO",
    "attributes": {
...
```

## Manual instrumentation

With automatic instrumentation, spans are automatically created, but wait. What is a span? It's basically a context level of the current application scope. For example:

```
GET /rolldice
    /roll
```

Where `/roll` is a child of `/rolldice` since it was created inside that scope. 
Therefore, information stored inside a specific span will belong to that span.

We can add events inside a span with `.add_event(message, attrs)` that are similar to a log message.

To try it out, execute `run1.sh`

## Metrics

Inside a `span` we can track metrics, such as the number of hits in a page (count), how many times an API was called, etc. Example (from app2.py):

```py
roll_counter = meter.create_counter(
    "dice.rolls",
    description="The number of rolls by roll value",
)
...
roll_counter.add(1, {"roll.value": result})
```

## Exporting results

We want to make our traces, metrics and logs available for other people. 
In that way, we need to export this data. 
There are several [exporters](https://opentelemetry.io/docs/languages/python/exporters/) supported by the SDK.
A common one is the otlp exporter (gRPC or proto) that sends the data in a binary format to a server such as otel/opentelemetry-collector (run_collector.sh), Jeager, Prometheus, etc.