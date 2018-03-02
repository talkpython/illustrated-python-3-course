

def test_mario():
    """
   ======= ====== ====== ===== =====================
   Name    Mario  Luigi  Toad  Princess Toadstool
   ======= ====== ====== ===== =====================
   Speed   4      3      5     2
   Jump    4      5      2     3
   Power   4      3      5     2
   ======= ====== ====== ===== =====================
    """
    # The table above lists Super Mario Skills
    # Create a base class, ``Character``,
    # that has speed, jump, and power methods.
    # They should each return 2.
    # Create subclasses for Mario and Luigi
    # that use ``super()`` to call the parent
    # class method, and increment the value
    # by the appropriate amount before returning
    # it.
    # Put this function in a module called py3code.py
    # ***********************************


    from py3code import Character, Luigi, Mario
    m = Mario()
    sp = m.speed()
    assert Character in Mario.__bases__
    assert sp == 4
    def speed(self):
        return 5
    Character.speed = speed
    assert m.speed() == 7
    assert Luigi().speed() == 6


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
