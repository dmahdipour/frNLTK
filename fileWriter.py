def my_file_line_writer(myPath, what2write):
    myFile = open(myPath, "w")
    for line in what2write:
        myFile.write(str(line) + "\n")
    myFile.close()


def my_file_writer(myPath, what2write):
    myFile = open(myPath, "w")
    myFile.write(str(what2write))
    myFile.close()