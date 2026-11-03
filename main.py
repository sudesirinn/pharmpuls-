import os
import json
import argparse

class InventoryManager:
    def __init__(self, data_path="data/inventory.json"):
        self.data_path = data_path
        self._ensure_file()

    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        if not os.path.exists(self.data_path):
            initial_data = {"Parol": {"quantity": 3, "threshold": 5, "category": "Medication"}}
            with open(self.data_path, "w", encoding="utf-8") as f:
                json.dump(initial_data, f, ensure_ascii=False, indent=4)

    def load_inventory(self):
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def update_item(self, item_name, quantity, threshold=None, category="General"):
        inventory = self.load_inventory()
        inventory[item_name] = {"quantity": quantity, "threshold": threshold or 5, "category": category}
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(inventory, f, ensure_ascii=False, indent=4)

class StockMonitor:
    def __init__(self):
        self.manager = InventoryManager()

    def check_critical_stock(self):
        return [item for item in self.manager.load_inventory().items()
                if item[1]["quantity"] < item[1]["threshold"]]

    def report_status(self):
        inventory = self.manager.load_inventory()
        for name, data in inventory.items():
            print(f"Ürün: {name} | Miktar: {data['quantity']} | Eşik: {data['threshold']} | Kategori: {data['category']}")

def main():
    parser = argparse.ArgumentParser(description="Pharmacy CLI")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--update", type=str)
    parser.add_argument("--qty", type=int)
    args = parser.parse_args()

    monitor = StockMonitor()
    if args.status:
        monitor.report_status()
    elif args.check:
        for item in monitor.check_critical_stock():
            print(f"Kritik Stok Uyarı: {item[0]} (Miktar: {item[1]['quantity']})")
    elif args.update and args.qty is not None:
        monitor.manager.update_item(args.update, args.qty)
        print(f"{args.update} başarıyla güncellendi.")

if __name__ == "__main__":
    main()