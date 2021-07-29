

if __name__ == '__main__':
    n = int(raw_input())
    i = 0
    print("-------From 0 to number onwards")
    while i < n:
        print(i**2)
        i = i + 1
    print("-------From number to 0 backwards")
    i = n
    while i >= 0:
        if i < n:
            print(i**2)
        i = i - 1
