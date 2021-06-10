import os
from datetime import date

print("Welcome to Chanrose Page Generator")
# Required input to generate new page
input_list = ['title', 'description', 'belongs', 'type']
projects_template = './projects/sample.html'

# titleUrl = title in lowercase join by _ 
# belongs = either ['log', 'pages', 'projects']
# type = either ['Vanilla JS', 'Web App', 'PWA', 'IoT', 'CMS']
# date = Month day, Year = June 09, 2021
belong = ['log', 'pages', 'projects']
types = ['Vanilla JS', 'Web App', 'PWA', 'IoT', 'CMS']
obj = dict()
obj['date'] = date.today().strftime("%B %d, %Y")

# Input for title and description
obj[input_list[0]] = input(f"{input_list[0]}: ")
obj[input_list[1]] = input(f"{input_list[1]}: ")
obj['titleUrl'] = '-'.join(obj['title'].lower().split())

print("\nCurrent belongs options:")
for item in range(len(belong)):
    print(f"{item}: {belong[item]}")
tmp = int(input(f"{input_list[2]}: "))
obj[input_list[2]] = belong[tmp] if (tmp < len(belong)) else print("invalid input")


print("\nCurrent types options:")
for item in range(len(types)):
    print(f"{item}: {types[item]}")
tmp = int(input(f"{input_list[3]}: "))
obj[input_list[3]] = types[tmp] if (tmp < len(types)) else print("invalid input")

print("\nRead Property: ")
for item in obj:
    print(f"{item}: {obj[item]}") 
print("\n")

f_template = open(projects_template)
file_path = f"./{obj['belongs']}/{obj['titleUrl']}.html"
new_file = open(file_path, 'w')
temp = f_template.read()
for key, val in obj.items():
    temp = temp.replace("@{" + key + "}", val)
new_file.write(temp)
new_file.close()
f_template.close()

print(f"Generated {obj['belongs']} / {obj['titleUrl']}.html Complete")




