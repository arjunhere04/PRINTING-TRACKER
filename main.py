import sys
from src.catalog_manager import CatalogManager
from src.tracker import PrintTracker

def display_menu():
    print("\n" + "="*38)
    print("   CAMPUS PRINT & STATIONERY HUB   ")
    print("="*38)
    print("1. View Rate Catalog")
    print("2. Add Item to Current Order")
    print("3. Update or Add Rate to Catalog")
    print("4. Generate Receipt & Print Total")
    print("5. Clear Current Order")
    print("6. Exit")
    print("="*38)

def main():
    catalog = CatalogManager()
    tracker = PrintTracker(catalog)

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print("\n--- Current Catalog Rates ---")
            for item, price in catalog.rates.items():
                print(f" • {item.replace('_', ' ').title():<22} : ₹{price:.2f}")

        elif choice == '2':
            item_name = input("Enter item/service name: ").strip()
            if not item_name:
                print("[!] Error: Item name cannot be empty.")
                continue

            try:
                qty = int(input(f"Enter quantity for '{item_name}': "))
            except ValueError:
                print("[!] Error: Quantity must be a valid integer.")
                continue

            existing_price = catalog.get_price(item_name)
            if existing_price is None:
                print(f"[i] '{item_name}' is not in standard catalog.")
                try:
                    custom_price = float(input(f"Enter custom unit price for '{item_name}' (₹): "))
                    added_item = tracker.add_order_item(item_name, qty, custom_price)
                except ValueError as e:
                    print(f"[!] Error: {e}")
                    continue
            else:
                try:
                    added_item = tracker.add_order_item(item_name, qty)
                except ValueError as e:
                    print(f"[!] Error: {e}")
                    continue

            print(f"[✓] Added: {qty} x {item_name.title()} @ ₹{added_item.unit_price:.2f} each.")

        elif choice == '3':
            item_name = input("Enter item name to add/update: ").strip()
            try:
                new_price = float(input(f"Enter price for '{item_name}' (₹): "))
                catalog.update_or_add_item(item_name, new_price)
                print(f"[✓] Updated rate for '{item_name.title()}' to ₹{new_price:.2f}")
            except ValueError as e:
                print(f"[!] Error: Invalid numeric input or price <= 0.")

        elif choice == '4':
            if not tracker.current_order:
                print("\n[!] No items added to active order session yet.")
                continue

            print("\n" + "="*45)
            print("         ITEMIZED PRINT & HUB RECEIPT        ")
            print("="*45)
            print(f"{'Item':<20} | {'Qty':<4} | {'Unit (₹)':<8} | {'Total (₹)':<8}")
            print("-" * 45)
            for item in tracker.current_order:
                name_disp = item.item_name.replace('_', ' ').title()[:18]
                print(f"{name_disp:<20} | {item.quantity:<4} | ₹{item.unit_price:<7.2f} | ₹{item.subtotal:<7.2f}")
            print("-" * 45)
            print(f"Total Items Printed/Bought : {tracker.calculate_total_items()}")
            print(f"Grand Total Amount Payable  : ₹{tracker.calculate_grand_total():.2f}")
            print("="*45)

        elif choice == '5':
            tracker.clear_order()
            print("[✓] Active order session cleared successfully.")

        elif choice == '6':
            print("Exiting Campus Print Hub Manager. Goodbye!")
            sys.exit()
        else:
            print("[!] Invalid option selected. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()