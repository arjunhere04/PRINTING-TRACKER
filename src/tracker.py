from src.models import PrintItem
from src.catalog_manager import CatalogManager


class PrintTracker:

    def __init__(self, catalog_manager: CatalogManager):
        self.catalog_manager = catalog_manager
        self.current_order = []

    def add_order_item(self, item_name: str, quantity: int, custom_price: float = None) -> PrintItem:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        clean_name = item_name.lower().strip()
        unit_price = self.catalog_manager.get_price(clean_name)

        if unit_price is None:
            if custom_price is None or custom_price <= 0:
                raise ValueError(f"Item '{item_name}' not in catalog. Valid custom price required.")
            unit_price = custom_price
            self.catalog_manager.update_or_add_item(clean_name, custom_price)

        item = PrintItem(item_name=clean_name, quantity=quantity, unit_price=unit_price)
        self.current_order.append(item)
        return item

    def calculate_grand_total(self) -> float:
        return round(sum(item.subtotal for item in self.current_order), 2)

    def calculate_total_items(self) -> int:
        return sum(item.quantity for item in self.current_order)

    def clear_order(self):
        self.current_order.clear()