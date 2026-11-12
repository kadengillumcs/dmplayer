from track import Track
from datetime import date

def test_new_track():
    cobra = Track("Geese", "Cobra", 181)

    assert cobra.artist == "Geese"
    assert cobra.title == "Cobra"
    assert cobra.duration == 181
    assert cobra.track_id is None
    assert cobra.date_added == date.today()
    assert cobra.play_count == 0

def test_saved_track():
    cobra = Track("Geese", "Cobra", 181, track_id=1, date_added=date(2026, 11, 10), play_count=12)

    assert cobra.artist == "Geese"
    assert cobra.title == "Cobra"
    assert cobra.duration == 181
    assert cobra.track_id == 1
    assert cobra.date_added == date(2026, 11, 10)
    assert cobra.play_count == 12