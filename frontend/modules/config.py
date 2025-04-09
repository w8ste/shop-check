from datetime import datetime

class Config:
    def __init__(self):
        self.is_purchase_modal_open = False
        self.is_budget_modal_open = False
        self.selected_month = datetime.now().month
        self.selected_year = datetime.now().year
        self.selected_db = f"{self.selected_year}_{self.selected_month}.db"
        self.budget_path = "./assets/budgets.json"
        self.default_budget = 0

    def update_month_and_year(self):
        split = self.selected_db.split("_")

        self.selected_year = int(split[0])
        self.selected_month = int(split[1].split(".")[0])

