import pluggy

hookspec = pluggy.HookspecMarker("texteditorapplication")

@hookspec
def eggsample_add_ingredients(ingredients: tuple):
    """Have a look at the ingredients and offer your own
    
    :param ingredients: the ingredients
    :return: a list of ingredients
    """

@hookspec
def eggsample_prep_condiments(condiments: dict):
    """Reorganize the condiments tray to your heart's content
    
    :param condiments: some souces and stuff
    :return: a witty comment about your activity
    """
