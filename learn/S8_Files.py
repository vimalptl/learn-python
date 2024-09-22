#Files in Python
#   Mode     Meaning
#   r        Read
#   w        Write
#   a        Append
#   r+       Read and Write
#   w+       Write and Read
#   b        Binary mode
hosts = open('C:/vimaljs/python/Notes.txt', 'r')
hosts_file = hosts.read()
print(hosts_file)
#Seek to end of file
print ("Current Position: " + str(hosts.tell()))
#Seek to start of file
hosts.seek(0)
print ("Current Position: " + str(hosts.tell()))
#Close file after reading.
print('File Closed: ' + str(hosts.closed)) 
if not hosts.closed:
    hosts.close()
print('File Closed: ' + str(hosts.closed)) 

#To automatically close file use with statement
with open('C:/vimaljs/python/Notes.txt', 'r') as hosts:
    hosts_file = hosts.read()
    print(hosts_file)   

print("File Mode: " + hosts.mode)

#Write to a file
with open('C:/vimaljs/python/PyWriteNotes1.txt', 'w') as hosts:
    hosts.write("Vimal, 1234567890" + "\n")
    hosts.write("Vijayalakshmi, 9876543210" + "\n")
    print("# of char in file: " + str(len(hosts_file)))
