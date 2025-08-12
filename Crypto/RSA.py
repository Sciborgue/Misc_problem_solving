def slow_expmod(b, e, m):
    result = 1
    for _ in range(e):
        result *= b
        result %= m
    return result


def fast_expmod_from_lsb_to_msb(b, e, m):
    result = 1
    k = e.bit_length()
    subresult = b
    for i in range(k):
        bit = e & (1 << i)
        if bit != 0:
            result *= subresult
            result %= m
        subresult *= subresult
        subresult %= m
    return result


def fast_expmod_from_msb_to_lsb(b, e, m):
    result = 1
    for bit in f"{e:b}":
        result *= result
        if bit != "0":
            result *= b
        result %= m
    return result


fast_expmod = fast_expmod_from_msb_to_lsb


class RSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q
        # set coprime
        self.e = e
        # set totient
        self.phi = (p - 1) * (q - 1)
        # computation of d, the modular multiplicative inverse of e[]
        self.d = self.euc_etendu(self.e, self.phi)[0] % self.phi

    def encrypt(self, m):
        self.c = fast_expmod(m, self.e, self.n)
        return self.c

    def decrypt(self, c):
        m_dec = 1
        for j in range(self.d):
            m_dec *= c
            m_dec = m_dec % self.n
            print(c, m_dec)
        return m_dec

    def euc_etendu(self, a, b):
        if b == 0:
            return 1, 0  # gcd, x, y
        else:
            x1, y1 = self.euc_etendu(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            print(f"x: {x}, y: {y}, a: {a}, b: {b}")
            return x, y


def main():
    rsa = RSA(61, 53, 17)
    a1 = rsa.encrypt(65)
    print(f"Encrypted message: {a1}")
    b1 = rsa.decrypt(2790)
    print(f"Decrypted message: {b1}")


def test():
    n = 50
    for b in range(n):
        for e in range(n):
            for m in range(2, n):
                assert (
                    slow_expmod(b, e, m) == fast_expmod(b, e, m) == pow(b, e, m)
                ), f"Failed for b={b}, e={e}, m={m}"


def test_perf():
    for _ in range(100):
        e = 2**255 - 19
        b = 1487720846
        m = 39881773273972
        assert fast_expmod(b, e, m) == pow(b, e, m), f"Failed for b={b}, e={e}, m={m}"
