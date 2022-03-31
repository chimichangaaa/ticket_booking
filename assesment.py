"""
This Summative assesment is to make a prgogram where you book a movie ticket. 
Project made by Uyanga 10B
"""
#Funtion to book the movie tickets
def tickets():
    #we need to start with our variables.
    movies = ('Harry Potter 3', 'A Silent Voice', 'La')
    sessions = ('Morning', 'Afternoon', 'Evening')
    #Seats for each movie and each session
    movie0 = {'Morning':[1, 2, 3], 'Afternoon':[4, 5, 6], 'Evening':[7, 8, 9]}
    movie1 = {'Morning':[1, 2, 3], 'Afternoon':[4, 5, 6], 'Evening':[7, 8, 9]}
    movie2 = {'Morning':[1, 2, 3], 'Afternoon':[4, 5, 6], 'Evening':[7, 9]}

    phone_number = None
    name = None
    #enter name and phone number 
    name = input("Welcome to the Classic Movie Theatre! Please write your name: ")
    phone_number = input ("Please type in your phone number: ")
    #display the list of movies
    print()
    print("--------------------------------")
    print("         M o v i e s            ")
    print("--------------------------------")
    for movie in movies:
        print (movie)
    print()
    print()

    #select a movie
    movie_choice = None
    while movie_choice not in movies:
        movie_choice = input("Please choose a movie you want to watch: ")

#Display the available sessions
    print()
    print("--------------------------------")
    print("        * Sessions *            ")
    print("--------------------------------")
    for session in sessions:
        print (session)
    print()
    print()

    #select a session
    session_choice = None
    while session_choice not in sessions:
        session_choice = input("Please choose a session for the movie: ")

    #seats
    seat_choice = None
    unavailable_seats = None
    seat_text = ''
    print()
    print("--------------------------------")
    print("        * Seats    *            ")
    print("--------------------------------")

    match movies.index(movie_choice):
        case 0:
            unavailable_seats = movie0[session_choice]
        case 1:
            unavailable_seats = movie1[session_choice]
        case 2:
            unavailable_seats = movie2[session_choice]
    
    for seat in range (1,21):
        if seat in unavailable_seats:
            seat_text = seat_text + ' X'
        else:
            seat_text = seat_text + f" {seat}"
    print(seat_text)
    
    while seat_choice not in range(1,21):
        try:
            seat_choice = int(input ('Please enter your seat number: '))
        except:
            print("Wrong seat number.")
        if seat_choice in unavailable_seats or seat_choice not in range(1,21):
            print("Seat unavailable")
            seat_choice = None
        else:
            unavailable_seats.append(seat_choice)
    
    print(unavailable_seats)
    #Print ticket info
    print (f"Name: {name}, Phone: {phone_number}, Movie: {movie_choice}, Session: {session_choice}, Seat: {seat_choice}")

#Main code
while True:
    tickets()
    book_again = ''
    while book_again not in ('yes','no'):
        book_again = (input ("Would you like to book again?: ")).lower()
    if book_again == 'no':
        print('Okay, thank you and enjoy the movie!')
        break

