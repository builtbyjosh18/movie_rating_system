# Today we will be building a movie rating system
movie_ratings = {
    "Inception": 9,
    "Titanic": 8,
    "TMNT": 8,
    "Going Home": 9,
    "The Witcher": 7
}

# Showing the user available options
print("Hello welcome to Movies! \n")

print('''To add or remove a movie from the list, enter '1' \n''')
print("If you want to update the rating of an existing movie, enter \"2\" \n")
print("If you want to search for a movie's rating by its title, enter \"3\".\n")
print("If you want to view all movies with their ratings enter \"4\"\n")
print("The key to exiting for another customer is to enter \"Exit\"\n")


# Function to add or delete movies
def add_remove():
    selection = False
    while not selection:
        choice = input("Please enter your choice (a to delete, b to add): ")

        if choice == 'a':
            correct_pick = False
            while not correct_pick:
                removed_movie = input("What movie would you like to delete: ")
                if removed_movie not in movie_ratings:
                    print("The movie you want to remove isn’t available. Pick again.")
                else:
                    correct_pick = True
                    movie_ratings.pop(removed_movie)
                    print(f"{removed_movie} has been removed successfully.")

        elif choice == 'b':
            added_movie = input("Please enter the movie you want to add: ")
            added_rating = int(input("Please enter your rating of the movie: "))
            movie_ratings.update({added_movie: added_rating})
            print(f"{added_movie} has been added successfully with rating {added_rating}.")

        # Asking the user if they want to exit the loop
        termination = input("Do you want to exit the loop (enter Y/N)? ")
        if termination.upper() == 'Y':
            selection = True
        elif termination.upper() == 'N':
            selection = False
        else:
            print("Invalid input. Please enter Y or N.")


# Function to update the rating of an existing movie
def rating():
    change_rating = False
    while not change_rating:
        movie_change = input("Please enter the name of the movie you want to change: ")
        if movie_change in movie_ratings:
            movie_score = int(input(f"Please enter the new rating of {movie_change}: "))
            movie_ratings[movie_change] = movie_score
            print(f"The rating of {movie_change} has been updated to {movie_score}.")
        else:
            print("Movie not found in the list.")

        continuation = input("Please enter if you would like to continue updating (Y or N): ")
        if continuation.upper() == 'N':
            change_rating = True


# Allowing the user to search for movie rating by title
def movie_search():
    search = False
    while not search:
        searching = input("Please enter the name of the movie you are searching for: ")
        if searching in movie_ratings:
            print(f"{searching}: {movie_ratings[searching]}")
        else:
            print("Movie not found in the list.")

        further = input("Do you want to continue searching (Y/N)? ")
        if further.upper() == 'N':
            search = True


# Function to view all movies and ratings
def view_movies(dict):
    return f"These are the current movie selections and their ratings: {movie_ratings}"


# Main program sequencing
Exit = False
while not Exit:
    browsing = input("Please enter the number of the action you want to take: ")

    if browsing == '1':
        add_remove()
    elif browsing == '2':
        rating()
    elif browsing == '3':
        movie_search()
    elif browsing == '4':
        print(view_movies(movie_ratings))
    else:
        print("Invalid selection. Please choose a valid option.")

    end_choice = input("Do you want to exit? (Type 'Exit' to quit): ")
    if end_choice == "Exit":
        Exit = True
