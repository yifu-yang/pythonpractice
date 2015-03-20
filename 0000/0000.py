from PIL import Image
head = Image.open('head.jpg')
no1 = Image.open('1.jpg')
newhead=Image.blend(head,no1,0.5)
newhead.save("no1.jpeg","JPEG")