import random

characters = [
    "retired detective", "AI journalist", "art thief", 
    "librarian with a secret", "forensic psychologist"
]

settings = [
    "foggy London", "abandoned space station", "sleepy coastal town",
    "underground cyberpunk city", "isolated mountain village"
]

twists = [
    "the killer is not human", "time loops every midnight",
    "everyone in town is lying", "the victim faked their death",
    "the AI system planned it all"
]

def get_random_seeds():
    return random.choice(characters), random.choice(settings), random.choice(twists)
