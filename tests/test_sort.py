from library import Library
from sort_library import merge_sort
from track import Track


def test_sort_empty_library():
    library = Library()

    sorted_tracks = merge_sort(library.get_all_tracks(), key=lambda track: track.artist)

    assert sorted_tracks == []

def test_sort_one_track():
    library = Library()
    cobra = Track("Geese", "Cobra", 181)

    library.add_track(cobra)

    sorted_tracks = merge_sort(library.get_all_tracks(), key=lambda track: track.artist)

    assert sorted_tracks == [cobra]

def test_sort_by_artist():
    library = Library()
    cobra = Track("geese", "Cobra", 181)
    selfless = Track("The strokes", "Selfless", 218)
    pardon_me = Track("Incubus", "Pardon Me", 221)

    library.add_track(cobra)
    library.add_track(selfless)
    library.add_track(pardon_me)

    sorted_tracks = merge_sort(library.get_all_tracks(), key=lambda track: track.artist.lower())

    assert sorted_tracks == [cobra, pardon_me, selfless]

def test_sort_by_duration():
    library = Library()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    pardon_me = Track("Incubus", "Pardon Me", 221)

    library.add_track(cobra)
    library.add_track(pardon_me)
    library.add_track(selfless)

    sorted_tracks = merge_sort(library.get_all_tracks(), key=lambda track: track.duration)

    assert sorted_tracks == [cobra, selfless, pardon_me]

def test_sort_with_same_artist():
    library = Library()
    cobra = Track("Geese", "Cobra", 181)
    taxes = Track("Geese", "Taxes", 197)
    pardon_me = Track("Incubus", "Pardon Me", 221)

    library.add_track(cobra)
    library.add_track(taxes)
    library.add_track(pardon_me)

    sorted_tracks = merge_sort(library.get_all_tracks(), key=lambda track: track.artist.lower())

    assert sorted_tracks == [cobra, taxes, pardon_me]