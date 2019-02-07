import pytest


@pytest.mark.parametrize("input, expected", [
                                ('tachycardic', True),
                                ('TACHYCARDIC', True),
                                ('Tachycardic', True),
                                ('TachYcArdiC', True)])
def test_correct_spelling(input, expected):
    from tachycardia import is_tachycardic
    input = 'tachycardic'
    outcome = is_tachycardic(input)
    expected = True
    assert outcome == expected
