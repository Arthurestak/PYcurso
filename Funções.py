num = 0

def soma(*a):
    global num
    for i in a:
        num += i
    print(num)
soma(1,2,3,4,5,6,7)