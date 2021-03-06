# by Kami Bigdely
# Replace nested conditional with gaurd clauses
import pytest
import math


def extract_position(line):
    if not line:
        pos = None
    else:
        if 'debug' in line or 'error' in line:
            pos = None
        else:
            if 'x:' in line:
                start_index = line.find('x:') + 2
                pos = line[start_index:]  # from start_index to the end.
            else:
                pos = None
    return pos


if __name__ == "__main__":
    result1 = extract_position(
        '|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position(
        '|update| the positron location in the particle accelerator is x:21.432')
    print(result2)


def test_extract_position():
    assert extract_position(
        '|error| numerical calculations could not converge.') == None

    assert extract_position(
        '|debug| numerical calculations could not converge.') == None

    assert extract_position(
        '|update| the positron location in the particle accelerator is x:21.432') == "21.432"

    assert extract_position(
        '|update| the positron location in the particle accelerator is x:43.283') == "43.283"

    assert extract_position(
        '|update| the positron location in the particle accelerator is x:175.319') == "175.319"
