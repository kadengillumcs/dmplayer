from track import Track
from library import Library


def test_add_track():
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)

    library = Library()
    library.add_track(cobra)
    library.add_track(selfless)

    assert cobra.track_id == 1
    assert selfless.track_id == 2

def test_get_track():
    cobra = Track("Geese", "Cobra", 181, 1)

    library = Library()
    library.add_track(cobra)

    assert library.get_track(1).artist == cobra.artist
    assert library.get_track(2) is None

def test_get_all_tracks():
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    pardon_me = Track("Incubus", "Pardon Me", 221)

    library = Library()
    library.add_track(cobra)
    library.add_track(selfless)
    library.add_track(pardon_me)

    all_tracks = library.get_all_tracks()

    assert isinstance(all_tracks, list)
    assert len(all_tracks) == 3
    assert cobra in all_tracks
    assert selfless in all_tracks
    assert pardon_me in all_tracks

def test_remove_track():
    cobra = Track("Geese", "Cobra", 181)

    library = Library()
    library.add_track(cobra)

    removed_track = library.remove_track(1)

    assert library.remove_track(2) is None
    assert removed_track is cobra
    assert library.remove_track(1) is None

    selfless = Track("The Strokes", "Selfless", 218)
    library.add_track(selfless)

    assert selfless.track_id == 2
