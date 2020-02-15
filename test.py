
from PIL import Image, ImageDraw, ImageFont

font_size = 7
text = "新年快乐！"
img_path = "C://Users//lwq//Desktop//py//680.jpg"

# 使用 pillow.Image读取图像，并使用load函数获取到每一个像素值
img_raw = Image.open(img_path)
img_array = img_raw.load()

# 新建一张画布，并选好你要使用的字体和字体大小
img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)

# 由于需要不断循环，所以这里可以while循环 yield 来实现一个生成器
def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

# 给这些字加上相应的颜色，写入新创建的画布中
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

# 保存图片
img_new.convert('RGB').save("C://Users//lwq//Desktop//py//save.jpg")