import random
import time

def generate_stream():
    while True:
        # normal values
        value = random.randint(10, 15)

        # inject anomaly occasionally
        if random.random() < 0.1:
            value = random.randint(40, 60)

        yield value
        time.sleep(0.5)
