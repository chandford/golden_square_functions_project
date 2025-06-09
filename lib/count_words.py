# Function that takes a string as an argument
# and returns the number of words in that string.
def count_words(str):
    str_list = str.split()
    print(str_list)
    word_list = [i for i in str_list if i[0].isalpha()]
    print(word_list)
    return len(word_list)