MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
	title = input("Enter the movie title: ")
	director = input("Enter the movie director: ")
	year = input("Enter the movie release year:")

	movies.append({
		'title': title,
		'director': director,
		'year': year
	})


def show_movies():
	for movie in movies:
		print_movie(movie)


def print_movie(movie):
	print(f"Title: {movie['title']}")
	print(f"Director: {movie['director']}")
	print(f"Release Year: {movie['year']}")


def find_movie():
	search_title = input("Enter movie title you are looking for: ")
	for movie in movies:
		if movie['title'] == search_title:
			print_movie()

def add_two_numbers(a,b):
	return a + b


def menu():
	selection = input(MENU_PROMPT)
	while selection != 'q':
		if selection == 'a':
			add_movie()
		elif selection == 'l':
			show_movies()
		elif selection == 'f':
			find_movie()
		else:
			print("Unknown command. Please try again.")





# menu()
first_number = input("enter first number")
second_number = input("enter second number")
sum_of = add_two_numbers(int(first_number),int(second_number))
print(sum_of)

