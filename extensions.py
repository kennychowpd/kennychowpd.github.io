def main():
    user_input = input("Input a file name: ").strip().lower()
    
    file_type = ck_file_type(user_input)
    
    print(file_type)
    

def ck_file_type(text):
    image = ["gif", "jpg", "jpeg", "png", ]
    app = ["pdf", "zip"]

    if "." in text:
        ext = text.split(".").pop()
    if ext in image:
        return f"image/{ext}"
    elif ext in app:
        return f"application/{ext}"
    elif ext == "txt":
        return f"text/plain"
    return "application/octet-stream"

main()