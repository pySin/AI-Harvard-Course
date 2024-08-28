# Checks

# Unknown variable in one line IF
# directory = sys.argv[1] if len(sys.argv) == 2 else "large"

# list_1 = [1, 2, 3]
#
# num = list_1[3] if len(list_1) > 1 else 90
# print(num)

# Evaluating function

class EvaluationCheck:

    def __init__(self, nums):
        self.nums = nums

    def empty(self):
        return len(self.nums) == 0

    def remove_num(self):
        self.nums.pop()


numbers = [1, 2, 3, 4, 5]
ec = EvaluationCheck(numbers)
for i in range(len(numbers) + 1):
    print(f"Empty expression: {ec.empty()}")
    if ec.empty():
        print(f"Numbers Finished!")
        break
    print(f"Numbers: {ec.nums}")
    ec.remove_num()
