from cs50 import get_int



def mario_int():
    while True:
        i = get_int("Height Please:")
        if i > 0 and i <= 8:
            break
    return i

n = mario_int()

for k in range(1,n+1):
    for j in range(n-k):
        print(" ",end="")
    print("#"*k,end="\n")
    
