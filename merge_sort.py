def merge_sort(unsorted_list):
	if(len(unsorted_list) <= 1):
		return unsorted_list
	middle = len(unsorted_list) // 2
	left_half = unsorted_list[:middle]
	right_half = unsorted_list[middle:]
	left_half = merge_sort(left_half)
	right_half = merge_sort(right_half)
	return list(merge(left_half, right_half))


def merge(left_half, right_half):
	res = []
	while len(left_half) != 0 and len(right_half) != 0:
		if left_half[0] < right_half[0]:
			res.append(left_half[0])
			left_half.remove(left_half[0])
		else:
			res.append(right_half[0])
			right_half.remove(right_half[0])
	if len(left_half) == 0:
		res = res + right_half
	else:
		res = res + left_half
	return res

unsorted_list = [69, 35, 28, 11, 29, 18, 156]

print(merge_sort(unsorted_list))