def func(var_a, var_b):
    return var_a + var_b

test_data = {4: (1,3), "ab": ("a", "b"), "df": ("f", "d")}

try:
    for key, value in test_data.items():

        if func(value[0], value[1]) == key:
            print("test pass")
        else:
            print("test fails")
except Exception as error:
    print(f"test failed due to: {error}")

else:
    print("sucessfully done")
