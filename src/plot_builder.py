def build_plot(character, setting, twist):
    synopsis = (
        f"In {setting}, a {character} faces their most perplexing case yet. "
        f"As clues unfold, dark truths emerge — until it's revealed that {twist}."
    )

    key_scenes = [
        f"1️⃣ The discovery of a mysterious clue in {setting}.",
        f"2️⃣ The {character} begins connecting the dots.",
        f"3️⃣ Secrets unravel as danger closes in.",
        f"4️⃣ The shocking revelation: {twist}.",
        f"5️⃣ Aftermath leaves the {character} forever changed."
    ]

    return synopsis, key_scenes
