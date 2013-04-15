# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import StringIO

IMAGE_WIDTH = 260
IMAGE_HEIGHT = 260
FONT_SIZE = 260

def get_font_image(word):
	# font = ImageFont.truetype("/Users/addsict/Downloads/migmix-1p-20121030/migmix-1p-bold.ttf", FONT_SIZE)
	font = ImageFont.truetype("/Users/addsict/Downloads/migmix-1p-20121030/migmix-1p-regular.ttf", FONT_SIZE)
	size = font.getsize(word)
	orig_width, orig_height = size

	background_color = (255, 255, 255) # white
	font_color = (0, 0, 0) # black
	img = Image.new('RGB', size, background_color)
	draw = ImageDraw.Draw(img)
	offset_top = 60
	draw.text((0, 0), word, font=font, fill=font_color)

	img = img.crop((0, offset_top, IMAGE_WIDTH, offset_top + IMAGE_HEIGHT))
	output = StringIO.StringIO()
	img.save(output, format='PNG')
	image_value = output.getvalue()
	output.close()
	return image_value
