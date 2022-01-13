def Averages():
    my_list = []
    average = 0
    count = 0
    total = 0
    import sys
    print("Dame un número: ")
    numbergiven = int(sys.stdin.readline())

    while numbergiven != 0:
        count = +1
        my_list.append(numbergiven)
        print("Dame otro número: ")
        numbergiven = int(sys.stdin.readline())
        total = sum(my_list)
        average = (total/count)
        print(my_list)
    else:
        print("La media de los números introducidos es", average)

Averages()
