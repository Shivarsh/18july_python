my_dict = {'c': 3,'a': 1,'d': 4,'b': 2}


sorted_dict = sorted([(key, value) for (value, key) in my_dict.items()])


print("Sorted dictionary is :")
print(sorted_dict)
