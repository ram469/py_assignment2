# Python is Easy Assignment 1

# Name of the song
SongName = "Our God"

# Singer name
Singer = "Chris Tomlin"

# Album name
Album = "If our God is for us"

# Genre of the song
Genre = "Worship"

# Releasing date
DateReleased = 2010

# Track length
Length = 285

# Lyric writers
LyricWriters = "Chris Tomlin, Jesse Reeves, Ed Cash, Jonas Myrin"


# Return artist name
def artist():
    return "Chris Tomlin"


# Return genre
def genre():
    return "Worship"


# Return date released
def year():
    return 2010


# Check whether the album is older or newer deciding by year 2010
def is_album_older(yr):
    if yr >= 2010:
        True


# Print extra statements about the track, writing to use boolean in the data type in the code
if is_album_older(year()):
    print("New Album")
else:
    print("Old album")


print("Song Name: ", SongName)
print("Track Length: ", Length, "Sec")
print("Lyrics Writers: ", LyricWriters)
print("Album Name:", Album)

# Print track details using functions
print("Artist: ", artist())
print("Genre: ", genre())
print("Release Date: ", year())