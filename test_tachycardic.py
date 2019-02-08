import pytest


@pytest.mark.parametrize("input, expected", [
                                ('tachycardic', True),
                                ('TACHYCARDIC', True),
                                ('Tachycardic', True),
                                ('TachYcArdiC', True),
                                ('.. tachycardic . .', True),
                                ('nottachy', False),
                                ('tachy cardic', False)])
def test_correct_spelling(input, expected):
    from tachycardia import is_tachycardic
    outcome = is_tachycardic(input)
    assert outcome == expected
