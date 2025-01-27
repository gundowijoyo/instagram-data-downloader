import instaloader
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")
for post in profile.get_posts():
    loader.download_post(post, target=profile.username)
  
