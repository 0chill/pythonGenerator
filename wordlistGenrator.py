def main():
    fo = open("C:\Users\YourUser\Desktop/text2Wordlist.txt", "w+"); 
    #change the directory to whatever you want it to be
    
    number = 0000
    while(number != 10000):
        text2Wordlist = "xxx-xxx-%.4d" % number 
        number += 1
        fo.write(text2Wordlist + "\n")
    
    fo.close()
if __name__ == "__main__":
	main()
