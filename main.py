import MultiSet

if __name__ == "__main__":
    print("test")
    print()

    # IMPLEMENTATION EXAMPLES
    my_object = MultiSet.MultiSet()
    my_object.insert(83)
    print(my_object)
    print()

    my_object.insert(83)
    my_object.insert(83)
    my_object.insert(83)
    my_object.insert(94)
    my_object.insert(56)
    my_object.insert(666)
    print(my_object)
    my_object.insert(56)
    print(my_object)
    print()

    print(my_object.is_in(83))
    print(my_object.is_in(2))
    print()

    print(my_object.get_value(0))
