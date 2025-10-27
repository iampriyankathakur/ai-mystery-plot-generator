import random

def generate_title(character, setting):
    templates = [
        "Shadows of {setting}",
        "The {character}'s Secret",
        "Echoes in {setting}",
        "The Case of the Lost Truth",
        "Murder in {setting}"
    ]
    title = random.choice(templates).format(
        character=character.title(), setting=setting.title()
    )
    return title
