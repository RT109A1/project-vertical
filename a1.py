import pickle
LIST_users = [1111111]
with open('users.sfh', 'wb') as file:
    pickle.dump(LIST_users, file)