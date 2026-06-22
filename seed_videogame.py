from datetime import date

from game_review.models import Genre, VideoGame


games = [
    {
        "title": "Hades",
        "developer": "Supergiant Games",
        "publisher": "Supergiant Games",
        "genre": "Action",
        "release_date": date(2020, 9, 17),
        "description": (
            "A fast-paced action game where Zagreus repeatedly attempts to escape "
            "the Underworld while fighting enemies and receiving help from the gods."
        ),
    },
    {
        "title": "Devil May Cry 5",
        "developer": "CAPCOM",
        "publisher": "CAPCOM",
        "genre": "Action",
        "release_date": date(2019, 3, 8),
        "description": (
            "A stylish action game where players control several demon hunters, "
            "combine attacks, and fight powerful enemies."
        ),
    },
    {
        "title": "Life is Strange",
        "developer": "DONTNOD Entertainment",
        "publisher": "Square Enix",
        "genre": "Adventure",
        "release_date": date(2015, 1, 29),
        "description": (
            "A story-based adventure game about a student who discovers that she can "
            "rewind time and change the results of important decisions."
        ),
    },
    {
        "title": "Firewatch",
        "developer": "Campo Santo",
        "publisher": "Panic",
        "genre": "Adventure",
        "release_date": date(2016, 2, 9),
        "description": (
            "A first-person adventure game where a fire lookout explores the Wyoming "
            "wilderness and investigates unusual events."
        ),
    },
    {
        "title": "Baldur's Gate 3",
        "developer": "Larian Studios",
        "publisher": "Larian Studios",
        "genre": "Role-Playing Game (RPG)",
        "release_date": date(2023, 8, 3),
        "description": (
            "A party-based role-playing game where players explore a fantasy world, "
            "complete quests, fight enemies, and make choices that affect the story."
        ),
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "developer": "CD PROJEKT RED",
        "publisher": "CD PROJEKT RED",
        "genre": "Role-Playing Game (RPG)",
        "release_date": date(2015, 5, 18),
        "description": (
            "An open-world role-playing game where Geralt of Rivia searches for Ciri "
            "while completing quests and hunting dangerous monsters."
        ),
    },
    {
        "title": "DOOM Eternal",
        "developer": "id Software",
        "publisher": "Bethesda Softworks",
        "genre": "Shooter",
        "release_date": date(2020, 3, 19),
        "description": (
            "A fast-paced first-person shooter where the player fights armies of "
            "demons using powerful weapons and constant movement."
        ),
    },
    {
        "title": "Titanfall 2",
        "developer": "Respawn Entertainment",
        "publisher": "Electronic Arts",
        "genre": "Shooter",
        "release_date": date(2016, 10, 28),
        "description": (
            "A first-person shooter that combines fast movement, gun combat, and "
            "large pilotable machines called Titans."
        ),
    },
    {
        "title": "Sid Meier's Civilization VI",
        "developer": "Firaxis Games",
        "publisher": "2K",
        "genre": "Strategy",
        "release_date": date(2016, 10, 21),
        "description": (
            "A turn-based strategy game where players build a civilization, manage "
            "cities, research technology, and compete with other nations."
        ),
    },
    {
        "title": "XCOM 2",
        "developer": "Firaxis Games",
        "publisher": "2K",
        "genre": "Strategy",
        "release_date": date(2016, 2, 5),
        "description": (
            "A turn-based strategy game where players command a resistance force "
            "against an alien occupation of Earth."
        ),
    },
    {
        "title": "Stardew Valley",
        "developer": "ConcernedApe",
        "publisher": "ConcernedApe",
        "genre": "Simulation",
        "release_date": date(2016, 2, 26),
        "description": (
            "A farming and life simulation game where players rebuild a farm, grow "
            "crops, raise animals, mine, fish, and meet local residents."
        ),
    },
    {
        "title": "Cities: Skylines",
        "developer": "Colossal Order Ltd.",
        "publisher": "Paradox Interactive",
        "genre": "Simulation",
        "release_date": date(2015, 3, 10),
        "description": (
            "A city-building simulation game where players design roads, manage "
            "services, develop neighborhoods, and respond to the needs of citizens."
        ),
    },
    {
        "title": "EA SPORTS FC 25",
        "developer": "EA Canada and EA Romania",
        "publisher": "Electronic Arts",
        "genre": "Sports",
        "release_date": date(2024, 9, 27),
        "description": (
            "A soccer game where players control real clubs and athletes in "
            "single-player, multiplayer, and team-management modes."
        ),
    },
    {
        "title": "NBA 2K25",
        "developer": "Visual Concepts",
        "publisher": "2K",
        "genre": "Sports",
        "release_date": date(2024, 9, 6),
        "description": (
            "A basketball game that allows players to control NBA teams, build custom "
            "players, manage rosters, and compete online or offline."
        ),
    },
    {
        "title": "Forza Horizon 5",
        "developer": "Playground Games",
        "publisher": "Xbox Game Studios",
        "genre": "Racing",
        "release_date": date(2021, 11, 9),
        "description": (
            "An open-world racing game set in Mexico where players collect cars, "
            "explore different environments, and enter races and challenges."
        ),
    },
    {
        "title": "F1 24",
        "developer": "Codemasters",
        "publisher": "Electronic Arts",
        "genre": "Racing",
        "release_date": date(2024, 5, 31),
        "description": (
            "A Formula One racing game where players compete as real drivers and teams "
            "across official tracks and racing events."
        ),
    },
    {
        "title": "Portal 2",
        "developer": "Valve",
        "publisher": "Valve",
        "genre": "Puzzle",
        "release_date": date(2011, 4, 19),
        "description": (
            "A first-person puzzle game where players create portals and use physics, "
            "timing, and objects to solve test chambers."
        ),
    },
    {
        "title": "The Talos Principle",
        "developer": "Croteam",
        "publisher": "Devolver Digital",
        "genre": "Puzzle",
        "release_date": date(2014, 12, 11),
        "description": (
            "A first-person puzzle game where an artificial intelligence solves logic "
            "challenges while exploring questions about consciousness and humanity."
        ),
    },
    {
        "title": "Resident Evil 7 Biohazard",
        "developer": "CAPCOM",
        "publisher": "CAPCOM",
        "genre": "Horror",
        "release_date": date(2017, 1, 24),
        "description": (
            "A first-person survival horror game where the player explores a dangerous "
            "plantation, solves puzzles, and manages limited supplies."
        ),
    },
    {
        "title": "Alien: Isolation",
        "developer": "Creative Assembly",
        "publisher": "SEGA",
        "genre": "Horror",
        "release_date": date(2014, 10, 7),
        "description": (
            "A survival horror game where Amanda Ripley explores a damaged space "
            "station while avoiding a deadly alien creature."
        ),
    },
]


for game_data in games:
    genre = Genre.objects.get(name=game_data["genre"])

    VideoGame.objects.create(
        title=game_data["title"],
        developer=game_data["developer"],
        publisher=game_data["publisher"],
        genre=genre,
        release_date=game_data["release_date"],
        description=game_data["description"],
    )

    print(f"Created game: {game_data['title']}")


print("Finished creating 20 video games.")
