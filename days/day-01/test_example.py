from days.day_01.example import sum_of_squares

def test_sum_of_squares_empty():
    assert sum_of_squares([]) == 0

def test_sum_of_squares_list():
    assert sum_of_squares([1, 2, 3]) == 14