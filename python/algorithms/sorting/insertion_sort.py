def insertion_sort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array


if __name__ == "__main__":
    array = [16, 3, 15, 5, 2, 10, 7, 9, 11, 6, 13, 1, 8, 14, 0, 18, 4, 17, 12]
    print(array)
    array = insertion_sort(array)
    print(array)
