import os
import socket
from collections import Counter

outputTxt = '------------- Starting the Docker Container ------------- \n'

def getIpAddrMachine():
    global outputTxt
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    outputTxt = outputTxt + '\n'
    outputTxt = outputTxt + '***** || Task e) Find IP Address of my machine \n'
    outputTxt = outputTxt + 'Ip Addr of my machine is ' + ip_address + '\n'
    outputTxt = outputTxt+ '\n'

directory_path = "/home/data/"
output_path = "/home/output/results.txt"

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Filter for text files with a .txt extension
text_files = [file for file in files if file.endswith(".txt")]

def getWordsInFiles():
    global outputTxt
    
    for file in files:
        if(file.endswith(".txt")):
            if file.startswith("IF.txt"):
                file1 = file
            else:
                file2 = file
          
    with open( directory_path + file1, 'r') as file:
        content = file.read()
        
    words = content.split();
    
    outputTxt = outputTxt + "no of words in " + file1 + ' are: '+ str(len(words)) + '\n'
    
    word_count = Counter(words)
    
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    
    top_words = list(sorted_word_count.items())[:3]
    
    with open( directory_path + file2, 'r') as file:
        content = file.read()
        
    words1 = content.split();
    
    outputTxt = outputTxt + "no of words in " + file2 + ' are: ' + str(len(words1))+ '\n'
    outputTxt = outputTxt + '\n'
    
    outputTxt = outputTxt + '***** || Task c) Total number of words in both the files \n'
    totalWords = len(words) +len(words1)
    outputTxt = outputTxt + 'total no of words in both the files: ' + str(totalWords) + '\n'
    outputTxt = outputTxt + '\n'
    
    outputTxt = outputTxt + '***** || Task d) top 3 words with maximum number of counts in IF.txt \n'
    
    for word in top_words:
        outputTxt = outputTxt + str(word) + ' '
        outputTxt = outputTxt+'\n'
    
    

outputTxt = outputTxt + '***** || Task a) All the text files at the location "/home/data" are : \n'

for eachFile in os.listdir(directory_path):
    if eachFile.endswith(".txt"):
        outputTxt=outputTxt+eachFile+"\n"
        
outputTxt = outputTxt+ '\n'
outputTxt = outputTxt + '***** || Task b) The number of words in each text files are : \n'
getWordsInFiles()

getIpAddrMachine()

# Redirect print to a file
with open(output_path, "w") as output_file:
    output_file.write(outputTxt)

# Redirect print to a file
with open(output_path, "r") as output_file:
    
    result_content = output_file.read()
    print(result_content)

print('All the Tasks are Completed')