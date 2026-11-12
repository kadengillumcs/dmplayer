class Library:
    """
    Stores Tracks in a dictionary using the track ID as the key.
    """
    def __init__(self):
        """
        Initializes the first track ID to 1 and an empty tracks dictionary.
        """
        self.next_id = 1
        self.tracks = {}

    def add_track(self, track):
        """
        Assigns next ID to track ID and adds the track to the
        tracks dict with the next ID as the key and the Track as the value.
        Next ID is incremented once after track is added to library so the next
        track gets a unique ID.
        """
        track.track_id = self.next_id
        self.tracks[self.next_id] = track

        self.next_id += 1

    def get_track(self, track_id):
        """
        Returns a Track if the ID exists and None if not.
        """
        return self.tracks.get(track_id, None)

    def get_all_tracks(self):
        """
        Returns all Tracks in the library as a list.
        """
        tracks_list = list(self.tracks.values())
        return tracks_list

    def remove_track(self, track_id):
        """
        Removes a Track by ID from library.
        Returns removed Track or None if ID doesn't exist.
        """
        removed_track = self.tracks.pop(track_id, None)

        return removed_track
