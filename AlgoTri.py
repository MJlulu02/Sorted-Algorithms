import random, time

def triBulle():
    mx = int(input("Nombre Max random : "))
    elem = int(input('Nombre D\'élement dans le tableau : '))

    T = [random.randint(1,mx) for _ in range(elem)]
    n = len(T)
    
    for j in range(1, n):
        for i in range(0,n-j):
            if T[i] > T[i+1]:
                T[i],T[i+1] = T[i+1], T[i]

def triSelection():
    mx = int(input("Nombre Max random : "))
    elem = int(input('Nombre D\'élement dans le tableau : '))

    T = [random.randint(1,mx) for _ in range(elem)]

     for i in range(len(T)):
       min = i
       for j in range(i+1, len(tab)):
           if T[min] > T[j]:
               min = j
                
       tmp = T[i]
       T[i] = T[min]
       T[min] = tmp

def triInsertion(): 
    mx = int(input("Nombre Max random : "))
    elem = int(input('Nombre D\'élement dans le tableau : '))

    T = [random.randint(1,mx) for _ in range(elem)]
    
    for i in range(1, len(tab)): 
        k = T[i] 
        j = i-1
        while j >= 0 and k < T[j] : 
                T[j + 1] = T[j] 
                j -= 1
        T[j + 1] = k
