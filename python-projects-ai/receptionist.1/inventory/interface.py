from abc import ABC, abstractmethod
from typing import List, Dict, Any
from models.vehicle import Vehicle

class InventoryProvider(ABC):
    @abstractmethod
    def search_part(self, vehicle: Vehicle, part_name: str) -> List[Dict[str, Any]]:
        """
        Searches for a part based on vehicle details.
        Should return a list of dictionaries with keys:
        - name: str
        - price: float
        - availability: str (e.g. "In Stock", "Out of Stock", "Available at nearby store")
        - part_number: str
        - url: str
        """
        pass
