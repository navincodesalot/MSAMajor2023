file_name = input("File name: ").lower()
extension = ""

if file_name.find(".") != -1:
    extension = file_name.split(".")[1]
if file_name.endswith(".gif") or file_name.endswith(".jpg") or file_name.endswith(".png") or file_name.endswith(".jpeg"):
    print(f"image/{extension}")
elif file_name.endswith(".pdf") or file_name.endswith(".txt"):
    print(f"document/{extension}")
elif file_name.endswith(".zip"):
    print(f"file/{extension}")
else:
    print(f"application/octet-stream")