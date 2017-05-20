from random import randint, shuffle


def generate_answers(minimum, maximum, step):
    """
    Generates A, B, and C answers to quiz questions, where player have to guess
    how many items of a given category is in a container
    :param minimum: minimal amount of items in a container
    :param maximum: maximal amount of items in a container
    :param step: defines spred of the generated answers, eg. 2 for min-max 10-20 == [10, 12, 14, 16, 18, 20]
    :return: tuple containing list of all possible answers, and correct answer
    """

    scope = [num for num in range(minimum, maximum+1, step)]
    ind = randint(0, len(scope)-3)

    answers = scope[ind:ind+3]
    shuffle(answers)

    # Returns all answers, and correct one
    return answers, answers[0]


if __name__ == "__main__":
    for _ in range(10):
        all_answers = generate_answers(10, 50, 2)
        print(all_answers)
