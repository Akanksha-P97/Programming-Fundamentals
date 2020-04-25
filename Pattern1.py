for level in range(3):
    for k in range(3-level):
        print(" ", end=" ")
    for x in range(2*level+1):
        print("*" ,end=" ")
    print()