import random
import numpy as np


def list_generator(length):
    limit = length * 2
    len_of_lists = random.sample(range(1, limit), length)
    base_for_lists = np.random.randint(-limit, limit, size=limit)
    final_list = []

    for odd_i in range(length):
        temp = np.random.choice(base_for_lists, len_of_lists[odd_i])
        if odd_i & 1:
            final_list.append(
                sorted(temp, reverse=True)
            )
        else:
            final_list.append(
                sorted(temp)
            )

    return final_list
