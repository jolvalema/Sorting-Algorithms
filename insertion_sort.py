def insertion_sort(unsorted_list):
	for i in range(1, len(unsorted_list)):
		j = i - 1
		next_item = unsorted_list[i]
		while (unsorted_list[j] > next_item) and (j >= 0):
			unsorted_list[j+1] = unsorted_list[j]
			j = j - 1
		unsorted_list[j+1] = next_item

unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(unsorted_list)
print(unsorted_list)