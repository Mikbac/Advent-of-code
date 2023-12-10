# cat sample | python3 task.py
# cat input | python3 task.py

#  Created by MikBac on 2021

numberCounter = 0
solution = 0

while True:
    try:

        # -- DETECT PART --

        segmentA = ''
        segmentB = ''
        segmentC = ''
        segmentD = ''
        segmentE = ''
        segmentF = ''
        segmentG = ''

        numberZero = ''
        numberOne = ''
        numberTwo = ''
        numberThree = ''
        numberFour = ''
        numberFive = ''
        numberSix = ''
        numberSeven = ''
        numberEight = ''
        numberNine = ''

        line = input().strip().split(' | ')
        partOne = line[0].strip()
        partTwo = line[1].strip()

        numbersFromOneToNine = partOne.split()
        numbers = partTwo.split()

        for n in numbersFromOneToNine:
            # number 1
            if len(n) == 2:
                numberOne = n

            # number 4
            if len(n) == 4:
                numberFour = n

            # number 7
            if len(n) == 3:
                numberSeven = n

            # number 8
            if len(n) == 7:
                numberEight = n

        # segment A
        for i in numberSeven:
            if i not in numberOne:
                segmentA = i

        # number 9
        for n in numbersFromOneToNine:
            if len(n) == 6:
                counter = 0
                for i in n:
                    if i in numberFour:
                        counter += 1
                if counter == 4:
                    numberNine = n

        # segment D
        for i in numberNine:
            if i not in numberFour and i not in numberSeven:
                segmentD = i

        # segment E
        for i in numberEight:
            if i not in numberNine:
                segmentE = i

        # number 6 and 0
        for n in numbersFromOneToNine:
            if len(n) == 6 and segmentE in n:
                counter = 0
                for i in n:
                    if i in numberOne:
                        counter += 1
                if counter == 1:
                    numberSix = n
                if counter == 2:
                    numberZero = n

        # segment G
        for i in numberSix:
            if i not in numberZero:
                segmentG = i

        # segment B
        for i in numberZero:
            if i not in numberSix:
                segmentB = i

        # number 5
        for n in numbersFromOneToNine:
            if len(n) == 5:
                counter = 0
                for i in n:
                    if i in numberSix:
                        counter += 1
                if counter == 5:
                    numberFive = n

        # number 2 and 3
        for n in numbersFromOneToNine:
            if len(n) == 5:
                counter = 0
                for i in n:
                    if i in numberFive:
                        counter += 1
                if counter == 3:
                    numberTwo = n
                if counter == 4:
                    numberThree = n

        # segment E
        for i in numberFive:
            if i not in numberThree:
                segmentF = i

        # segment C
        for i in numberThree:
            if i not in numberTwo:
                segmentC = i

        # -- PREDICT PART --

        encodedNumber = ''
        for n in numbers:

            # 0
            if len(n) == 6 and segmentA in n and segmentB in n and segmentC in n and segmentD in n and segmentE in n and segmentF in n:
                encodedNumber += '0'

            # 1
            if len(n) == 2:
                encodedNumber += '1'

            # 2
            if len(n) == 5 and segmentA in n and segmentB in n and segmentD in n and segmentE in n and segmentG in n:
                encodedNumber += '2'

            # 3
            if len(n) == 5 and segmentA in n and segmentB in n and segmentC in n and segmentD in n and segmentG in n:
                encodedNumber += '3'

            # 4
            if len(n) == 4:
                encodedNumber += '4'

            # 5
            if len(n) == 5 and segmentA in n and segmentC in n and segmentD in n and segmentF in n and segmentG in n:
                encodedNumber += '5'

            # 6
            if len(n) == 6 and segmentA in n and segmentC in n and segmentD in n and segmentE in n and segmentF in n and segmentG in n:
                encodedNumber += '6'

            # 7
            if len(n) == 3:
                encodedNumber += '7'

            # 8
            if len(n) == 7:
                encodedNumber += '8'

            # 9
            if len(n) == 6 and segmentA in n and segmentB in n and segmentC in n and segmentD in n and segmentF in n and segmentG in n:
                encodedNumber += '9'

        solution += int(encodedNumber)

    except EOFError:
        break

print('Solution = {}'.format(solution))
# 973499