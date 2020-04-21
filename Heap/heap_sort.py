import heap

def sort(array):
	'''An in space version of this can be implemented
	We will have to maintain a heap data structure with
	heap_size attribute
	'''
	
	sorted_arr = [0] * (len(array))
	arr_size = len(array) -1 

	for i in range(arr_size, -1, -1):
		sorted_arr[i] = heap.extract_max(array)

	return sorted_arr

def main():
	array = [16, 7, 9, 0 , 1, 5, 4, 13]
	heap.build_max_heap(array)
	array = sort(array)
	print(array)

if __name__ == '__main__':
	main()