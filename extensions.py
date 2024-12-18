user_file=input("file name:").lower().strip()
if user_file.endswith(".gif"):
    print("image/gif")
elif user_file.endswith(".exe"):
   print("runfile or adminrun/exe aplication app,shorcut")
elif user_file.endswith(".jpg"):
    print("image or .jpg file/jpeg")
elif user_file.endswith("jpeg"):
   print("image/jpeg")
elif user_file.endswith(".txt"):
   print("text/plain")

