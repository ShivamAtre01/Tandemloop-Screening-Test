class Calculator:
    def __init__(self, a: float, b: float, operation_type: str):
        #In python a and b are explicitly expected to be float, corresponding to double in other languages
        self.a = a
        self.b = b
        self.operation_type = operation_type.lower()

    def compute(self):
        """
        Perform the specified operation based on the operation type.
        Returns:
        float or str: Result of the operation or error message.
        """
        if self.operation_type == "add":
            return self.a + self.b
        elif self.operation_type == "subtract":
            return self.a - self.b
        elif self.operation_type == "multiply":
            return self.a * self.b
        elif self.operation_type == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero is not allowed"
        else:
            return "Error: Invalid operation type"

# Example Usage
if __name__ == "__main__":
    # Inputs
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the type of operation (add, subtract, multiply, divide): ")

    # Create an instance of the calculator
    calc = Calculator(a, b, operation)

    # Compute and print the result
    result = calc.compute()
    print("Result:", result)
