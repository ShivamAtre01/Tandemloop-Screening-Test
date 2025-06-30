def generate_odd_series(n: int):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

if __name__ == "__main__":
    try:
        raw_input = input("Enter the value of a (positive integer): ")
        print(f"Raw input received: {raw_input}")
        a = int(raw_input)
        if a > 0:
            print("Output:", ", ".join(map(str, generate_odd_series(a))))
        else:
            print("Error: Please enter a positive integer.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid positive integer.")
