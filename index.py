# Part I
class MathDojo(object):
    def __init__(self):
        self.answer = 0

    def add(self, *num):
        for i in num:
            self.answer = self.answer + i
        return self

    def subtract(self, *num):
        for i in num:
            self.answer = self.answer - i
        return self

md = MathDojo().add(2).add(2, 5).subtract(3,2).answer
print md

#Part II

class MathDojo(object):
    def __init__(self):
        self.answer = 0

    def add(self, *num):
        for i in num:
            if isinstance(i, list) or isinstance(i, tuple):
                for j in i:
                    self.answer = self.answer + j
            else:
                self.answer = self.answer + i
        return self

    def subtract(self, *num):
        for i in num:
            if isinstance(i, list):
                for j in i:
                    self.answer = self.answer - j
            else:
                self.answer = self.answer - i
        return self

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).answer
print md