def createFile(file_name):
    try:
        file1=open(file_name,"w")
        file1.write("Hai Aswin, Welcome to Avodha")
        file1.close()
        return "file created with name "+file_name
    except:
        return "Something Wrong..."

def readFile(file_name):
    try:
        file1=open(file_name,"r")
        content=file1.read()
        file1.close()
        return content
    except:
        return "File not found"

def addContentToFile(file_name,content):
    try:
        file1 = open(file_name,"a")
        file1.write("\n"+content)
        file1.close()
        return "content added to the file"
    except:
        return "Somthing Wrong"

def mainFunction():
    i=str(input("\nTo create file Enter 1 \nTo read file Enter 2\nTo add content Enter 3\nTo exit press any key\n"))
    if i=="1":
        file_name=input("Enter the file name : ")
        print(createFile(file_name))
        mainFunction()
    elif i=="2":
        file_name=input("Enter the file name : ")
        print(readFile(file_name))
        mainFunction()
    elif i=="3":
        file_name = input("Enter the file name : ")
        content=input("Type Your content : ")
        print(addContentToFile(file_name,content))
        mainFunction()
    else:

        return
mainFunction()
print("Bye...")

# Output
# To create file Enter 1
# To read file Enter 2
# To add content Enter 3
# To exit press any key
# 1
# Enter the file name : demo.txt
# file created with name demo.txt
#
# To create file Enter 1
# To read file Enter 2
# To add content Enter 3
# To exit press any key
# 2
# Enter the file name : demo.txt
# Hai Aswin, Welcome to Avodha
#
# To create file Enter 1
# To read file Enter 2
# To add content Enter 3
# To exit press any key
# 3
# Enter the file name : demo.txt
# Type Your content : welcome to python
# content added to the file
#
# To create file Enter 1
# To read file Enter 2
# To add content Enter 3
# To exit press any key
# g
# Bye...