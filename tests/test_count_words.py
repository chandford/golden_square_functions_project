from lib.count_words import count_words

def test_count_words_returns_int():
    # Arrange, act, assert
    result = count_words("string")
    assert type(result) == int

def test_single_word_string():
    result = count_words("string")
    assert result == 1

def test_count_words_returns_correct_length_no_punctuation():
    result = count_words("Test string")
    assert result == 2
    result = count_words("Extended test string to be tested")
    assert result == 6

def test_count_words_returns_correct_length_with_punctuation():
    result = count_words("A - funky - test - string")
    assert result == 4
    result = count_words("! Will $ this... bamboozle the function?!")
    assert result == 5
