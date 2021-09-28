

def main():
    y=int(input()) #renglones
    x=int(input()) #columnas
    b=x*y
    i=0
    listas=[]
    while i<b:
        u=int(input())
        listas.append(u)
        i=i+1
    yu=[]
    for element in listas:
            if element <10:
                yu.append(element)
    print(yu)            



if __name__=='__main__':
    main()
