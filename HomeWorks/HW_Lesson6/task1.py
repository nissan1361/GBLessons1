import time


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def __init__(self):
        self.__color.append(self)

    def running(self):
        check = 0
        while check < 3:
            print(self.__color[0])
            time.sleep(7)

            print(self.__color[1])
            time.sleep(2)

            print(self.__color[2])
            time.sleep(9)

            check += 1


light_torch = TrafficLight()

light_torch.running()
