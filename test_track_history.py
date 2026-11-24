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