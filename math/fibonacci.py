class Fibonacci:
    def __init__(self, number):
        self.d = {0: 1, 1: 1, 2: 2}
        self.n = number
        if self.n > 2:
            for i in range(3, self.n):
                self.d[i] = self.d[i - 1] + self.d[i - 2]

    def fibonacci_nth_number(self):
        return self.d[self.n - 1]

    def sum_of_fibonacci_numbers(self):
        return sum(self.d.values())

if __name__ == '__main__':
    print Fibonacci(100).fibonacci_nth_number()
    print Fibonacci(100).sum_of_fibonacci_numbers()
