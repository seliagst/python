def starFormation(n):
    for i in range(n) :
        for j in range(i+1) :
            print("*", end=" ")
        print()
def starFormation1(n):
    for i in range(n) :
        for j in range(i, n) :
            print("*", end=" ")
        print()
def starFormation2(n):
     starFormation(n)
     starFormation1(n)      
starFormation2(int(input("Jumlah n:")))
