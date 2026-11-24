from history import TrackHistory
from track import Track


def test_add_to_empty_history():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    history.add_cur_track(cobra)

    assert history.size == 1
    assert history.head.track == cobra
    assert history.tail.track == cobra
    assert history.current.track == cobra
    assert history.head.next is None
    assert history.tail.prev is None

def test_add_to_non_empty_history():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    history.add_cur_track(cobra)
    history.add_cur_track(selfless)

    assert history.size == 2
    assert history.head.track == cobra
    assert history.tail.track == selfless
    assert history.current.track == selfless
    assert history.head.next.track == selfless
    assert history.tail.prev.track == cobra

def test_empty_history_prev_next():
    history = TrackHistory()

    assert history.prev_track() is None
    assert history.next_track() is None
    assert history.get_current_track() is None

def test_prev_track_at_head():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    history.add_cur_track(cobra)

    assert history.prev_track() is None
    assert history.current.track == cobra

def test_prev_track():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    history.add_cur_track(cobra)
    history.add_cur_track(selfless)

    prev_track = history.prev_track()

    assert prev_track == cobra
    assert history.current.track == cobra

def test_next_track_at_tail():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    history.add_cur_track(cobra)

    assert history.next_track() is None
    assert history.current.track == cobra

def test_next_track():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    history.add_cur_track(cobra)
    history.add_cur_track(selfless)

    history.prev_track() # go to cobra to get next track to be selfless
    next_track = history.next_track()

    assert next_track == selfless
    assert history.current.track == selfless

def test_get_current_track():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    history.add_cur_track(cobra)
    history.add_cur_track(selfless)

    assert history.get_current_track() == selfless

    history.prev_track()
    assert history.get_current_track() == cobra

    history.next_track()
    assert history.get_current_track() == selfless

def test_history_log():
    history = TrackHistory()
    cobra = Track("Geese", "Cobra", 181)
    selfless = Track("The Strokes", "Selfless", 218)
    history.add_cur_track(cobra)
    history.add_cur_track(selfless)

    history.prev_track()
    pardon_me = Track("Incubus", "Pardon Me", 221)
    history.add_cur_track(pardon_me)

    assert history.tail.prev.track == selfless
    assert history.tail.track == pardon_me
    assert history.current.track == pardon_me
    assert history.size == 3