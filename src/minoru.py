# -*- coding: utf-8 -*-

import png, array
import sys

CANVAS_WIDTH = 26
CANVAS_HEIGHT = 14
BLACK_PIXEL_DETECTION_THRESHOLD = 80


def _is_black_block(pixels, x, y, dx, dy, width, height):
	total_pixel_count = dx * dy
	black_pixel_count = 0

	init_x = x * 3
	init_y = y * 3 * width
	for i in range(0, dy):
		for j in range(0, dx):
			r_index = init_x + init_y + j * 3 + i * 3 * width
			g_index = r_index + 1
			b_index = r_index + 2
			# if pixels[r_index] != 255 and pixels[g_index] != 255 and pixels[b_index] != 255:
			if pixels[r_index] == 0 and pixels[g_index] == 0 and pixels[b_index] == 0:
				black_pixel_count += 1
	
	if black_pixel_count >= BLACK_PIXEL_DETECTION_THRESHOLD:
		return True
	else:
		return False


def write_minoru(image_data):
	reader = png.Reader(bytes=image_data)
	w, h, pixels, metadata = reader.read_flat()

	block_width = w / CANVAS_WIDTH
	block_height = h / CANVAS_HEIGHT

	# [left-space, left-char, left-space, right-space, right-char]
	char_and_space_map = [[4, 4, 2, 2, 4],
                      	  [3, 3, 4, 4, 3],
                      	  [2, 3, 5, 5, 3],
                      	  [1, 3, 6, 6, 3],
                      	  [1, 3, 6, 6, 3],
                      	  [0, 3, 7, 7, 3],
                      	  [0, 3, 7, 7, 3],
                      	  [0, 3, 7, 7, 3],
                      	  [0, 3, 7, 7, 3],
                      	  [1, 3, 6, 6, 3],
                      	  [1, 3, 6, 6, 3],
                      	  [2, 3, 5, 5, 3],
                      	  [3, 3, 4, 4, 3],
                      	  [4, 4, 2, 2, 4]]

	minoru_str = ''
	minoru_str += '                ##############\n'
	minoru_str += '           ########        ########\n'
	minoru_str += '        #####                    #####\n'
	minoru_str += '      ####                          ####\n'

	for i in range(0, CANVAS_HEIGHT):
		# print left-side space
		for space in range(0, char_and_space_map[i][0]):
			minoru_str += ' '
		# print left-side character
		for char in range(0, char_and_space_map[i][1]):
			minoru_str += '#'
		# print left-side space
		for space in range(0, char_and_space_map[i][2]):
			minoru_str += ' '

		for j in range(0, CANVAS_WIDTH):
			if (_is_black_block(pixels,
		                   	   j * block_width,
		                   	   i * block_height,
		                   	   block_width,
		                   	   block_height,
		                   	   w,
		                   	   h)):
				minoru_str += '#'
			else:
				minoru_str += ' '

		# print right-side space
		for space in range(0, char_and_space_map[i][3]):
			minoru_str += ' '
		# print right-side character
		for char in range(0, char_and_space_map[i][4]):
			minoru_str += '#'

		minoru_str += '\n'

	minoru_str += '      ####                          ####\n'
	minoru_str += '        #####                    #####\n'
	minoru_str += '           ########        ########     TM\n'
	minoru_str += '                ##############\n'

	return minoru_str
