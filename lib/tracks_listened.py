class TracksListened():

    def __init__(self):
        #Initialise empty list that will hold tracks listened
        #Return - no return
        self.tracks_list = []
        

    def add_tracks(self, track):
        #Parameters:
        #input string
        # task: add tracks listened into a list of tracks
        #Return: No return
        if track == "" or type(track) != str:
            raise Exception("No track provided or wrong data type")
        elif track not in self.tracks_list:
            self.tracks_list.append(track)

    #Returning formatted string of tracks
    def formatting_tracks_list(self):
        seperator = ', '
        formatted_tracks_list = seperator.join(self.tracks_list)
        return formatted_tracks_list

    def list_tracks(self):
        #Parameters:
        #task: List all tracks in a list of listened tracks
        #Returns: List of all listened tracks - list of strings "So far, you've listened to these tracks: [....]"
        return f"So far, you've listened to these tracks: {self.formatting_tracks_list()}"

tracks_listened = TracksListened()
tracks_listened.add_tracks("Stairway to heaven")
print(tracks_listened.list_tracks() )

