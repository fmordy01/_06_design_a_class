import pytest
from lib.tracks_listened import TracksListened

"""
Given no tracks - emptry string or given a data type other than a string
Will raise an ERROR - "no track provided"
"""
def test_no_track_provided_error():
    tracks_listened = TracksListened()
    with pytest.raises(Exception) as err:
        tracks_listened.add_tracks("")  
    assert str(err.value) == "No track provided or wrong data type"

def test_wrong_data_type_provided_error():
    tracks_listened = TracksListened()
    with pytest.raises(Exception) as err:
        tracks_listened.add_tracks(1230)  
    assert str(err.value) == "No track provided or wrong data type"




"""
Given 1 track - Stairway to heaven
will return a list of 1 track in a string message
"""
def test_given_one_track_list_it():
    tracks_listened = TracksListened()
    tracks_listened.add_tracks("Stairway to heaven")
    result = tracks_listened.list_tracks() 
    assert result == "So far, you've listened to these tracks: Stairway to heaven"


"""
Given 3 track - Stairway to heaven, Here comes the sun, Nothing else matters
will return a list of 3 track in a string message
"""
def test_add_three_tracks_list_them():
    tracks_listened = TracksListened()
    tracks_listened.add_tracks("Stairway to heaven")
    tracks_listened.add_tracks("Here comes the sun")
    tracks_listened.add_tracks("Nothing else matters")
    result = tracks_listened.list_tracks() 
    assert result == "So far, you've listened to these tracks: Stairway to heaven, Here comes the sun, Nothing else matters"

"""
Given 2 of the same track - Stairway to heaven
will return a list of 1 track in a string message as it is repeated
"""
def test_add_two_same_tracks_list_one():
    tracks_listened = TracksListened()
    tracks_listened.add_tracks("Stairway to heaven")
    tracks_listened.add_tracks("Stairway to heaven")
    result = tracks_listened.list_tracks() 
    assert result == "So far, you've listened to these tracks: Stairway to heaven"