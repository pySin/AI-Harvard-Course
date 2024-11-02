# Objects used as dictionary keys

class O1:

    def __init__(self, num):
        self.num = num


test_object_1 = O1(1)
test_object_2 = O1(2)

dict_1 = dict()
dict_1[test_object_1, test_object_2] = 3
print(dict_1[test_object_1, test_object_2])

