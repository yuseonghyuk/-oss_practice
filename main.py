def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

print("A:")
A = int(input())

print("B:")
B = int(input())

print("op:")
op = input()

if op == "+":
    print(add(A, B))
elif op == "-":
    print(sub(A,B))
elif op == "*":
    print(mul(A, B))
