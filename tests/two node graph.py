import JINTFP as fp


class Adder(fp.NodeBody):
    in0 = fp.Input(def_val=0)
    in1 = fp.Input(def_val=0)
    out0 = fp.Output()

    def __init__(self, a, b):
        super().__init__(a, b)

    def calculate(self, a, b):
        return a + b


node0 = Adder(10, 20)
node1 = Adder(20, 50)
node1.in0 = node0.out0

print(node0.out0)
print(node1.out0)
