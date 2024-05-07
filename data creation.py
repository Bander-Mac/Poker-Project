file = open("Small Blind.csv", 'w')

skip = False
for i in range(1, 21):
    file.write(f'{i}: ')
    print("for blind:", i)
    skips = []
    num1 = input("Enter first number: ")
    num2s = []
    string = ''

    while num1 != "":
        num2 = input("Enter first range num: ")
        while num2 != "":
            num2s.append(int(num2))
            num2 = input("Enter range num: ")
        skips.append([num1, num2s])
        num1 = input("Enter first number: ")
    for i in range(1, 15):
        for j in range(1, 15):
            message = f'({i}, {j}), '
            for skipnums in skips:
                print('Checking skip:', skipnums)
                for nums in sorted(skipnums[1]):
                    print('Checking range:', nums)
                    nummessage = f'({int(skipnums[0])}, {nums}), '
                    if message == nummessage:
                        print('skipping', nummessage)
                        skip = True
                    else:
                        string += message
    file.write(string + '\n')
