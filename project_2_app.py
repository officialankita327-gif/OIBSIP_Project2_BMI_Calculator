def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Return BMI value = weight / (height^2)."""
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi: float) -> str:
    """
    Return BMI category based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def ask_positive_float(prompt: str) -> float:
    """User se positive number safely lena."""
    while True:
        value_str = input(prompt).strip()
        if value_str.lower() in ("exit", "quit"):
            print("Goodbye! 👋")
            exit()

        try:
            value = float(value_str)
            if value <= 0:
                print("Value must be greater than zero. Try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== BMI Calculator (Python) ===")
    print("Type 'exit' at any time to quit.\n")

    while True:
        print("\n--- New BMI Calculation ---")

        weight = ask_positive_float("Enter your weight (in kilograms): ")

        height_unit = input("Is your height in meters or centimeters? (m/cm): ").strip().lower()
        if height_unit not in ("m", "cm"):
            print("Invalid choice, assuming centimeters (cm).")
            height_unit = "cm"

        height_value = ask_positive_float("Enter your height: ")

        if height_unit == "cm":
            height_m = height_value / 100.0
        else:
            height_m = height_value

        bmi = calculate_bmi(weight, height_m)
        category = get_bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}\n")

        next_step = input("Calculate again? (y/n): ").strip().lower()
        if next_step != "y":
            print("Goodbye! 👋")
            break


if __name__ == "__main__":
    main()
