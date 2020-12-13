from random import randint, shuffle


RANGE = 100


def create_test_case():
    # get a list from [1 - RANGE]
    l = [x for x in range(1, RANGE + 1)]
    # randomize the locations of elements in the list
    shuffle(l)
    # get a random number between [1 - RANGE]
    dup = randint(1, RANGE + 1)
    # get a random index in the list
    i = randint(0, RANGE)
    # add the random number to a random index
    l.insert(i, dup)
    # return the test case and the duplicate (for validating the answer) ;)
    return l, dup


def check_answer(assumed_answer, correct_answer):
    # return true or false if answer is correct
    return assumed_answer == correct_answer


# TODO: find the duplicate value in l
def find_duplicate(l):
    d = {}
    
    for i in l:
        answer = 0
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    if d[i] == 2:
        answer = i
        
    
    
    # return the answer
    return answer


if __name__ == '__main__':
    # get the test case and the answer
    l, answer = create_test_case()

    # find the duplicate
    assumed_answer = find_duplicate(l)
    print(assumed_answer)
    # validate the answer
    if check_answer(assumed_answer, answer):
        print('You found the duplicate!', end=' ')
    else:
        print('You did NOT find the duplicate!', end=' ')

    # give the answer
    print('It was "{}"!'.format(answer))

