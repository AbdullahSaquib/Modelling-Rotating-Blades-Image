import math as m
from conversions import deg_to_rad


class Blade(object):

    ts = 0.1

    def __init__(self, pi, w, omg):
        self.pi = pi
        self.w = w
        self.omg = omg
        self.pf = pi + omg * Blade.ts

    def tc(self, p):
        # self.pf = self.pi + self.omg * Blade.ts
        if self.pf >= self.w:
            if self.pi <= p <= self.pi + self.w:
                tc = (p - self.pi) / self.omg
            elif self.pi + self.w < p < self.pf:
                tc = self.w/self.omg
            elif self.pf <= p <= self.pf + self.w:
                tc = (self.pf + self.w - p) / self.omg
            else:
                tc = 0
        elif self.pf < self.w:
            if self.pi <= p <= self.pf:
                tc = (p - self.pi) / self.omg
            elif self.pf < p < self.pi + self.w:
                tc = Blade.ts
            elif self.pi + self.w <= p <= self.pf + self.w:
                tc = (self.pf + self.w - p) / self.omg
            else:
                tc = 0

        if tc < Blade.ts:
            return tc
        else:
            return Blade.ts

    def Pc(self, p):
        return self.tc(p)/Blade.ts

    def tr(self, p):
        nf = (self.pf + self.w)//(2*m.pi) + 1
        self.nf = nf  #
        tmp = 0
        if 0 <= p < 2*m.pi:
            for i in range(0, int(nf + 1)):
                tmp += self.tc(p + 2*i*m.pi)
            return tmp
        else:
            raise ValueError('phi is out of range.')

    def Pr(self, p):
        return self.tr(p)/Blade.ts

    @classmethod
    def set_ts(cls, ts):
        cls.ts = ts


# w = deg_to_rad(10)
# omg = deg_to_rad(2 * 360)
#
# b1 = Blade(m.pi/2, w, omg)
# b2 = Blade(3*m.pi/2, w, omg)
#
# for i in range(0, 360, 1):
#     p = deg_to_rad(i)
#     print(i, b1.Pr(p) + b2.Pr(p))
