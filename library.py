from track import Track

class Library:
    def __init__(self):
        self.next_id = 1
        self.tracks = {}

    def add_track(self, track):
        track.track_id = self.next_id
        self.tracks[self.next_id] = track

        self.next_id += 1
