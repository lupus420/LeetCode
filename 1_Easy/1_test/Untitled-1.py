txt = "I like bananas"
while (" " in txt):
	space_index = txt.index(" ")
	txt[space_index + 1].upper()
print(txt)
