import numpy as np
import random

class QxBinEdge:
    """QxBin Logic for Edge Computing: Probabilistic Qubit Simulation for IoT Decision Making"""
    
    def __init__(self, size=4):
        # Binary Probability Matrix: rows as states, columns as probabilities
        self.bpm = np.random.rand(size, 2)  # Prob of 0 and 1
        self.bpm /= self.bpm.sum(axis=1, keepdims=True)  # Normalize to probabilities
    
    def simulate_qubit(self, measurements=10):
        """Simulate fractional state measurements"""
        results = []
        for _ in range(measurements):
            state_probs = self.bpm.mean(axis=0)
            result = np.random.choice([0, 1], p=state_probs)
            results.append(result)
        return results, np.mean(results)
    
    def adaptive_decision(self, sensor_data):
        """Use case: Probabilistic decision in edge device"""
        prob_1 = np.mean(sensor_data) * 0.5 + 0.5  # Fuse data
        decision = 1 if random.random() < prob_1 else 0
        return decision

if __name__ == "__main__":
    edge = QxBinEdge()
    results, avg = edge.simulate_qubit()
    print("Edge QxBin Results:", results, "Avg:", avg)
    print("Decision for sensor:", edge.adaptive_decision([0.1, 0.3, 0.8]))