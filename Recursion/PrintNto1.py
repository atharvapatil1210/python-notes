def PrintNoto1(n):
    if n == 0 :
        return
    print(n)

    PrintNoto1(n-1)
    print(n)

PrintNoto1(7)
