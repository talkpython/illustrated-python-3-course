def test_1():
    # The following is a line from
    # Yu Lou Chun by Dao Ren Bai Yun
    # https://www.gutenberg.org/files/25422/25422-0.txt
    # Convert the line to UTF-8 bytes
    # stored in the variable ``utf8_txt``
    # ***********************************
    txt = "十五歲上娶了太史方定隆小姐為妻，十六歲便生一位男子。是五月端午日生的，因天"

    assert len(utf8_txt) == 111
    assert utf8_txt[-5:] == b'\x9b\xa0\xe5\xa4\xa9'


def test_2():
    # The following is a line from
    # Yu Lou Chun by Dao Ren Bai Yun
    # https://www.gutenberg.org/files/25422/25422-0.txt
    # Convert the line to big5 (another Chinese encoding) bytes
    # stored in the variable ``big5_txt``
    #
    # Is big5 more compact than UTF-8?
    # ***********************************
    txt = "十五歲上娶了太史方定隆小姐為妻，十六歲便生一位男子。是五月端午日生的，因天"

    assert len(big5_txt) == 74
    assert big5_txt[-5:] == b'A\xa6]\xa4\xd1'


def test_3():
    # The following is UTF-8 bytes
    # Decode it into a variable, ``result``
    # ***********************************
    unknown = b'\xf0\x9f\x90\x8d makes your head \xe1\xb4\x8eI\xd4\x80S'

    assert len(result) == 22


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
