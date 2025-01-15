# 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open("/Users/srishtisharma/python/code harry/chapter 8/donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")
# read data assigned to the content variable; 
#contentnew store the the content data but now having replaced word donkey with ######

with open("/Users/srishtisharma/python/code harry/chapter 8/donkey.txt", "w") as f:
    f.write(contentNew)
#open file in w mode , and pass the content new data with updated words

'''
old text = donkey is a nice ###### not a bad donkey
new text = ###### is a nice ###### not a bad ######
'''



# 5. Repeat program 4 for a list of such words to be censored.

words = ["old", "to", "goes"]     # declared list

with open("/Users/srishtisharma/python/code harry/chapter 8/donkey.txt", "r") as f:
    content = f.read()

for word in words:       # search in list
    content = content.replace(word, "#" * len(word))    # put no .of letters or length of the word

with open("/Users/srishtisharma/python/code harry/chapter 8/donkey.txt", "w") as f:
    f.write(content)        #write updated content


'''
old text = he is very old but he likes me and he goes to dance
new text = he is very ### but he likes me and he #### ## dance
'''