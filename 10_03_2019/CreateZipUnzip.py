import shutil

def main():
    inputDirName = eval (input("Enter Directory Name to be archived:"))
    ZipFileName = eval (input("Enter zip File name:"))

    shutil.make_archive(ZipFileName, "zip", inputDirName)
    print("Folder Zipped..!!")
    unzipName = ZipFileName + ".zip"
    unzipDirName = inputDirName + "\\try"
    shutil.unpack_archive(unzipName, unzipDirName)
    print("Folder Unzipped..!!")

if __name__ == '__main__':
    main()
