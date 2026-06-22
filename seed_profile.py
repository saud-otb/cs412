from game_review.models import Profile


profiles = [
    {
        "display_name": "Saud",
        "bio": "Enjoys action games, RPGs, and competitive multiplayer games.",
    },
    {
        "display_name": "Alex",
        "bio": "Enjoys story-driven adventures, puzzle games, and simulation games.",
    },
    {
        "display_name": "Maya",
        "bio": "Enjoys horror games, role-playing games, and games with strong stories.",
    },
    {
        "display_name": "Daniel",
        "bio": "Enjoys shooters, racing games, and strategy games.",
    },
    {
        "display_name": "Lina",
        "bio": "Enjoys sports games, relaxing simulations, and adventure games.",
    },
]


for profile_data in profiles:
    Profile.objects.create(
        display_name=profile_data["display_name"],
        bio=profile_data["bio"],
    )
    print(f"Created profile: {profile_data['display_name']}")


print("Finished creating 5 profiles.")
