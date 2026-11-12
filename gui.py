import tkinter as tk


class DMPlayerApp(tk.Tk):
    """
    Main application window for the DMPlayer.
    """
    def __init__(self):
        """
        Initialize GUI window
        """
        super().__init__()

        self.title("DMPlayer")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        """
        Create the main frames and buttons for the application.
        """
        # Top frame for add, remove, and sort tracks buttons
        self.top_nav = tk.Frame(self, bg="#2c3e50", height=50)
        self.top_nav.pack(side="top", fill="x")

        add_track_btn = tk.Button(self.top_nav, text="Add Track")
        add_track_btn.pack(side="left", padx=5, pady=5)

        remove_track_btn = tk.Button(self.top_nav, text="Remove Track")
        remove_track_btn.pack(side="left", padx=5, pady=5)

        sort_tracks_btn = tk.Button(self.top_nav, text="Sort Tracks")
        sort_tracks_btn.pack(side="right", padx=5, pady=5)

        # Bottom frame for the playback history navigation,
        # now playing track, and Add To Deck and On Deck buttons.
        self.bottom_nav = tk.Frame(self, bg="#2c3e50", height=50)
        self.bottom_nav.pack(side="bottom", fill="x")

        self.audio_nav_frame = tk.Frame(self.bottom_nav, bg="#34495e")
        self.audio_nav_frame.pack(side="top", fill="x")

        audio_back_btn = tk.Button(self.audio_nav_frame, text="<<")
        audio_back_btn.pack(side="left", padx=5, pady=5)

        audio_forward_btn = tk.Button(self.audio_nav_frame, text=">>")
        audio_forward_btn.pack(side="right", padx=5, pady=5)

        self.now_playing_label = tk.Label(self.audio_nav_frame, text="Now Playing: None")
        self.now_playing_label.pack(padx=5, pady=5)

        add_to_deck_btn = tk.Button(self.bottom_nav, text="Add To Deck")
        add_to_deck_btn.pack(side="left", padx=5, pady=5)

        on_deck_btn = tk.Button(self.bottom_nav, text="On Deck")
        on_deck_btn.pack(side="right", padx=5, pady=5)

        # Library frame for displaying the list of tracks in the library.
        self.library_frame = tk.Frame(self, bg="#619682")
        self.library_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = DMPlayerApp()
    app.mainloop()
