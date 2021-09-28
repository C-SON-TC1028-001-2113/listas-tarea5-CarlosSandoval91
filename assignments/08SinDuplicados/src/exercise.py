
def main():
    #escribe tu código abajo de esta línea
    x= int(input())
    i=0
    listas=[]
    if x>0:
        while i<x:
            u=str(input())
            listas.append(u)
            i=i+1
        print (listas)
        yu=[]
        for element in listas:
            if element not in yu:
                yu.append(element)
        print (yu)

    else:
        print('Error')    

    pass

if __name__=='__main__':
    main()
