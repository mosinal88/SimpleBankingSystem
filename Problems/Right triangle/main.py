class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if self.c ** 2 == self.a ** 2 + self.b ** 2:
            self.s = round(0.5 * self.a * self.b, 1)
        else:
            self.s = "Not right"


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
right_triangle = RightTriangle(input_c, input_a, input_b)
print(right_triangle.s)
