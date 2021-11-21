#import time
import sys  
import multiprocessing

encryption_code_small= {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n',
                        'z':'a','y':'b','x':'c','w':'d','v':'e','u':'f','t':'g','s':'h','r':'i','q':'j','p':'k','o':'l','n':'m'}


encryption_code_capital={'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N',
                            'Z':'A','Y':'B','X':'C','W':'D','V':'E','U':'F','T':'G','S':'H','R':'I','Q':'J','P':'K','O':'L','N':'M'}


# starting time 
#begin = time.time()

#input file name and number of lines per smaller files 
# arguments to be passed in command line
fileName=sys.argv[1]
#smaller file to be processed 
smallfile = None
lines_per_smaller_file = 400
# names of smaller files splitted from the main input file
small_files_list=list()
#number of lines in input file
num_lines = sum(1 for line in open(str(fileName)))

#splitting bigger file into smaller files
if lines_per_smaller_file>num_lines:
    small_files_list.append(str(fileName))
else:
    with open(str(fileName)) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_smaller_file == 0:
                if smallfile:
                    smallfile.close()
                file_num  =lineno + lines_per_smaller_file
                small_filename = 'small_file_{}.txt'.format(file_num)
                small_files_list.append(small_filename)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()

# merging multiple text files into single file and encrypting at same time
def readWrite(fileList):
    for current_file in fileList:
        with open(current_file,'r') as temp_file:
            while True:
                reader  =temp_file.read(1)
                with open('outputFile.txt','a+') as file1:
                    if str(reader).isalpha():
                        if str(reader).isupper():
                            file1.write(encryption_code_capital[str(reader)])
                        else:
                           file1.write(encryption_code_small[str(reader)]) 
                    else:
                        file1.write(str(reader))
                if not reader:
                    break 
     


if __name__ == "__main__":
  # creating new process
    p1 = multiprocessing.Process(target=readWrite, args=(small_files_list,))
    # starting process
    p1.start()
    # wait until process is finished
    p1.join()

#edning of code time
#end = time.time()
#print(end-begin)
