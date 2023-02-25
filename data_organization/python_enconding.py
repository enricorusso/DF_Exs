str = "utf-16 encoding😉".encode("utf-16")

with open("python_UTF16.txt", "wb") as f:
	f.write(str) 

f.close()
	
