# Dictionary containing current movies and their showtimes
current_movies = {
    'Blue Lock': '11:00am',
    'Godzilla': '1:00pm',
    'Interstellar': '3:00pm',
    'Planet of the apes': '5:00pm'
}

# Print the list of currently showing movies
print('We are showing the following movies:\n')
for key in current_movies:
    print(key)

# Prompt the user to input the name of the movie they want the showtime for
movie = input('What movie would you like the showtime for?\n')

# Get the showtime for the selected movie
showtime = current_movies.get(movie)

# Check if the showtime is available and print the result
if showtime is None:
    print('Requested movie is not available')
else:
    print('The movie', movie, 'starts at', showtime)