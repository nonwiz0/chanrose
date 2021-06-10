import os
from datetime import date

# Required input to generate new page
input_list = ['title', 'description', 'belongs', 'type']
projects_template = './projects/sample.html'

def hello():
    print("hello there")

def create_page():
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

    print(f"Generated {obj['belongs']}/{obj['titleUrl']}.html Complete")
    update_projects(obj)

def update_projects(obj):
    new_link = obj['titleUrl'] + '.html'
    file_path = "./projects.html"
    open_file = open(file_path)
    text = open_file.read()
    open_file.close()
    a_href = f"<a href='./projects/{new_link}' class='btn text-gray light-theme' data-type='{obj['type']}'> {obj['title']} </a>"
    text = text.replace("<!-- @{newLink} -->", "<!-- @{newLink} -->\n\t\t\t\t"+ a_href)
    open_file = open(file_path, 'w')
    open_file.write(text)
    open_file.close()
    print("updated projects.html successfully")

menu_list = {
    0: create_page,
    1: hello
}

def total_project():
    os.listdir('./projects')
while True:
    print("\nWelcome to Gemini Generator")
    print("="*50)
    print("Total Projects: ", len(os.listdir('./projects')) - 1)
    print("0). Create new page\n1). Say hello\n3). Exit")
    selection = int(input("➤ Your input: "))
    print("")
    if selection >=0 and selection <=1:
        menu_list.get(selection, "invalid input")()
    else:
        print("Saiyonara!")
        break;
    


