def func(var_a, var_b):
    return var_a + var_b

test_data = {4: (1,3), "ab": ("a", "b"), "df": ("f", "d")}

errors = []

for key, value in test_data.items():
    try:
        assert key == func(*value), f"test fails wiyh {key}, {value}"
    except AssertionError as error:
        errors.append(error)

assert not errors, print(errors)