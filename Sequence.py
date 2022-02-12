class Sequence:

    def __init__(self):
        self._ele = []

    def __str__(self):
        return str(self._ele)

    def insert(self, val):
        self._ele.append(val)

    def get_value(self, pos):
        return self._ele[pos]

    def is_in(self, val):
        return val in self._ele
