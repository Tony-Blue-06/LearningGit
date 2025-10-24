from pathlib import Path

path = Path('Programming.txt')

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I love working with data.\n"


path.write_text(contents)

content = path.read_text()
print(content)