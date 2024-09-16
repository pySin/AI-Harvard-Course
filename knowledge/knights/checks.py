# Check code pieces
# Class methods Recall

# class BasicPizza:
#
#     def __init__(self, main_1, main_2,  extra_1: str, extra_2: str):
#         self.main_1 = main_1
#         self.main_2 = main_2
#         self.extra_1 = extra_1
#         self.extra_2 = extra_2
#
#     @classmethod
#     def peperoni(cls):
#         return cls("dove", "tomato", "peperoni", "salami")
#
#     @classmethod
#     def mushroom(cls):
#         return cls("dove", "tomato", "mushroom", "cheese")
#
#
# peperoni_pizza = BasicPizza.peperoni()
# print(peperoni_pizza.extra_1)
# print(peperoni_pizza.extra_2)
# mushroom_pizza = BasicPizza.mushroom()
# print(mushroom_pizza.extra_1)
# print(mushroom_pizza.extra_2)

# -- Simple function string return

# def text_1():
#     return "a"
#
#
# def text_2():
#     return "b"
#
#
# def text_c(letter):
#     return letter + "c"
#
#
# print(text_1() + text_2())
# print(text_c(text_1()))

# -- sorted() recall

# words = ["ino", "you", "I", "immobilized"]
#
#
# def sorted_by_vowels(word):
#     vowel_count = 0
#     for letter in word:
#         if letter in "aoiue":
#             vowel_count += 1
#     return vowel_count
#
#
# def sorted_by_consonants(word):
#     vowel_count = 0
#     for letter in word:
#         if letter not in "aoiue":
#             vowel_count += 1
#     return vowel_count
#
#
# sorted_words = sorted(words, key=len)
# print(sorted_words)
#
# sort_by_vowels = sorted(words, key=sorted_by_vowels, reverse=True)
# print(sort_by_vowels)
#
# sort_by_consonants = sorted(words, key=sorted_by_consonants)
# print(f"Sorted by Consonants: {sort_by_consonants}")

# -- Validate that object is from particular class

# class Particular:
#
#     def __init__(self):
#         self.collection: list = []
#
#     @classmethod
#     def validate(cls, part):
#         if isinstance(part, Particular):
#             print(f"The object is of type Particular: {part}")
#         else:
#             raise TypeError("The object must be of type Particular!")
#
#     def __repr__(self):
#         return f"Particular Object"
#
#
# part_1 = Particular()
# print(part_1)
# Particular.validate(part_1)
# a = 1
# Particular.validate(a)


# hash() function
# Produces the same number(hash code) from the same content

# class a1:
#     @staticmethod
#     def text_return():
#         return "a1"
#
#
# class a2:
#     @staticmethod
#     def text_return():
#         return "a1"

# hash_1 = hash("a1")
# hash_2 = hash(l1)
# hash_2b = hash(l2)
# print(hash_1)
# print(hash_2)
# print(hash_2b)


# o1 = a1()
# o2 = a2()
#
# hash_3 = hash(o1.text_return())
# hash_4 = hash(o2.text_return())
# print(f"Hash 3: {hash_3}")
# print(f"Hash 4: {hash_4}")


# -- Check if key in dictionary

# named_collection = {"one": 1, "two": 2, "three": 3, "four": 4}
# name = "five"
#
#
# def key_check(dict_x, name_1):
#     try:
#         return bool(dict_x[name_1])
#     except KeyError as ke:
#         return f"Key {ke} is not in the dictionary!"
#
#
# print(key_check(named_collection, name))
# print(key_check(named_collection, "four"))

# -- Logic classes try
# If he gets a bit more money from work he was visiting the Black Club.
from logic import *


symbol1 = Symbol("A bit more money from work")
symbol2 = Symbol("Visiting the Black Club")

knowledge_x = And(
    Not(symbol1)
)
result = model_check(knowledge_x, symbol1)
print(result)


