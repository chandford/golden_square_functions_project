from lib.diary import make_snippet

def test_make_snippet_returns_string():
    # Arrange, act, assert 
    result = make_snippet("")
    assert result == ""
    result = make_snippet("Hello")
    assert type(result) == str

def test_make_snippet_returns_string_under_five_words():
    result = make_snippet("Hello there you")
    assert result == "Hello there you"
    result = make_snippet("Let's have another example")
    assert result == "Let's have another example"

def test_make_snippet_snips_string_over_five_words():
    result = make_snippet("Hello to my dear code reader")
    assert result == "Hello to my dear code..."
    result = make_snippet("Let's have another example to demonstrate")
    assert result == "Let's have another example to..."

def test_make_snippet_with_punctuation(): 
    result = make_snippet("Well, hello to you, my dear code reader!")
    assert result == "Well, hello to you, my..."
    result = make_snippet("Oh. My. God. Is this really working?!")
    assert result == "Oh. My. God. Is this..."

# Checked with coverage, 100%! 