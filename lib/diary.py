# Function takes a string as an argument 
# and returns the first five words
# and then a '...' if there are more than that.

def make_snippet(str):
    str_list = str.split()
    if len (str_list) <= 5:
        return str
    else:
        snipped_str = " ".join(str_list[0:5])
        snippet = snipped_str + "..."
        return snippet