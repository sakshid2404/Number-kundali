import math
def check():
   
    r=int(input("enter a number-"))

  #square
    s=r*r
    print("square of given number -",s)

  #cube    
    a=r**3
    print("cube root of given number -",a)

  #odd or even
    if(r%2==0):
        print("even number")
    else:
        print("odd number")

  #square root
    print("square root-",math.sqrt(r))


  #factorial
    s=1
    for i in range(1,r+1):
        s*=i

    print("factorial-",s)
check()