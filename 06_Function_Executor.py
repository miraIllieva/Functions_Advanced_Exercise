def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")
    return "\n".join(result)


# Test code for sum and multiplication

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

# Testing the func_executor with sum_numbers and multiply_numbers
print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


# Test code for string manipulation

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

# Testing the func_executor with make_upper and make_lower
print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",))
))
