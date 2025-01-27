import instaloader
loader = instaloader.Instaloader()
hashtag = "nature"
for post in instaloader.Hashtag.from_name(loader.context, hashtag).get_posts():
    loader.download_post(post, target=hashtag)
  
