class SumCheck:

    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers

    def isSum(self, searched_sum):
        for summand1 in self.list_of_numbers:
            for summand2 in self.list_of_numbers:
                if summand1 + summand2 is searched_sum:
                    return True
        return False
