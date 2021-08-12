"""A video player class."""
# I have relatively basic knowledge of python - first couple of commands were done with help, slowly figured out the others.
# I managed to get to the end of part 1
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.video_library = VideoLibrary()
        self.video_playing = False
        self.video_paused = True
        self.video_name = None

    def number_of_videos(self):
        num_videos = len(self.video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        # get_all_videos command taken from video_library
        all_videos = self.video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_vid_list = []

        for vid in all_videos:
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            # List videos for sorting
            temp_vid_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort list alphabetically and display
        sorted_vid_list = sorted(temp_vid_list)
        for a in sorted_vid_list:
            print(a)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        # get_video(video_id) taken from video_library
        now_playing = self.video_library.get_video(video_id)
        # try function - using the self parameters from line 9+
        try:
            if self.video_playing is True:
                if not now_playing:
                    print("Cannot play video: Video does not exist")
                else:
                    print(f"Stopping video: {self.video_name}")
                    print(f"Playing video: {now_playing.title}")
                    self.video_name = now_playing.title
                    self.video_paused = False

            else:
                print(f"Playing video: {now_playing.title}")
                self.video_playing = True
                self.video_paused = False
                self.video_name = now_playing.title

        except:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""

        if self.video_playing is True:
            print(f"Stopping video: {self.video_name}")
            self.video_playing = False
            self.video_paused = True
            self.video_name = None

        elif self.video_playing is False:
            print("Cannot stop video: No video is currently playing")
            self.video_paused = True


    def play_random_video(self):
        """Plays a random video from the video library."""
        import random
        rand_vid = random.choice(self.video_library.get_all_videos())
        if self.video_playing is True:
            print(f"Stopping video: {self.video_name}")
            print(f"Playing video: {rand_vid.title}")
            self.video_paused = False
            self.video_name = rand_vid.title

        elif self.video_playing is False:
            print(f"Playing video: {rand_vid.title}")
            self.video_playing = True
            self.video_paused = False
            self.video_name = rand_vid.title

    def pause_video(self):
        """Pauses the current video."""
        if self.video_playing is False:
            print("Cannot pause video: No video is currently playing")
            self.video_name = None

        elif self.video_paused is True:
            print(f"Video already paused: {self.video_name}")
            self.video_playing = False

        else:
            print(f"Pausing video: {self.video_name}")
            self.video_name = self.video_name
            self.video_paused = True


    def continue_video(self):
        """Resumes playing the current video."""
        if self.video_name is None:
            print("Cannot continue video: No video is currently playing")

        # these two elif statements work separately #
        else:
            if self.video_paused is True:
                print(f"Continuing video: {self.video_name}")
                self.video_playing = True
                self.video_paused = False

            elif self.video_paused is False:
                print("Cannot continue video: Video is not paused")
        # try to find a way to make them work :) #




    def show_playing(self):
        """Displays video currently playing."""

        playing_videos = self.video_library.get_all_videos()
        for vid in playing_videos:
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"
        if self.video_playing is True:
            print(f"Currently playing: {vid.title} ({vid.video_id}) {tags}")

        else:
            print("Nothing is currently playing")

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")