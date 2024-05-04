import tkinter as tk
from tkinter import ttk

class NutritionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Nutrition Calculator")
        
        self.age_label = ttk.Label(root, text="Age(years):")
        self.age_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.age_entry = ttk.Entry(root)
        self.age_entry.grid(row=0, column=1, padx=5, pady=5)

        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=5, pady=5)

        self.height_label = ttk.Label(root, text="Height (cm):")
        self.height_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.height_entry = ttk.Entry(root)
        self.height_entry.grid(row=2, column=1, padx=5, pady=5)

        self.gender_label = ttk.Label(root, text="Gender:")
        self.gender_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(root, textvariable=self.gender_var, values=["Female", "Male"])
        self.gender_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.metabolic_rate_label = ttk.Label(root, text="Metabolic rate:")
        self.metabolic_rate_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.metabolic_rate_var = tk.StringVar()
        self.metabolic_rate_combobox = ttk.Combobox(root, textvariable=self.metabolic_rate_var, values=["Very low", "Low", "Mid", "High", "Very high"])
        self.metabolic_rate_combobox.grid(row=4, column=1, padx=5, pady=5)

        self.physical_activity_label = ttk.Label(root, text="Physical activity intensity:")
        self.physical_activity_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.physical_activity_var = tk.StringVar()
        self.physical_activity_combobox = ttk.Combobox(root, textvariable=self.physical_activity_var, values=["Very low", "Low", "Mid", "High", "Very high"])
        self.physical_activity_combobox.grid(row=5, column=1, padx=5, pady=5)

        self.blood_pressure_label = ttk.Label(root, text="Blood pressure:")
        self.blood_pressure_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.blood_pressure_var = tk.StringVar()
        self.blood_pressure_combobox = ttk.Combobox(root, textvariable=self.blood_pressure_var, values=["Hypotension", "Normal", "Hypertension"])
        self.blood_pressure_combobox.grid(row=6, column=1, padx=5, pady=5)

        self.diabetic_label = ttk.Label(root, text="Diabetic:")
        self.diabetic_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.diabetic_var = tk.StringVar()
        self.diabetic_combobox = ttk.Combobox(root, textvariable=self.diabetic_var, values=["Normal", "High", "Severely high"])
        self.diabetic_combobox.grid(row=7, column=1, padx=5, pady=5)

        self.heart_disease_label = ttk.Label(root, text="Heart disease:")
        self.heart_disease_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.heart_disease_var = tk.StringVar()
        self.heart_disease_combobox = ttk.Combobox(root, textvariable=self.heart_disease_var, values=["Yes", "No"])
        self.heart_disease_combobox.grid(row=8, column=1, padx=5, pady=5)

        self.lactose_intolerance_label = ttk.Label(root, text="Lactose Intolerance:")
        self.lactose_intolerance_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        self.lactose_intolerance_var = tk.StringVar()
        self.lactose_intolerance_combobox = ttk.Combobox(root, textvariable=self.lactose_intolerance_var, values=["Normal", "High", "Severely high"])
        self.lactose_intolerance_combobox.grid(row=9, column=1, padx=5, pady=5)

        self.nutrition_goal_label = ttk.Label(root, text="Nutrition goal:")
        self.nutrition_goal_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.nutrition_goal_var = tk.StringVar()
        self.nutrition_goal_combobox = ttk.Combobox(root, textvariable=self.nutrition_goal_var, values=["Gain weight", "Lose weight", "Maintain weight", "Gain muscle", "Gain endurance"])
        self.nutrition_goal_combobox.grid(row=10, column=1, padx=5, pady=5)

        self.calculate_button = ttk.Button(root, text="Calculate", command=self.calculate_nutrition)
        self.calculate_button.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

        self.output_label = ttk.Label(root, text="Output:")
        self.output_label.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=12, column=1, padx=5, pady=5)

    def calculate_nutrition(self):
        age = int(self.age_entry.get())
        weight = int(self.weight_entry.get())
        height = int(self.height_entry.get())
        gender = self.gender_var.get()
        metabolic_rate = self.metabolic_rate_var.get()
        physical_activity_intensity = self.physical_activity_var.get()
        blood_pressure = self.blood_pressure_var.get()
        diabetic = self.diabetic_var.get()
        heart_disease = self.heart_disease_var.get()
        lactose_intolerance = self.lactose_intolerance_var.get()
        nutrition_goal = self.nutrition_goal_var.get()

        # Perform calculation based on input attributes
        # Dummy calculation for demonstration
        proteins = 70
        carbohydrates = 250
        fats = 55
        calcium = 1200
        vitamin_a = 1200
        vitamin_c = 800
        calories = 2600

        output_text = f"Proteins: {proteins}g\nCarbohydrates: {carbohydrates}g\nFats: {fats}g\nCalcium: {calcium}mg\nVitamin_A: {vitamin_a}mcg\nVitamin_C: {vitamin_c}mg\nCalories: {calories}kcal"
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output_text)

def main():
    root = tk.Tk()
    app = NutritionCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
