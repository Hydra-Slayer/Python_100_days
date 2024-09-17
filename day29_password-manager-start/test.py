import json
with open("data.json","r") as data_file:
    # data.write(f"{website}\n{email}\n{password}\n")
    try:
        data = json.load(data_file)
        try:
            if data["amazon"]:
                print("True")
        except KeyError:
            pass
            
    except json.decoder.JSONDecodeError:
        print("file is empty")
    
