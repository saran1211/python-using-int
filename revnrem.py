while True:
	print("Enter 'x' for exit.")
	string = input("Enter any string: ")
	if string == 'x':
		break
	else:
		newstr = string
		print("\nRemoving vowels from the given string.")
		vowels = ('a', 'e', 'i', 'o', 'u')
		for x in string.lower():
			if x in vowels:
				s = newstr.replace(x,"")
		print("New string after removing all vowels!:",s)
		print("reverse of new string:",s[::-1])
