

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def prepare_data(self):
        result = []
        data = self.matrix_string.split('\n')
        for num in data:
            mid = []
            num_string = num.split()
            for num in num_string:
                mid.append(int(num))
            result.append(mid)
        return result

    def row(self, index):
        return self.prepare_data()[index - 1]

    def column(self, index):
        result = []
        data = self.prepare_data()
        for num in data:
            result.append(num[index - 1])
        return result
