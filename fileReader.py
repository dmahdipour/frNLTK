import json


def my_file_reader(myFile, fileEncode):
    fileContent = open(myFile, encoding = fileEncode)
    return fileContent.read()


def my_floatFile_reader(myFile):
    fileContent = open(myFile, 'r')
    x = [float(line.strip()) for line in fileContent if line]    
    return x


def my_Json_reader(myFile, fileEncode, keyName):
    with open(myFile, 'r', encoding = fileEncode) as fp:
        obj = json.load(fp, strict=False)
    return obj[keyName]