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
            print(os.getcwd().split("\\")[-1],file=file)
        for i in range(len(os.listdir(dir))):
            if i == len(os.listdir(dir))-1:
                text = " "+"┃ "*(depth)+"┗━"+os.listdir(dir)[i]
            else:
                text = " "+"┃ "*(depth)+"┣━"+os.listdir(dir)[i]
            print(text,file=file,)
            if os.path.isdir(os.listdir(dir)[i]):
                self.tree(dir=dir+"/"+os.listdir(dir)[i],depth=depth+1,file=file)
info()