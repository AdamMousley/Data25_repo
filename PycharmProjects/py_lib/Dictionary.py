from pprint import pprint

dictionary_variable = {"Danny": ["Green","Emerald","Turquoise"],
                       "Jade": {"Fav colour": "Teal", "Least_fave": "Red"}, "Ensty": "Blue"}

# print(dictionary_variable["Danny"])
#
# for i in dictionary_variable.keys():
#     print(dictionary_variable[i])

# for i in dictionary_variable.values():
#     print(i)

print(dictionary_variable["Danny"][2])
print(dictionary_variable["Jade"]["Least_fave"])

pprint(dictionary_variable)