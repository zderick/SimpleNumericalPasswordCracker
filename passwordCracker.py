import pikepdf

FILEPATH = "Desktop/.../myFile.pdf"

for password in range(10000):
    try:
        with pikepdf.open(FILEPATH, password=str(password)):
            print("Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        continue
