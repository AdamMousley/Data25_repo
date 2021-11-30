def alphabet_position(letter: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())
print("danny")
print(alphabet_position("C"))

def id_generator(name_string: str)->str:
    id = ""
    for letter in name_string:
        position = alphabet_position(letter)
        id += str(position)
    return id
print("danny")
print(id_generator("bob"))

def password_generator(name_string: str)-> str:
    number = 0
    for i in id_generator(name_string):
        number += int(i)
    return str(int(id_generator(name_string)) - number)
print("danny")
print(password_generator("bob"))
