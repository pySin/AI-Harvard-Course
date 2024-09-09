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

words = ["ino", "you", "I", "immobilized"]


def sorted_by_vowels(word):
    vowel_count = 0
    for letter in word:
        if letter in "aoiue":
            vowel_count += 1
    return vowel_count


sorted_words = sorted(words, key=len)
print(sorted_words)

sort_by_vowels = sorted(words, key=sorted_by_vowels, reverse=True)
print(sort_by_vowels)
