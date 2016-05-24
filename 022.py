
def names_sort_sum(list_names):
	sorted_names = sorted(list_names)
	result = (sum(i * sum(ord(letter) - 64 for letter in name)
		for i, name in enumerate(sorted_names, 1)))

	return result


with open("p022_names.txt", 'rb') as f:
    names = f.read().strip('"')
    list_names = names.split('","')

print names_sort_sum(list_names)
