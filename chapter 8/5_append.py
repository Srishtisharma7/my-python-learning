# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.  [default]
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc).

st = "\nHey Harry you are amazing"

f = open("/Users/srishtisharma/python/code harry/chapter 8/myfile.txt", "a")    # opening "myfile.txt" in append mode, every time we execute this program , string gets append or added to the list

f.write(st)

f.close()

# writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.