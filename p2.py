n=int(input("Starting point "))
a=int(input("Ending point   "))
def function_(a):
    if a==n:
        print("Thanks")
        return
    print(a)
    function_(a-1)
function_(a)
def function_1(n):
    if n==a+1:
        print("Thanks")
        return
    print(n)
    function_1(n+1)
function_1(n)