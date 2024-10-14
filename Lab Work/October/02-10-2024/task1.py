import instaloader

ig = instaloader.Instaloader()

username = input("Enter Username: ")

try:

    profile = instaloader.Profile.from_username(ig.context, username)


    print("Username: ", profile.username)
    print("Posts: ", profile.mediacount)
    print("Followers: ", profile.followers)
    print("Following: ", profile.followees)
    print("Bio: ", profile.biography)


    ig.download_profile(username, profile_pic_only=True)

except instaloader.exceptions.ProfileNotExistsException:
    print("The profile does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
