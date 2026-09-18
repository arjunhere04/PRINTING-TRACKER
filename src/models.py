from dataclasses import dataclass

@dataclass
class PrintItem:
    item_name: str
    quantity: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return round(self.quantity * self.unit_price, 2)