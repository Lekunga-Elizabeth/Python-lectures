def get_even_numbers(n):
    even_numbers = []
    for i in range(n):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(get_even_numbers(10))