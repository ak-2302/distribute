import os
class info:
    def __init__(self) -> None:
        with open("README.md","w",encoding="utf-8") as f:
            f.write("# content\n")
        with open("README.md","a",encoding="utf-8") as f:
            self.tree(dir=".",depth=0,file=f)
        pass
    def tree(self,dir,depth,file):
        if depth == 0:
            print("    "+os.getcwd().split("\\")[-1]+"  ",file=file)
        for i in range(len(os.listdir(dir))):
            if i == len(os.listdir(dir))-1:
                text = " "+"┃ "*(depth)+"┗ "+os.listdir(dir)[i]
            else:
                text = " "+"┃ "*(depth)+"┣ "+os.listdir(dir)[i]
            size = "size="+str(self.size(dir+"/"+os.listdir(dir)[i]))
            text += "-"*(30-len(text))+ size+"  "
            print("    "+text,file=file)
            if os.path.isdir(os.listdir(dir)[i]):
                self.tree(dir=dir+"/"+os.listdir(dir)[i],depth=depth+1,file=file)
    def size(self,path='.'):
        total = 0
        if os.path.isfile(path):
            return os.path.getsize(path)
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.size(entry.path)
        return total
info()