from seeds import get_random_seeds
from title_generator import generate_title
from plot_builder import build_plot

if __name__ == "__main__":
    character, setting, twist = get_random_seeds()
    title = generate_title(character, setting)
    synopsis, scenes = build_plot(character, setting, twist)

    print(f"🕵️ Title: {title}\n")
    print(f"📖 Synopsis: {synopsis}\n")
    print("🎬 Key Scenes:")
    for scene in scenes:
        print(scene)

    with open("data/sample_outputs.txt", "a") as f:
        f.write(f"{title}\n{synopsis}\n\n")
