from src.detector import AnomalyDetector
from src.stream_simulator import generate_stream

detector = AnomalyDetector(window_size=5, threshold=2.5)

stream = generate_stream()

try:
    for value in stream:
        result = detector.update(value)

        if result["status"] == "anomaly":
            print(f"🚨 Anomaly: {result}")
        else:
            print(f"Normal: {value}")

except KeyboardInterrupt:
    print("\nStopped by user.")
