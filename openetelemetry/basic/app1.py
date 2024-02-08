from random import randint
from flask import Flask
import logging

from opentelemetry import trace

# Acquire a tracer
tracer = trace.get_tracer("diceroller.tracer")

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/rolldice")
def roll_dice():
    logger.info("Outside roll")
    return str(roll())

def roll():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("roll") as rollspan:
        rollspan.add_event("Inside roll", {"2": 2})
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        return res
