
x = 6

def example3():
    global x
    x += 1
    print(x)

def example():
    z = 5
    print(z)

# cannot do this:
#print(z)

def example2():
    z = 7
    print(z)
    y = x + 1
    print(y)
    return y

x = example2()
print(x)


    













    
