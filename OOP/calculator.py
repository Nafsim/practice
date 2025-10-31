class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Math Error"

class CalculatorApp:
    def __init__(self):
        self.calc = Calculator()

    def run(self):
        while True:
            print("\n Simple Calculator" )
            print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
            choice = input("Enter what you want to do: ")

            if choice == "5":
                print("Exit")
                break

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", self.calc.add(a, b))
            elif choice == "2":
                print("Result:", self.calc.subtract(a, b))
            elif choice == "3":
                print("Result:", self.calc.multiply(a, b))
            elif choice == "4":
                print("Result:", self.calc.divide(a, b))
            else:
                print("Invalid choice")

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
