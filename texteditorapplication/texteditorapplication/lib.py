import texteditorapplication

@texteditorapplication.hookimpl
def eggsample_add_ingredients():
    spices = ["salt", "pepper"]
    eggs = ["egg", "egg"]
    ingredients = spices + eggs
    return ingredients

@texteditorapplication.hookimpl
def eggsample_prep_condiments(condiments):
    condiments["mint sauce"] = 1