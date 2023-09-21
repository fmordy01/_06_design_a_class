{{PROBLEM}} Class Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

<!-- As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them. -->

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class TracksListened():

    def __init__(self)
        #Initialise empty list that will hold tracks listened
        #Return - no return
        pass

    def add_tracks(self, track):
        #Parameters:
        #input string
        # task: add tracks listened into a list of tracks
        #Return: No return
        pass

    def list_tracks(self):
        #Parameters:
        #task: List all tracks in a list of listened tracks
        #Returns: List of all listened tracks - list of strings "So far, you've listened to these tracks: [....]"


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

"""
Given no tracks - emptry string or given a data type other than a string
Will raise an ERROR - "no track provided"
"""
def test_no_track_provided_error:
    tracks_listened = TracksListened()
    tracks.listened.add("") => "no track provided or wrong data type"


"""
Given 1 track - Stairway to heaven
will return a list of 1 track in a string message
"""
    tracks_listened = TracksListened()
    tracks_listened.add("Stairway to heaven")
    tracks_listened.list_tracks() # => "So far, you've listened to these tracks: [Stairway to heaven]"


"""
Given 3 track - Stairway to heaven, Here comes the sun, Nothing else matters
will return a list of 3 track in a string message
"""
    tracks_listened = TracksListened()
    tracks_listened.add("Stairway to heaven")
    tracks_listened.list_tracks() 

    tracks_listened = TracksListened()
    tracks_listened.add("Stairway to heaven")
    tracks_listened.add("Here comes the sun")
    tracks_listened.add("Nothing else matters")
    tracks_listened.list_tracks() # => "So far, you've listened to these tracks: [Stairway to heaven, Here comes the sun, Nothing else matters]"
    




    



4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

