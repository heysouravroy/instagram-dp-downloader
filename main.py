import instaloader

ig = instaloader.Instaloader()
dp = input("Enter the profile name : ")

ig.download_profile(dp , profile_pic_only=True)
