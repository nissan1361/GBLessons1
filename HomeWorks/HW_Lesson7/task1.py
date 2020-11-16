class InitialMatrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        return self.data + other


class Matrix(InitialMatrix):
    def __init__(self, data):
        super(Matrix, self).__init__(data)


    def matrix1(self, input_data):
        self.data = [123]
        try:
            self.data = input_data
            print(self.data + "\n \n")
        except TypeError:
            print("Type Error!")

    def __str__(self):
        for sp in self.data.split():
            print(sp)

    #def __add__(self, other):
        #return Matrix(self.data + other.data)



tmp = [123]
matrix_var = input("Введите список списков в формате: 1,2,3  4,5,6  7,9,8 :\n>>")
mtrx = Matrix(tmp)

mtrx.matrix1(matrix_var)
mtrx.__str__()

#mtrx2 = Matrix(tmp)
#mtrx2.matrix1(matrix_var)
#print(mtrx + mtrx2)