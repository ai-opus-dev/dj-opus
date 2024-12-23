import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from agents.base_agent import BaseAgent

class MicroTrendModel(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=32):
        super(MicroTrendModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, 2)  # Buy or Sell signal

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

class PulseRider(BaseAgent):
    def __init__(self, agent_id="pulserider"):
        super().__init__(agent_id)
        self.current_model = MicroTrendModel()
        self.optimizer = optim.Adam(self.current_model.parameters(), lr=1e-3)
        self.criterion = nn.CrossEntropyLoss()

    def fetch_data(self):
        # Simulate fetching recent order book snapshots, price ticks
        # Here we just create dummy volatile price data
        data = np.random.randn(10)
        self.data_buffer = data

    def generate_signals(self):
        # Convert data to tensor
        inp = torch.tensor(self.data_buffer, dtype=torch.float32).unsqueeze(0)
        logits = self.current_model(inp)
        # Softmax to get probabilities
        probs = torch.softmax(logits, dim=1).detach().numpy()[0]

        # If buy probability > 0.5, generate buy signal, else sell signal
        signal = "BUY" if probs[0] > 0.5 else "SELL"
        return signal

    def execute_trades(self, signal):
        # Simulate trade execution
        # e.g., if BUY and we have free balance, buy a small fraction of an asset
        if signal == "BUY" and self.wallet_state["balance"] > 0:
            self.wallet_state["balance"] -= 10  # Buy action
        elif signal == "SELL":
            self.wallet_state["balance"] += 5   # Sell action
        # In real scenario, integrate with a DEX or centralized exchange API

    def train_model(self):
        # Placeholder: in reality, this would use historical data, labels, etc.
        # Here we simulate a quick training step
        dummy_input = torch.randn(32, 10)
        dummy_labels = torch.randint(0, 2, (32,))
        self.optimizer.zero_grad()
        logits = self.current_model(dummy_input)
        loss = self.criterion(logits, dummy_labels)
        loss.backward()
        self.optimizer.step()
