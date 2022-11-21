# formasi 1
def starFormation1(n):
    for i in range(n+1) :
        print("*" * i)
starFormation1(5)
# formasi 2
def starFormation2(n):
    for i in range(n) :
        print("*" * (n- i))
starFormation2(5)

# formasi 3
def starFormation3(n):
    m = n//2+1
    starFormation1(m)
    starFormation2(n-m)
starFormation3(7)
    
