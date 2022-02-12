import Set


class MultiSet(Set.Set):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def insert(self, val):
        multiset_elements = self._ele
        val_position = None

        # Check whether it is the first occurrence of the value
        evaluation_first = True
        i = 0
        while evaluation_first and i < len(multiset_elements):
            if val == multiset_elements[i][0]:
                evaluation_first = False
                val_position = i
            i += 1

        if evaluation_first:
            super().insert((val, 1))
        else:
            # Update the number of occurrences of the value
            count_val = multiset_elements[val_position][1] + 1

            # Insert the Updated Tuple
            super().insert((val, count_val))

            # Remove Out-Dated Tuple
            self._ele.remove((val, count_val - 1))

    def is_in(self, val):
        multiset_elements = self._ele

        # Check whether the value exists in a tuple
        bool_is_in = False
        i = 0
        while not bool_is_in and i < len(multiset_elements):
            if val == multiset_elements[i][0]:
                bool_is_in = True
            i += 1
        return bool_is_in

    def get_value(self, pos):
        return super(Set.Set, self).get_value(pos)[0]
