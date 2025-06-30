def generate_series_based_on_input(a: int):
    """
    Generate a series of odd numbers based on the input value.
    
    Parameters:
    a (int): The input value that determines the series output.
    
    Returns:
    list: A list of odd numbers.
    """
    series = []
    max_length = a if a % 2 != 0 else a - 1  # Series length matches largest odd number <= a
    for i in range(max_length):
        series.append(2 * i + 1)
    return series

# Example Usage
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer (a): "))
        if user_input > 0:
            result_series = generate_series_based_on_input(user_input)
            print("Output:", ", ".join(map(str, result_series)))
        else:
            print("Error: Please enter a positive integer.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid positive integer.")
