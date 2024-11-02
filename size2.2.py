import os

def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
            for dirpath, dirnames, filenames in os.walk(path):
              for filename in filenames:
                    fp = os.path.join(dirpath, filename)
                    if os.path.isfile(fp):
                        size += os.path.getsize(fp)
    return size

def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)

    for item in items:
        full_path = os.path.join(pwd, item)
        size = get_size(full_path)
        print("{}{}".format(size, item))

if __name__== "__main__":
   main()