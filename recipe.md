# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem
_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature
_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):
        """Provides estimate of reading time for a text

    Parameters: (list all parameters and their types)
        text: a string representing human-readable text

    Returns: (state the return value and its type)
       estimated reading time as a float
       (alternative: f-string including reading time and unit of measurement (minutes))

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
```

## 3. Create Examples as Tests
_Make a list of examples of what the function will take and return._

```python
# Given a text of 200 words
# It returns a reading time of 1

estimate_reading_time("...200...")
# => 1.0

# Given a text of 400 words
# It returns a reading time of 2

estimate_reading_time("...400...")
# => 2.0

# Given a text of 300 words
# It returns a reading time of 1.5

estimate_reading_time("...300...")
# => 1.5

# Given an empty string
# It throws an error

estimate_reading_time("")
# => Raises error: "Can't estimate reading time for an empty text"

```

_Encode each example as a test. You can add to the above list as you go._



## 4. Implement the Behaviour
_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python
# Given a text of 200 words
# It returns a reading time of 1

def test_with_two_hundred_words():
    result = estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten")
    assert result == 1.0

# Given a text of 400 words
# It returns a reading time of 2

def test_with_four_hundred_words():
    result = estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten")
    assert result == 2.0

# Given a text of 300 words
# It returns a reading time of 1.5

def test_with_three_hundred_words():
    result = estimate_reading_time("one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten one two three four five six seven eight nine ten")
    assert result == 1.5

# Given an empty string
# It throws an error

def test_with_empty_string():
    with pytest.raises(Exception) as err:
        estimate_reading_time(" ")
    error_message = str(err.value)
    assert error_message == "Can't estimate reading time for an empty text"
```