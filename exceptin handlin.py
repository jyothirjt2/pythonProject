a=5
b=2
k=int(print("enter a num: "))
print(k)
try:
    print(a/b)
except ZeroDivisionError as e:
    print("hey,u cannt divide by zer")
finally:
    print("file is clsed")
