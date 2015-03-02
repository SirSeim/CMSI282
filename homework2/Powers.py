class Powers:
    @staticmethod
    def main (a, b, c, p):
        bmp = b % (p - 1)
        bcmp = Powers.power(bmp, c)
        amp = a % p
        return Powers.power(amp, bcmp)

    @staticmethod
    def mod_power (base, power, mod):
        answer = 1
        for i in range(1, power):
            answer = ((answer * base) % mod)
        return answer

    @staticmethod
    def power (base, power):
        if power == 0:
            return 1
        if power == 1:
            return base
        if Powers.is_odd(power):
            return base * Powers.power(base * base, (power - 1) / 2)
        else:
            return Powers.power(base * base, power / 2)

    @staticmethod
    def is_odd (num):
        return num % 2 == 0

print Powers.main(6, 9, 1, 7)

print Powers.mod_power(6, 9, 7)

print pow(6, 9, 4)
