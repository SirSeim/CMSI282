class Powers:
    @staticmethod
    def main (a, b, c, p):
        return pow(a, pow(b, c), p)

print Powers.main(6, 6, 1, 3) # prints 0
