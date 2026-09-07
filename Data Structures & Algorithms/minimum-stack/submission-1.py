class MinStack:

    def __init__(self):
        self.a = []
        self.mim = []

    def push(self, val: int) -> None:
        self.a.append(val)

        if len(self.mim) == 0:
            self.mim.append(val)
        else:
            self.mim.append(min(val, self.mim[-1]))

    def pop(self) -> None:
        self.a.pop()
        self.mim.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.mim[-1]