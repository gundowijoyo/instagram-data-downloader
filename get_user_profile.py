import instaloader
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")
print(f"Username: {profile.username}")
print(f"Full Name: {profile.full_name}")
print(f"Bio: {profile.biography}")
print(f"Followers: {profile.followers}")
print(f"Following: {profile.followees}")
print(f"Posts: {profile.mediacount}")
