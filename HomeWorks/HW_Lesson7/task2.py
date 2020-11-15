from abc import ABC, abstractmethod

class Wear(ABC):

    @abstractmethod
    def materials(self):
        pass

class Coat:
    def __init__(self, size):
        self.size = size

    def materials(self):
        mat = self.size/6.5 + 0.5
        return mat


class Suite:
    def __init__(self, high):
        self.high = high

    def materials(self):
        mat = 2 * self.high + 0.3
        return mat


wear1 = Coat(56)
wear2 = Suite(199)
print("Ткани на куртку: " + str(wear1.materials()))
print("Ткани на костюм: " + str(wear2.materials()))