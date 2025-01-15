import customtkinter as ctk

class TaxCalculator:
    def __init__(self):
        # initialisation de la fenetre
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        # Initialisation
        self.padding: dict = {"padx": 20, "pady": 10}

        # label et entrée
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # tax et entrée
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Percent:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        # resultat et entrée
        self.result_label = ctk.CTkLabel(self.window, text="Tax:")
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")
        self.result_entry.grid(row=2, column=1, **self.padding)

        # bouton de calcul
        self.calculate_button = ctk.CTkButton(self.window, text="Calculate", command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            self.update_result(f"€{income * (tax_rate / 100):,.2f}")
        except ValueError:
            self.update_result("Invalid input")


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    tax_calculator = TaxCalculator()
    tax_calculator.run()
