import os

def main():

    directory = input("Enter the directory where you wish to save the file : ")
    filename = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phonenumber = input("Enter your phone number : ")
    


    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,filename),'w+')
        writeFile.write("Name: " + name + ", ")
        writeFile.write("Address: " + address + ", ")
        writeFile.write("Phone Number: " + phonenumber + ", ")
        print("File contents:")
        print(writeFile.read())

        with open(os.path.join(directory,filename),'r') as f:
            for line in f:
                print(line)

        # readFile = open(os.path.join(directory,filename),'r')
        # line = readFile.read()
        # while line:
        #     line = line.rstrip()
        #     print(line)
        #     line = readFile.readline()
        # readFile.close()

        #print(readFile.read())

        #for line in readFile:
        #    print(line())
            

    else:
        print("Sorry that directory does not appear to exist.")

main()