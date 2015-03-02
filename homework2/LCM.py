class LCM:
    @staticmethod
    def lcm (value1, value2):
        return (value1 * value2) / LCM.gcd(value1, value2)

    @staticmethod
    def gcd (value1, value2):
        while value1:
            value1, value2 = value2 % value1, value1
        return value2

print LCM.lcm(6, 9) # Prints 18