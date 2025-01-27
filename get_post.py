import instaloader
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, "username_Instagram")
for post in profile.get_posts():
    print(f"Post URL: https://www.instagram.com/p/{post.shortcode}/")
    print(f"Caption: {post.caption}")
    print(f"Likes: {post.likes}")
    print(f"Date: {post.date}")
    print("-" * 30)
  
