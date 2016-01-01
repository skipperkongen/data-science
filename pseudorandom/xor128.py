MAX = 2**64

class Xor128Plus(object):
    """docstring for Xor128Plus"""
    def __init__(self):
        super(Xor128Plus, self).__init__()
        self.state0 = 1
        self.state1 = 2
        for i in range(10000):
            self.next()

    def next(self):
        s1 = self.state0
        s0 = self.state1
        self.state0 = s0 % MAX
        s1 ^= (s1 << 23) % MAX
        s1 ^= (s1 >> 17) % MAX
        s1 ^= s0 % MAX
        s1 ^= (s0 >> 26) % MAX
        self.state1 = s1 % MAX
        return self.state1 % MAX

xor = Xor128Plus()
for i in range(10000):
    print xor.next()
    