file1 = open("testfile1.txt", "r")
x = file1.readlines()
file1.close()
file2 = open("testfile2.txt", "w")
file2.writelines(x)
file2.close()
