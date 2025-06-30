def count_multiples(numbers):
    """
    Count how many numbers in the list are multiples of integers from 1 to 9.
    
    Parameters:
    numbers (list): List of integers to be checked.
    
    Returns:
    dict: A dictionary with keys as numbers from 1 to 9 and values as their counts.
    """
    # Initialize dictionary to store counts
    multiples_count = {i: 0 for i in range(1, 10)}
    
    # Check each number in the input list
    for number in numbers:
        for key in multiples_count.keys():
            if number % key == 0:
                multiples_count[key] += 1
    
    return multiples_count

if __name__ == "__main__":
    try:
        # Take input from the user
        user_input = input("Enter numbers separated by commas: ")
        numbers = list(map(int, user_input.split(',')))
        
        # Get the multiples count
        result = count_multiples(numbers)
        print("Output:", result)
    except ValueError:
        print("Error: Please enter valid integers separated by commas.")
