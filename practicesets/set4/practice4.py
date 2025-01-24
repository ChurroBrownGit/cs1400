team_size = int(input("Enter the size of your gaming team: "))
game_genre = input("Enter the game genre for the event (MOBA, FPS, RTS, Battle Royale): ").lower()
experience_level = input("Enter your experience level (beginner, intermediate, expert): ").lower()
location = input("Is the event local or online? (local/online): ").lower()

#Unnested (original)
if (team_size >= 5 and game_genre == "moba" and experience_level == "expert" and location == "local") or \
   (team_size == 1 and game_genre == "fps" and experience_level == "beginner" and location == "online") or \
   (team_size >= 3 and game_genre == "rts" and experience_level == "intermediate" and location == "local") or \
   (team_size <= 2 and game_genre == "battle royale" and experience_level == "expert" and location == "online"):
    print("You are eligible to participate in the event.")
else:
    print("You do not meet the criteria for the event.")

#Nested
if team_size >= 5:
    if game_genre == "moba":
        if experience_level == "expert":
            if location == "local":
                print("You are eligible to participate in the event.")
            else:
                print("You do not meet the criteria for the event.")
if team_size == 1:
    if game_genre == "fps":
        if experience_level == "beginner":
            if location == "online":
                print("You are eligible to participate in the event.")
            else:
                print("You do not meet the criteria for the event.")
if team_size >= 3:
    if game_genre == "rts":
        if experience_level == "intermediate":
            if location == "local":
                print("You are eligible to participate in the event.")
            else:
                print("You do not meet the criteria for the event.")
if team_size <= 2:
    if game_genre == "battle royale":
        if experience_level == "expert":
            if location == "online":
                print("You are eligible to participate in the event.")
            else:
                print("You do not meet the criteria for the event.")
else:
    print("You do not meet the criteria for the event.")
