
try:
    print(x)
    
except TypeError as t:
    print('TypeError triggered')

except NameError as n:
    print('NameError triggered')
    print(str(n))

except Exception as e:
    print('General Exception')
    print(str(e))
