from game_review.models import GameLibraryEntry, Profile, Review, VideoGame


reviews = [
    ("Saud", "Hades", 9, "Excellent combat", "The combat is fast, responsive, and stays interesting because every escape attempt feels different.", True),
    ("Saud", "Baldur's Gate 3", 10, "A complete RPG", "The choices, characters, combat, and exploration make this one of the strongest role-playing games I have played.", True),
    ("Saud", "DOOM Eternal", 8, "Fast and demanding", "The movement and combat are excellent, although some fights can become overwhelming.", True),
    ("Saud", "Forza Horizon 5", 8, "Great open-world racing", "The map is enjoyable to explore and the large selection of cars gives the game plenty of variety.", True),

    ("Alex", "Life is Strange", 9, "Strong story and characters", "The story is emotional and the decisions make the player feel involved in what happens.", True),
    ("Alex", "Firewatch", 8, "Short but memorable", "The game has excellent dialogue and atmosphere, but it ends sooner than I expected.", True),
    ("Alex", "Portal 2", 10, "Creative puzzle design", "The puzzles are clever, the writing is funny, and the mechanics are introduced at a good pace.", True),
    ("Alex", "Stardew Valley", 9, "Relaxing and rewarding", "There are many activities to complete, and the game gives the player freedom to progress at their own speed.", True),

    ("Maya", "Baldur's Gate 3", 9, "Choices matter", "The game gives the player many ways to solve problems and makes decisions feel meaningful.", True),
    ("Maya", "The Witcher 3: Wild Hunt", 9, "Excellent world and quests", "The world is detailed and even many of the smaller quests have interesting stories.", True),
    ("Maya", "Resident Evil 7 Biohazard", 8, "Very tense horror", "The atmosphere and sound design create constant tension, especially during the first half of the game.", True),
    ("Maya", "Alien: Isolation", 7, "Scary but too long", "The alien creates great tension, but some sections feel repetitive and make the game longer than necessary.", True),

    ("Daniel", "DOOM Eternal", 9, "Excellent shooter", "The game rewards movement, quick decisions, and using the correct weapon for each enemy.", True),
    ("Daniel", "Titanfall 2", 9, "Great campaign", "The movement system and level design make the campaign exciting from beginning to end.", True),
    ("Daniel", "Sid Meier's Civilization VI", 8, "Deep strategy game", "There are many systems to learn, and each match can develop differently depending on the chosen civilization.", True),
    ("Daniel", "XCOM 2", 8, "Tactical and challenging", "The battles require careful planning, but missing high-percentage attacks can sometimes feel frustrating.", True),

    ("Lina", "EA SPORTS FC 25", 6, "Fun but familiar", "The matches are enjoyable, but the game feels too similar to earlier entries in the series.", False),
    ("Lina", "NBA 2K25", 6, "Good basketball gameplay", "The gameplay is solid, but some modes feel repetitive and depend too much on progression systems.", False),
    ("Lina", "Stardew Valley", 10, "Easy to keep playing", "The farming, relationships, exploration, and steady progress make the game relaxing and enjoyable.", True),
    ("Lina", "Life is Strange", 8, "Emotional adventure", "The characters and story are memorable, although some dialogue and choices feel unrealistic.", True),
]


for profile_name, game_title, rating, review_title, review_text, recommended in reviews:
    profile = Profile.objects.get(display_name=profile_name)
    game = VideoGame.objects.get(title=game_title)

    library_entry = GameLibraryEntry.objects.get(
        profile=profile,
        video_game=game,
    )

    Review.objects.create(
        game_library_entry=library_entry,
        rating=rating,
        review_title=review_title,
        review_text=review_text,
        recommended=recommended,
    )

    print(f"Created review: {profile_name} - {game_title}")


print("Finished creating 20 reviews.")
