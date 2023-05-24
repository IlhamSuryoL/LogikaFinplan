def bilangan(N):
    count = 0
    num = 1
    while count < N:
        if num % 3 == 0 and num % 7 == 0:
            print("Z")
        elif num % 3 == 0 or num % 7 == 0:
            print(num)
        num += 1
        count += 1

bilangan(29)

