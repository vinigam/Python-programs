def the_boat():
    "Variables that control number of jesuits and cannibals in both sides and an array that contain the sequence of the user choice"
    jesuits = 3
    cannibals = 3

    jesuits_other_side = 0
    cannibals_other_side = 0

    another_side = 0

    sequence = []
    departure_boat = 0
    return_boat = 0

    " As long as the number of Jesuits is greater than the cannibals the user can make choices to solve the problem"

    while another_side < 6 and (jesuits >= cannibals and jesuits > 0) or another_side < 6 and jesuits < 1:

        print('this side: ')
        for i  in range(0, jesuits):
            print('J ')

        print('-------')

        for i in range(0, cannibals):
            print('C ')

        print('\n')

        print('other side')
        for i  in range(0, jesuits_other_side):
            print('J ')

        print('-------')

        for i in range(0, cannibals_other_side):
            print('C ')

        print('\n')

        flag = 0
        while flag != 1:
            traveler1 = int(input('who should go 1 ?(1- cannibal 2-jesuit 3- none)\n'))
            traveler2 = int(input('who should go ?1-cannibal 2-jesuit 3- none\n'))

            if traveler1 == 0 and traveler2 == 0:
                print('invalid')

            else:
                departure_boat+=1
                "----------------------------------------------------------------------------------------------------"
                if traveler1 == 1 and cannibals > 0:
                    cannibals-=1
                    cannibals_other_side+=1
                    another_side+=1

                    sequence.append("{}-departure C ".format(departure_boat))
                elif cannibals < 1:
                    print('empty cannibals1')

                if traveler2 == 1 and cannibals > 0:
                    cannibals -= 1
                    cannibals_other_side += 1
                    another_side += 1

                    sequence.append("{}-departure C ".format(departure_boat))
                elif cannibals < 1:
                    print('empty cannibals2')
                "----------------------------------------------------------------------------------------------------"
                if traveler1 == 2 and jesuits > 0:
                    jesuits-=1
                    jesuits_other_side+=1
                    another_side+=1

                    sequence.append("{}-departure J ".format(departure_boat))
                elif jesuits < 1:
                    print('empty jesuits1')
                if traveler2 == 2 and jesuits > 0:
                    jesuits -= 1
                    jesuits_other_side += 1
                    another_side += 1

                    sequence.append("{}-departure J ".format(departure_boat))
                elif jesuits < 1:
                    print('empty jesuits2')

                if traveler1 == 1 or traveler1 == 2 or traveler1 == 3:
                    flag = 1
                if traveler2 == 1 or traveler2 == 2 or traveler2 == 3:
                    flag = 1

                "----------------------------------------------------------------------------------------------------"
                if jesuits > 0:
                    if cannibals > jesuits:
                        break
                if jesuits_other_side > 0:
                    if cannibals_other_side > jesuits_other_side:
                        break

                print('this side: ')
                for i in range(0, jesuits):
                    print('J ')

                print('-------')

                for i in range(0, cannibals):
                    print('C ')

                print('\n')

                print('other side')
                for i in range(0, jesuits_other_side):
                    print('J ')

                print('-------')

                for i in range(0, cannibals_other_side):
                    print('C ')

                print('\n')

                flag2 = 0
                while flag2 != 1:
                    traveler1 = int(input('who should back 1 ?(1- cannibal 2-jesuit 3- none)\n'))
                    traveler2 = int(input('who should back ?1-cannibal 2-jesuit 3- none\n'))

                    if traveler1 == 0 and traveler2 == 0:
                        print('invalid')

                    else:
                        return_boat+=1
                        "----------------------------------------------------------------------------------------------"
                        if traveler1 == 1 and cannibals_other_side > 0:
                            cannibals += 1
                            cannibals_other_side -= 1
                            another_side -= 1

                            sequence.append("{}-return C ".format(return_boat))
                        elif cannibals_other_side < 1:
                            print('empty cannibals_other_side1')

                        if traveler2 == 1 and cannibals_other_side > 0:
                            cannibals += 1
                            cannibals_other_side -= 1
                            another_side -= 1

                            sequence.append("{}-return C ".format(return_boat))
                        elif cannibals_other_side < 1:
                            print('empty cannibals_other_side2')
                        "----------------------------------------------------------------------------------------------"
                        if traveler1 == 2 and jesuits_other_side > 0:
                            jesuits += 1
                            jesuits_other_side -= 1
                            another_side -= 1

                            sequence.append("{}-return J ".format(return_boat))
                        elif jesuits_other_side < 1:
                            print('empty jesuits_other_side1')
                        if traveler2 == 2 and jesuits_other_side > 0:
                            jesuits += 1
                            jesuits_other_side -= 1
                            another_side -= 1

                            sequence.append("{}-return J ".format(return_boat))
                        elif jesuits_other_side < 1:
                            print('empty jesuits_other_side2')

                        "----------------------------------------------------------------------------------------------"
                        if traveler1 == 1 or traveler1 == 2 or traveler1 == 3:
                            flag2 = 1
                        if traveler2 == 1 or traveler2 == 2 or traveler2 == 3:
                            flag2 = 1

                        if jesuits > 0:
                            if cannibals > jesuits:
                                break
                        if jesuits_other_side > 0:
                            if cannibals_other_side > jesuits_other_side:
                                break




        if jesuits_other_side > 0:
            if not jesuits_other_side >= cannibals_other_side:
                break
    if another_side == 6:
        print('Right sequence \n {}'.format(sequence))
    elif jesuits < cannibals or jesuits_other_side < cannibals_other_side:
        print('Wrong sequence \n {}'.format(sequence))
        print('this side: ')
        for i in range(0, jesuits):
            print('J ')

        print('-------')

        for i in range(0, cannibals):
            print('C ')

        print('\n')

        print('other side')
        for i in range(0, jesuits_other_side):
            print('J ')

        print('-------')

        for i in range(0, cannibals_other_side):
            print('C ')

        print('\n')


the_boat()