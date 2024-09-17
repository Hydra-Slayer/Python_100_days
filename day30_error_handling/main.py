# try:
#     with open("afile.txt") as file:
#         file.read()
        
# except FileNotFoundError as e:
#     print(f"{e.filename} does not exist.")

# else:
#     print("Some error occured")
# finally:
#     print("Execution completed")

# height = float(input("Enter Height: "))
# if height> 2:
#     raise ValueError("Human height cannot be more than 2 meters")

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try: 
    make_pie(4)

except (IndexError):
    print("Fruit pie")
    
    
###modified password manage and nato project