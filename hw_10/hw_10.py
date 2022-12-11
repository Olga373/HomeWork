class Triangle:

    def __init__(self, side_list):
        self.side_list = side_list

    def is_possible(self):
        self.side_list.sort()
        a = self.side_list[0]
        b= self.side_list[1]
        c = self.side_list[2]

        if a + b > c:
            print(("Tringle is possible"))
        else:
            print("Ttingle is not possible")

tringle = Triangle([5, 1, 2])
print(tringle.is_possible())

