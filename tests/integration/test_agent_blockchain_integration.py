import abc
from typing import Dict, Any

class BaseAgent(abc.ABC):
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.current_model = None
        self.performance_metrics = {
            "profitability": 0.0,
            "latency": 0.0,
            "accuracy": 0.0,
            "strategic_cohesion": 0.0
        }

        # Sealed environment states
        self.internal_state = {}
        self.data_buffer = []
        self.wallet_state = {"balance": 1000.0}  # Example starting balance

    @abc.abstractmethod
    def fetch_data(self):
        """Fetch domain-specific data: market, social, fundamental, etc."""
        pass

    @abc.abstractmethod
    def generate_signals(self) -> Any:
        """Generate trading signals or investment recommendations."""
        pass

    @abc.abstractmethod
    def execute_trades(self, signals):
        """Execute trades on-chain or via exchange API."""
        pass

    @abc.abstractmethod
    def train_model(self):
        """Retrain or fine-tune internal models (e.g., after catalyst request)."""
        pass

    def update_performance_metrics(self, new_metrics: Dict[str, float]):
        # Called internally or externally to update performance
        for k, v in new_metrics.items():
            self.performance_metrics[k] = v

    def report_metrics(self) -> Dict[str, float]:
        # Returns metrics to the Omnichron Catalyst
        return self.performance_metrics
