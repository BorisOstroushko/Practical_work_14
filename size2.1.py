import os

def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)

    for item in items:
        print (item)

if __name__== "__main__":
   main()