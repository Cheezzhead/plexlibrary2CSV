#import modules and dependencies
from plexapi.server import PlexServer
from plexapi.media import Media
import csv


#Your plex credentials
PLEX_URL = 'http://192.168.0.2:32400'
PLEX_TOKEN = 'mL5Y3ttWity3xv5gTJCR'
MOVIE_LIBRARIES = ['Test','Test2']

#Create plex server instance
plex = PlexServer(PLEX_URL, PLEX_TOKEN)

#Get list of movies in MOVIE_LIBRARIES
#ovies = []
movies = [plex.library.section(library).all() for library in MOVIE_LIBRARIES]
movie_list = []

#print(movies)
for library_list in movies:
	for movie in library_list:
		movie_list.append({"Title" : movie.title,
						   "Type" : movie.type,
						   "LastViewed" : movie.lastViewedAt
						   })



#print(movie_list)
print("\nLength of movie list is ",len(movie_list))

full_list = []
for plexlib in movies:
	for film in plexlib:
		full_list.append(film.media)

for i in range(len(movie_list)):
	for media in full_list[i]:
		movie_list[i].update({
			"Bitrate":media.bitrate, 
			"Container":media.container,
			"Duration(mins)":round((media.duration*0.00001666667))
			})


		
#print(full_list)
print(movie_list)





