def main():
    file_name = input("> ").lower().strip()
    print(check(file_name))


def check(file_name):
    for i in range(len(file_name)):
        if file_name[i] == ".":
            # determine length file extension
            length_ext = len(file_name) - i - 1

            # determine location file extension, add 1 because includes last char
            ext = file_name[i+1:i + length_ext + 1]

            # png, jpg, jpeg, gif == image
            if ext == "png" or ext == "gif":
                return "image/" + ext
            elif ext == "jpg" or ext == "jpeg":
                return "image/jpeg"
            # pdf, zip == application
            elif ext == "pdf" or ext == "zip":
                return "application/" + ext
            # txt == text
            elif ext == "txt":
                return "text/plain"
    return "application/octet-stream"


main()