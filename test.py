from PIL import Image

path = "template/img/avatar.png"

img = Image.open(path)
img = img.convert("RGBA")
datas = img.getdata()

newData = []

for item in datas:
    newData.append((item[0], item[1], item[2], 150))

img.putdata(newData)
img.save(path + "1.png", "PNG")
