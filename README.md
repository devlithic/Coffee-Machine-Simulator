# Coffee-Machine-Simulator
This project simulates a coffee machine using Python. It allows users to choose between espresso, latte, and cappuccino, insert virtual coins, and get feedback on whether they have inserted enough money and whether the machine has enough resources to make the drink. The machine also provides change when needed and keeps track of available resources and revenue.

🔧 Features
Choose from three types of coffee: Espresso, Latte, or Cappuccino.

Insert coins: quarters, dimes, nickels, and pennies.

Automatic check for sufficient resources (water, milk, coffee).

Calculates total money inserted and returns change if overpaid.

Displays current machine report (resources and money).

Stops working when resources are insufficient and displays a refill message: You need to refill the machine ☕🔄.

📦 Structure
report_machine: Dictionary to track available water, milk, coffee, and money.

Individual drink recipes and costs (espresso, LATTE, CAPPUCCINO).

enter_money(): Calculates total money inserted.

ressource_machine(): Checks if enough ingredients are available.

choix_*(): Deducts the ingredients when a drink is selected.

change_*(): Calculates and displays change based on user input.

report(): Returns the current machine status.
