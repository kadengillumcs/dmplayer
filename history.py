class Node:
    def __init__(self, track):
        self.track = track
        self.next = None
        self.prev = None

class TrackHistory:
    def __init__(self):
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
