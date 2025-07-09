import sys
import os

if (len(sys.argv) == 3):
    directory = sys.argv[1]
    name = sys.argv[2]
    try:
        folder = os.listdir(path=directory)
        print("### OLD DIRECTORY ##")
        print(folder)
        for ep,old in enumerate(folder,1):
            ext = os.path.splitext(old)[1]
            new = name + " EP" + str(ep) + ext
            old_path = os.path.join(directory,old)
            new_path = os.path.join(directory,new)
            os.rename(old_path,new_path)
            print(old, " -> ", new)
        print("### NEW DIRECTORY ##")
        print(os.listdir(path=directory))
    except:
        print("ERROR: something went wrong")
else:
    print("ERROR: Requires", len(sys.argv), "arguments!")


