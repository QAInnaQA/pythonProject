import string

data = [y for y in string.ascii_lowercase + string.printable + string.ascii_uppercase]
#print(data)

#print(data.count("a"))

def get_data(var:str):
    new_data = []
    for i in range(len(data)):
        if data[i] == var:
            new_data.append(data[1])
    return new_data

def comp(actual: str, expected = "d"):
    return actual == expected
def comp_0(actual: str, expected = "a"):
    return actual == expected
#new_data = get_data("a")
#print(new_data)

#new_data_0 = get_data("d")
#print(new_data_0)

newest_data = filter(comp, data)
newest_data_0 = filter(lambda x: x =="6", data)

print(list(newest_data))
print(list(newest_data_0))

old_data = map(lambda x: x.upper(), data)
print(list(old_data))



