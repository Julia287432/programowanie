def print_slupek(equation):
    parts = equation.split('+')
    first_number = parts[0].strip()
    second_number = parts[1].strip()
    result = int(first_number) + int(second_number)
    
    
    print(first_number.rjust(4))
    print("+", second_number)
    print("-----")
    print(result)

if __name__ == "__main__":
    equation = input("Podaj działanie (np. '235 + 72'): ")
    print_slupek(equation)

