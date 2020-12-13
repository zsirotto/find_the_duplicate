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


# find the duplicate value in l
def find_duplicate(l):
    # initilize a frequency array to count the elements in l
    frequency_array = [0] * len(l)
    # iterate over each element in l
    for element in l:
        # increase the frequency count of each element
        frequency_array[element] += 1
        # if an element's frequency == 2, we found the duplicate
        if frequency_array[element] == 2:
            return element
    # there is no duplicate
    return None


if __name__ == '__main__':
    # get the test case and the answer
    l, answer = create_test_case()

    # find the duplicate
    assumed_answer = find_duplicate(l)

    # validate the answer
    if check_answer(assumed_answer, answer):
        print('You found the duplicate!', end=' ')
    else:
        print('You did NOT find the duplicate!', end=' ')

    # give the answer
    print('It was "{}"!'.format(answer))
