print("Enter at least five integers ")
user_lst = list(map(int,input().split()))
user_tup = tuple(user_lst)
user_set = set(user_lst)
user_fst = frozenset(user_set)
user_dict = {i:i**2 for i in user_lst}

print(f'Original List: {user_lst}')
print(f'Converted Tuple : {user_tup}')
print(f'Converted Set removing Duplicated : {user_set}')
print(f'Original List: {user_lst}')
print(f'Converted frozen set {user_fst}')
print(f'Dictionary of squares : {user_dict}')