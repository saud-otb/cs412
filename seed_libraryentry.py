from game_review.models import GameLibraryEntry, Profile, VideoGame


entries = [
    # Saud
    ("Saud", "Hades", "Played", 42),
    ("Saud", "Baldur's Gate 3", "Played", 95),
    ("Saud", "DOOM Eternal", "Played", 28),
    ("Saud", "Forza Horizon 5", "Played", 51),
    ("Saud", "The Witcher 3: Wild Hunt", "Currently Playing", 34),
    ("Saud", "Alien: Isolation", "Want to Play", 0),

    # Alex
    ("Alex", "Life is Strange", "Played", 14),
    ("Alex", "Firewatch", "Played", 6),
    ("Alex", "Portal 2", "Played", 12),
    ("Alex", "Stardew Valley", "Played", 80),
    ("Alex", "The Talos Principle", "Currently Playing", 9),
    ("Alex", "Cities: Skylines", "Want to Play", 0),

    # Maya
    ("Maya", "Baldur's Gate 3", "Played", 120),
    ("Maya", "The Witcher 3: Wild Hunt", "Played", 110),
    ("Maya", "Resident Evil 7 Biohazard", "Played", 11),
    ("Maya", "Alien: Isolation", "Played", 18),
    ("Maya", "Hades", "Currently Playing", 16),
    ("Maya", "DOOM Eternal", "Want to Play", 0),

    # Daniel
    ("Daniel", "DOOM Eternal", "Played", 30),
    ("Daniel", "Titanfall 2", "Played", 15),
    ("Daniel", "Sid Meier's Civilization VI", "Played", 140),
    ("Daniel", "XCOM 2", "Played", 75),
    ("Daniel", "F1 24", "Currently Playing", 22),
    ("Daniel", "Devil May Cry 5", "Want to Play", 0),

    # Lina
    ("Lina", "EA SPORTS FC 25", "Played", 65),
    ("Lina", "NBA 2K25", "Played", 48),
    ("Lina", "Stardew Valley", "Played", 72),
    ("Lina", "Life is Strange", "Played", 13),
    ("Lina", "Forza Horizon 5", "Currently Playing", 20),
    ("Lina", "Firewatch", "Want to Play", 0),
]


for profile_name, game_title, status, hours_played in entries:
    profile = Profile.objects.get(display_name=profile_name)
    game = VideoGame.objects.get(title=game_title)

    GameLibraryEntry.objects.create(
        profile=profile,
        video_game=game,
        status=status,
        hours_played=hours_played,
    )

    print(f"Created library entry: {profile_name} - {game_title} - {status}")


print("Finished creating 30 game library entries.")
