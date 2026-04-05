import numpy as np

class AnomalyDetector:
    def __init__(self, window_size=10, threshold=2.5):
        self.window_size = window_size
        self.threshold = threshold
        self.window = []

    def update(self, value):
        # Cold Start Handling
        if len(self.window) < self.window_size:
            if len(self.window) > 1:  # need at least 2 points for std
                mean = np.mean(self.window)
                std = np.std(self.window)

                if std > 0:
                    z_score = (value - mean) / std

                    if abs(z_score) > self.threshold:
                        return {
                            "status": "anomaly",
                            "value": value,
                            "z_score": float(z_score),
                            "mean": float(mean),
                            "std": float(std),
                            "phase": "cold_start"
                        }

            # if normal OR not enough data → add to window
            self.window.append(value)

            return {
                "status": "collecting",
                "value": value,
                "window_size": len(self.window)
            }

        # Normal Detection Phase
        mean = np.mean(self.window)
        std = np.std(self.window)

        if std == 0:
            # all values same → treat as normal
            self.window.append(value)
            self.window.pop(0)

            return {
                "status": "normal",
                "value": value,
                "z_score": 0.0,
                "mean": float(mean),
                "std": float(std)
            }

        z_score = (value - mean) / std

        # Anomaly Detection
        if abs(z_score) > self.threshold:
            return {
                "status": "anomaly",
                "value": value,
                "z_score": float(z_score),
                "mean": float(mean),
                "std": float(std),
                "phase": "detection"
            }

        # Normal → update window
        self.window.append(value)
        self.window.pop(0)

        return {
            "status": "normal",
            "value": value,
            "z_score": float(z_score),
            "mean": float(mean),
            "std": float(std)
        }
