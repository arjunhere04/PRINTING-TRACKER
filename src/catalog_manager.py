import json
import os

class CatalogManager:

    
    def __init__(self, filepath="data/catalog.json"):
        self.filepath = filepath
        self.rates = {}
        self.load_catalog()

    def load_catalog(self):

        if not os.path.exists(self.filepath):
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            self.rates = {
                "bw_print_a4": 2.0,
                "color_print_a4": 10.0,
                "spiral_binding": 30.0,
                "soft_binding": 50.0,
                "lab_record_notebook": 65.0,
                "blue_book": 15.0
            }
            self.save_catalog()
        else:
            try:
                with open(self.filepath, "r") as f:
                    self.rates = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.rates = {"bw_print_a4": 2.0, "color_print_a4": 10.0}

    def save_catalog(self):
        with open(self.filepath, "w") as f:
            json.dump(self.rates, f, indent=4)

    def get_price(self, item_name: str):
        return self.rates.get(item_name.lower().strip(), None)

    def update_or_add_item(self, item_name: str, price: float):
        if price <= 0:
            raise ValueError("Item price must be greater than zero.")
        self.rates[item_name.lower().strip()] = round(price, 2)
        self.save_catalog()