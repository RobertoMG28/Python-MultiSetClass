import Sequence


class Set(Sequence.Sequence):

    def __init__(self):
        super().__init__()

    def insert(self, val):
        if not self.is_in(val):
            super(Set, self).insert(val)

    def __str__(self):
        return super().__str__()
