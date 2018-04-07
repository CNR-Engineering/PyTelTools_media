import Image
im = Image.open("mono_demo.gif")

# To iterate through the entire gif
try:
    while 1:
        im.seek(im.tell()+1)
        # do something to im
except EOFError:
    pass # end of sequence
