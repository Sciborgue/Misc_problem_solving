P = 2**255 - 19
A = 486662
x_9 = 9
y_9 = 14781619447589544791020593568409986887264606134616475288964881837755586237401


def ecc_trans_naivegen(x1, x2, y1, y2, m):
    x3 = ((y1 - y2) / (x1 - x2)) ** 2 - x1 - x2
    y3 = -(y1 - y2) / (x1 - x2) * (x3 - x1) - y1
    return x3, y3
def ecc_trans_mod(x1, x2, y1, y2, m):
    x3 = ((y1 - y2) * pow((x1 - x2), -1, m)) ** 2 - x1 - x2
    y3 = -(y1 - y2) * pow((x1 - x2), -1, m) * (x3 - x1) - y1
    return x3 % m, y3 % m

def ecc_trans_naive25519(x1: int,  y1: int, x2: int, y2: int) -> tuple[int, int] | None:
    if x1 == x2:
        if y1 != y2:
            assert y1 == -y2 % P
            return None
        else:
            c = (3 * x1**2 + 2 * A * x1 + 1) * pow(2 * y1, -1, P)
    else:
        c = (y2 - y1) * pow(x2 - x1, -1, P)

    x3 = c**2 - A - x1 - x2
    y3 = (x1 - x3) * c - y1
    return x3 % P, y3 % P

def multip_naive(x, y, e):
    x_r = x
    y_r = y
    for _ in range(e - 1):
        result = ecc_trans_naive25519(x, y, x_r, y_r)
        assert result != None
        x_r, y_r = result
    return x_r, y_r


def multip_fastexp(x:int, y:int, e:int)->tuple[int, int] :
    # Let's consider e as its binary expression and browse from msb to lsb
    x_r = x
    y_r = y
    for bit in f"{e:b}"[1:]:
        result = ecc_trans_naive25519(x_r, y_r, x_r,  y_r)
        assert result != None
        x_r, y_r = result
        if bit != "0":
            result = ecc_trans_naive25519(x, y, x_r,  y_r)
            assert result != None
            x_r, y_r = result
    return x_r, y_r


def main():
    alice_secret = 4
    bob_secret = 9
    alice_pub = multip_fastexp(x_9, y_9, alice_secret)
    bob_pub = multip_fastexp(x_9, y_9, bob_secret)
    alice_share = multip_fastexp(*bob_pub, alice_secret)
    bob_share = multip_fastexp(*alice_pub, bob_secret)
    assert alice_share == bob_share
    print(alice_share)


if __name__ == "__main__":
    main()


def test():
    expected = 0x20D342D51873F1B7D9750C687D1571148F3F5CED1E350B5C5CAE469CDD684EFB
    xf, y = multip_fastexp(x_9, y_9, 2)
    x, y = multip_naive(x_9, y_9, 2)
    assert xf == expected == x

    expected = 0x1C12BC1A6D57ABE645534D91C21BBA64F8824E67621C0859C00A03AFFB713C12
    xf, y = multip_fastexp(x_9, y_9, 3)
    x, y = multip_naive(x_9, y_9, 3)
    assert xf == expected == x

    expected = 0x79CE98B7E0689D7DE7D1D074A15B315FFE1805DFCD5D2A230FEE85E4550013EF
    xf, y = multip_fastexp(x_9, y_9, 4)
    x, y = multip_naive(x_9, y_9, 4)
    assert xf == expected == x

    expected = 0x41B6EC3C50EE7AF203C0026E5E079E7FA8CBC9BC581D49CB0D537D5778497C87
    xf, y = multip_fastexp(x_9, y_9, 5)
    x, y = multip_naive(x_9, y_9, 5)
    assert xf == expected == x
