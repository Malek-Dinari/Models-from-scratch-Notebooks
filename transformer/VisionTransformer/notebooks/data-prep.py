import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset

# Simulate rPPG signal
def generate_synthetic_rPPG(batch_size, signal_length):
    # Generate synthetic signals and labels (e.g., heart rate ranges)
    signals = np.random.randn(batch_size, signal_length)  # Random 1D signals
    labels = np.random.randint(60, 100, size=(batch_size,))  # Heart rates
    return signals, labels

class rPPGDataset(Dataset):
    def __init__(self, signals, labels):
        self.signals = torch.tensor(signals, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.signals[idx], self.labels[idx]

# Generate dataset
batch_size, signal_length = 32, 128
signals, labels = generate_synthetic_rPPG(1000, signal_length)
dataset = rPPGDataset(signals, labels)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
