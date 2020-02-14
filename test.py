from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("D:\Philosopher\Philosopher.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.save(output_image_path)



if __name__ == '__main__':
    img = '111.png'
    watermark_text(img,
                   text=input(),
                   pos=(440, 240))