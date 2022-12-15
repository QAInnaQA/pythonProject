data = []

for i in range(5):
    data.append(lambda x: x + i)

print(data[-1](10))
print(data[1](10))

def fun()
    print ("first")

# 1)определяем фукнцию
def foo(x):
# 3)выполняем функцию
    value = x**2
    return value
# 2)вызываем функцию
foo(3)