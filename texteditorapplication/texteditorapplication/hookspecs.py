import pluggy

hookspec = pluggy.HookspecMarker("texteditorapplication")

@hookspec
def count_characters(text):
    """Counts the characters of the text
    
    :param text: data text from the file
    :return: an integer value representing the number of characters
    """