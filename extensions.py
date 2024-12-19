user_file=input("file name:").lower().strip()
if user_file.endswith(".gif"):
    print("image/gif")
elif user_file.endswith(".jpg"):
    print("image/jpeg")
elif user_file.endswith("jpeg"):
   print("image/jpeg")
elif user_file.endswith(".txt"):
   print("text/plain")
elif user_file.endswith(".pdf"):
   print("application/pdf")
elif user_file.endswith(".zip"):
   print("aplication/zip")
elif user_file.endswith(".png"):
   print("image/png")
else:
    print("application/octet-stream")