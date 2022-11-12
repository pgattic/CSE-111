# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
	draw_circle_with_vert_grad, start_drawing, draw_line, draw_oval, draw_arc, \
	draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
	# Width and height of the scene in pixels
	scene_width = 800
	scene_height = 500

	# Call the start_drawing function in the draw2d.py
	# library which will open a window and create a canvas.
	canvas = start_drawing("Scene", scene_width, scene_height)

	# Call your drawing functions such
	# as draw_sky and draw_ground here.

	draw_sky(canvas, scene_width, scene_height)
	draw_ground(canvas, scene_width, scene_height)

	# Call the finish_drawing function
	# in the draw2d.py library.
	finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(ctx, canvas_width, canvas_height):
	draw_rectangle(ctx, 0, 0, canvas_width, canvas_height, fill="#66f")
	draw_sun(ctx, canvas_width, canvas_height)
	draw_clouds(ctx, canvas_width, canvas_height)
	# draw_bird(ctx, canvas_width, canvas_height)


def draw_ground(ctx, canvas_width, canvas_height):
	draw_rectangle(ctx, 0, 0, canvas_width, canvas_height/4, fill="#3b3")
	draw_trees(ctx, canvas_width, canvas_height)
	draw_grass(ctx, canvas_width, canvas_height, canvas_height/4 - 16)
	draw_fence(ctx, canvas_width, canvas_height)
	for i in range(0, int((canvas_height/4) / 12)):
		draw_grass(ctx, canvas_width, canvas_height, canvas_height/4 - (i * 12) - 24)
	draw_grass(ctx, canvas_width, canvas_height, 0)


def draw_sun(ctx, canvas_width, canvas_height):
	draw_circle_with_vert_grad(ctx, canvas_width - 64, canvas_height - 64, 36, [255, 255, 255], [255, 255, 64])

def draw_clouds(ctx, canvas_width, canvas_height):
	draw_circle_with_vert_grad(ctx, 128, canvas_height - 128, 36, [255, 255, 255], [255, 255, 255])
	draw_circle_with_vert_grad(ctx, 88,  canvas_height - 128, 30, [255, 255, 255], [255, 255, 255])
	draw_circle_with_vert_grad(ctx, 168, canvas_height - 128, 33, [255, 255, 255], [255, 255, 255])

	draw_circle_with_vert_grad(ctx, 556, canvas_height - 150, 48, [255, 255, 255], [255, 255, 255])
	draw_circle_with_vert_grad(ctx, 516, canvas_height - 150, 40, [255, 255, 255], [255, 255, 255])
	draw_circle_with_vert_grad(ctx, 596, canvas_height - 150, 44, [255, 255, 255], [255, 255, 255])


def draw_trees(ctx, canvas_width, canvas_height):
	draw_rectangle(ctx, 690, 110, 710, 200, fill="#962")
	draw_polygon(ctx, 600, 150, 800, 150, 700, 400, fill="#5b5")
	draw_rectangle(ctx, 590, 115, 610, 200, fill="#962")
	draw_polygon(ctx, 530, 130, 670, 130, 600, 300, fill="#5b5")
	pass

def draw_fence(ctx, canvas_width, canvas_height):
	fence_width = 24
	fence_gap = 8
	fence_spacing = fence_width + fence_gap
	for i in range(0, int(canvas_width / fence_spacing + 1)):
		draw_rectangle(ctx, i * fence_spacing, 100, i * fence_spacing + fence_width, 200, fill="#b73")

def draw_grass(ctx, canvas_width, canvas_height, base):
	grass_width = 6
	grass_height_min = 12
	grass_height_max = 48
	for i in range(0, int(canvas_width / grass_width) + 1):
		draw_polygon(ctx, i * grass_width, base, i * grass_width + grass_width, base, i * grass_width + (grass_width / 2), base + random.randint(grass_height_min, grass_height_max), fill="#484")
		pass
	pass

# Call the main function so that
# this program will start executing.
main()
