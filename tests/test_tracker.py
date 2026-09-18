import unittest
import os
from src.catalog_manager import CatalogManager
from src.tracker import PrintTracker

class TestPrintTracker(unittest.TestCase):
    def setUp(self):
        self.test_catalog_path = "data/test_catalog.json"
        self.catalog = CatalogManager(filepath=self.test_catalog_path)
        self.tracker = PrintTracker(self.catalog)

    def tearDown(self):
        if os.path.exists(self.test_catalog_path):
            os.remove(self.test_catalog_path)

    def test_add_valid_item(self):
        item = self.tracker.add_order_item("bw_print_a4", 10)
        self.assertEqual(item.quantity, 10)
        self.assertEqual(item.subtotal, 20.0)

    def test_grand_total_calculation(self):
        self.tracker.add_order_item("bw_print_a4", 10) # 20.0
        self.tracker.add_order_item("spiral_binding", 1) # 30.0
        self.assertEqual(self.tracker.calculate_grand_total(), 50.0)

    def test_invalid_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            self.tracker.add_order_item("bw_print_a4", -5)

if __name__ == "__main__":
    unittest.main()