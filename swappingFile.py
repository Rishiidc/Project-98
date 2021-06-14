def swipeFileData():
    file1 = input("This file is from file 2")
    file2 = input("This file is from file 1")
    with open(file1,"r") as a:
        data_a = a.read()
    with open(file2,"r") as b:
        data_b = b.read()
    with open(file1,"w") as x:
        x.write(data_b)
    with open(file2,"w") as z:
        z.write(data_a)

swipeFileData()

