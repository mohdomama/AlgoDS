def max_heapify(array, i):
    heap_size = len(array)
    '''
    general formula is l = 2i, r = 2i + 1
    for indices starting from 1
    '''
    l = 2*(i+1) - 1
    r = 2*(i+1)
    largest = i

    if l < heap_size:
        if array[l] > array[largest]:
            largest = l
    if r < heap_size:
        if array[r] > array[largest]:
            largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)


def build_max_heap(array):
    base = int(len(array) / 2) # general fromula
    base = base -1 #indices start form 0
    for i in range(base, -1, -1):
        max_heapify(array, i)


if __name__ == '__main__':
    array = [1, 5, 6, 8, 12, 14, 16]
    build_max_heap(array)
    print(array)