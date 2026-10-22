with open('name.txt') as f:
    
    name=f.read()
    
    name=name.splitlines()
    
    for i, name in enumerate(name):
        print(f"{i + 1}.{name}")
        

    