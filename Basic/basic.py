f = open("Hii.text")
content = f.read()
print(content)
f.close()

g = open("Sample.txt", "r")
# g.write("Long Off.......")
# g.write("Longgggg Off")
print(g.read())
