def shell_sort(data: list[int]) -> list[int]:
    """
    The function implementing the shell sort algorithm
    :param: data (list[int]) - our list, which will sorting.
    :return: (list[int]) - the new sorted list.
    """
    length = len(data)
    step = length // 2
    while step > 0:
        for ind in range(step, length, 1):
            key = data[ind]
            tmp = ind - step
            while tmp >= 0 and data[tmp] > key:
                data[tmp + step] = data[tmp]
                tmp -= step
            data[tmp + step] = key
        step //= 2
    return data


def get_own_count(array: list[int]) -> int:
    """
    The function calculating amount of team's own numbers.
    :param: array (list[int]) - The sorted list.
    :return: (int) - count of team's own numbers.
    """
    index = 0
    count = 0
    length = len(array)
    while index < length - 2:
        if array[index] == array[index + 1] == array[index + 2]:
            count += 1
            index += 3
        elif array[index] == array[index + 1] != array[index + 2]:
            index += 2
        elif array[index] != array[index + 1]:
            index += 1
    return count


lst = []

for i in range(3):
    n = int(input())
    lst += list(map(int, input().split()))

print(lst)

print(get_own_count(shell_sort(lst.copy())))
