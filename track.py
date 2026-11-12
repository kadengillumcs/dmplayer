from datetime import date


class Track:
    """
    Stores data for a track's artist, title,
    duration in seconds, date added, and play count.
    """
    def __init__(self, artist, title, duration, date_added=None, play_count=0):
        """
        Date added and play count are optional because if
        they are not passed in it means they are new additions.
        If data is passed in for date added and play count that
        means they have been loaded from saved data.
        """
        self.artist = artist
        self.title = title
        self.duration = duration
        
        if date_added is None:
            self.date_added = date.today()
        else:
            self.date_added = date_added
        
        self.play_count = play_count
