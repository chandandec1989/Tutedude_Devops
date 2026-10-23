def get_data():
    
    with open("name.txt") as f:
        
        name = f.read()
        name = name.splitlines()

    for i, person in enumerate(name, start=1):
        print(f"{i}.{person}")
    
    return name

    
    