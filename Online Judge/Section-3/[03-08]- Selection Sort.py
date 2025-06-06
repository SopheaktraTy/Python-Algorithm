
def sort_descending(arr):
    return sorted(arr, reverse=True)


input_data = list(map(int,"1 2 3 4 5 6 7 8 9 10".split()))


sorted_data = sort_descending(input_data)

print(sorted_data)
