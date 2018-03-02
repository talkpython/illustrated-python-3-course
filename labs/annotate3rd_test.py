from pathlib import Path

def test_ann3rd():
    """
    0. Copy py3code.pyORIG to py3mt.py and py3pa.py
    1. Install MonkeyType
    2. Create a function ``test_mt`` that exercises py3mt.py
       in a file ``runmt.py``::

      force(mass=10, acceleration=9.8)
      quad(a=1, b=2, c=1)
      Mario().speed()
    
    3. Create a stub for py3mt.py in py3mt.pyi
    4. Run mypy against py3mt.py

    5. Install PyAnnotate
    6. Create a function ``test_pa`` that exercises py3pa.py
       and sticks the json output into ``type_info.json``
    7. Use pyannotate to update py3pa.py
    8. Run mypy against py3pa.py
    
    """
    p = Path('py3code.pyi')
    assert p.exists()
    p = Path('py3code.type_info.json')
    assert p.exists()

    
if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
