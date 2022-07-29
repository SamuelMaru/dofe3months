import random


def sum_ver_two(x, y):
    return x + y


def list_to_string(sentence):
    return (" ".join(sentence)).lstrip() + "."


def random_gen():
    return (random.randrange(0, 10), random.randrange(0, 10))


def func_4(x, y, z):
    print(max(x, y, z))


def replacing_stringthing(stringthing):
    return (
        stringthing.replace("A", "4")
        .replace("E", "3")
        .replace("I", "1")
        .replace("O", "0")
        .replace("U", "2")
    )


def encoded_string(encodedstring):
    """
    Returns a decoded string
    :param encodedstring:    string
    """
    return (
        encodedstring.replace("4", "A")
        .replace("3", "E")
        .replace("1", "I")
        .replace("0", "O")
        .replace("2", "U")
    )


def challenge_7(list_ints):
    return sum(list_ints)


def challenge_8(list_ints):
    return_list = []
    for i in list_ints:
        if i % 2 == 0:
            return_list.append(i)
    return return_list


def challenge_9(list_inputted):
    list_new = []
    for i in list_inputted:
        if i not in list_new:
            list_new.append(i)
    return list_new

if __name__ == "__main__":
    print("25_1_22")