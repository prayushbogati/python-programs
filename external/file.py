import os

print(os.getcwd())

os.chdir("E:/docs")
print(os.getcwd())

# os.mkdir("innerDoc")
print(os.listdir())

os.rename("Photos", "photos")
print(os.listdir())