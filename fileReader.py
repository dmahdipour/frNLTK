def my_file_reader(myFile, fileEncode):
    fileContent = open(myFile, encoding = fileEncode)
    return fileContent.read()