import texteditorapplication

@texteditorapplication.hookimpl
def count_characters(text):
    character_count = len(text)
    print("omgg: ", character_count)
    return character_count