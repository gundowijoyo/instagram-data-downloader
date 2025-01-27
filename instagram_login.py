import instaloader
loader = instaloader.Instaloader()

loader.context.log("Masukkan username dan password")
loader.load_session_from_file("username")  
loader.login("username", "password") 
