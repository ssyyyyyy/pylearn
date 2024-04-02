import tables

def filetest(filename):
    with open(filename,'a') as f:
        f.write("hello")

if __name__ == "__main__":
    # os.mkdir("./testpackage1")
    # filetest("./testpackage1/hello.txt")
