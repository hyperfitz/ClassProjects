"""
This is a program that uses some functions to process user inputs for storing, listing, and searching movie titles
in a list of dictionaries. The movies are user-defined and are no longer stored once the program exits. The functions are
unnecessary but part of the exercise was to define functions and then use them.

This program is complete as of Sep 23, 2020.
"""



while True == True:
    StartProgram = input("Do you want to run this program? Enter yes or no: ")
    StartProgramLower = StartProgram.lower()
    if StartProgramLower == "no":
        print("Program will now exit.")
        quit()
    elif StartProgramLower != "yes":
        print("please type a valid option")
        continue
    else:
        movies = []


        def AddMovie():
            title = input("Enter the movie title: ")
            director = input("Enter the movie director: ")
            year = input("Enter the movie release year: ")
            movies.append({'title': title, 'director': director, 'year': year})
            print(f"You've added: ")
            print(f"""movie "{title}",""")
            print(f"""director "{director}",""")
            print(f"""released "{year}".""")


        def ListMovies():
            for movie in movies:
                print(f"""Movie: {movie["title"]}, directed by {movie["director"]}, released in {movie["year"]}.""")


        def FindMovie():
            Input = input("Enter the title you'd like to find (not case sensitive): ")
            Result = {}
            for movie in movies:
                if movie["title"].lower() == Input.lower():
                    Result = movie
                else:
                    continue
            if bool(Result) == True:
                print(f"""Movie: {Result["title"]}, directed by {Result["director"]}, released in {Result["year"]}.""")
            else:
                print(f"That title does not exist in this archive.")


        while True == True:
            MENU_PROMPT = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")
            if MENU_PROMPT == "q":
                print("Program will now exit.")
                quit()
            elif MENU_PROMPT == "a":
                AddMovie()
            elif MENU_PROMPT == "l":
                ListMovies()
            elif MENU_PROMPT == "f":
                FindMovie()
            else:
                print("Please choose a valid option.")
                continue