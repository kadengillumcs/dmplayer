class Node:
    def __init__(self, track):
        """
        Initializes a Node with a track and pointers to the next and previous nodes.
        """
        self.track = track
        self.next = None
        self.prev = None

class TrackHistory:
    def __init__(self):
        """
        Initializes an empty TrackHistory with head, tail, and current pointers, and a size counter.
        """
        self.current = None
        self.head = None
        self.tail = None
        self.size = 0

    def add_cur_track(self, track):
        """
        Adds a new track to the end of the history.
        """
        new_node = Node(track)
        if self.tail is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

        self.tail = new_node
        self.current = new_node
        self.size += 1

    def prev_track(self):
        """
        Moves the current pointer to the previous track in the history.
        Returns the previous track or None if there is no previous track.
        """
        if self.current is None:
            return None
        if self.current.prev is None:
            return None

        self.current = self.current.prev
        return self.current.track


    def next_track(self):
        """
        Moves the current pointer to the next track in the history.
        Returns the next track or None if there is no next track.
        """
        if self.current is None:
            return None
        if self.current.next is None:
            return None

        self.current = self.current.next
        return self.current.track

    def get_current_track(self):
        """
        Returns the current track in the history or None if there is no current track.
        """
        if self.current is None:
            return None
        return self.current.track
