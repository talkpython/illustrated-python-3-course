def test_bytes1():
    # Write a function, ``put_bytes``, that
    # takes a filename and bytes and
    # writes it to disk
    # ***********************************

    assert put_bytes.__name__ == 'put_bytes'


def test_bytes2(tmpdir):
    # Write a function, ``get_bytes``, that
    # takes a filename, and returns the bytes in it
    # ***********************************
    unknown = b'\xf0\x9f\x90\x8d makes your head \xe1\xb4\x8eI\xd4\x80S'

    fname = tmpdir.join('out.txt')
    put_bytes(fname, unknown)
    content = get_bytes(fname)
    assert content == unknown


def test_encoding1():
    # Write a function, ``put_unicode``, that
    # takes a filename, a Unicode string, and
    # an encoding. It uses that encoding
    # to write the string to disk
    # ***********************************

    assert put_unicode.__name__ == 'put_unicode'


def test_encoding(tmpdir):
    # Write a function, ``get_unicode``, that
    # takes a filename and an encoding, and returns
    # a Unicode string with the contents of the file
    # ***********************************
    txt = "十五歲上娶了太史方定隆小姐為妻，十六歲便生一位男子。是五月端午日生的，因天"

    fname = tmpdir.join('out2.txt')
    put_unicode(fname, txt, 'big5')
    content = get_unicode(fname, 'big5')
    assert content == txt
    txt_bytes = get_bytes(fname)
    assert txt_bytes[-5:] == b'A\xa6]\xa4\xd1'


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])
