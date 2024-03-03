class Calculator:
    def __init__(self):
        self.equation = ""

    def add_to_equation(self, value):
        self.equation += str(value)

    def clear_equation(self):
        self.equation = ""

    def calculate_result(self):
        try:
            result = eval(self.equation)
            return result
        except Exception as e:
            return "Error"

if __name__ == "__main__":
    calc = Calculator()

