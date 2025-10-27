from src.plot_builder import build_plot

def test_build_plot():
    synopsis, scenes = build_plot("detective", "city", "killer was a robot")
    assert "detective" in synopsis
    assert len(scenes) == 5
