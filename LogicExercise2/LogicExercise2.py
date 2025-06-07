import sys

def roundN(n):
    if(n % 1000):
        return(1 + n // 1000) * 1000
    else:
        return n

def computeDebt(n):
    if(n == 0):
        return 100000
    return int(roundN(computeDebt(n-1) * 1.05))

result = computeDebt(int(input("Enter Number of Months: ")))
print("Amount of Debt: ", "$" + str(result).strip())

num = list(map(int, input("Enter 3 numbers: ").split()))

x,y,z = sorted(num)

if(x**2 + y**2 == z**2):
    print(True)
else:
    print(False)

a,b,c,d,e,f = map(float,input("Enter 5 numbers: ").split())
n = a * e - b * d

if(n != 0):
    x = (c * e - b * f) / n
    y = (a * f - c * d) / n

    print('{:.3f} {:.3f}'.format(x+0, y+0))





















