class Methods:
    def Sumnatural(self, n):
        return (n * (n + 1)) // 2
    
    def Factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.Factorial(n - 1)
        
    def Fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)