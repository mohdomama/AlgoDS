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


def extract_max(array):
    if len(array) < 1:
        raise IndexError('Heap Empty!')

    max_el = array[0]
    array[0] = array[-1]
    array.pop()
    max_heapify(array, 0)
    return max_el


def increase_key(array, i, val):
    if val < array[i]:
        raise ValueError('Cannot decrease value!')

    array[i] = val
    parent = int((i+1) / 2) - 1
    # General formula is floor(i/2)

    while(i > 0 and array[parent] < array[i]):
        array[parent], array[i] = array[i], array[parent]
        i = parent
        parent = parent = int((i+1) / 2) - 1


def insert_element(array, elem):
    array.append(elem)
    increase_key(array, len(array)-1, elem)



def main():
    array = [1, 5, 6, 8, 12, 14, 16]
    build_max_heap(array)
    print(array)
    
    insert_element(array, 3)
    print(array)

    insert_element(array, 17)
    print(array)


if __name__ == '__main__':
    main()