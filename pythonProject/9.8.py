# Построить правильный пятиугольник со стороной a
import math

from PIL import Image, ImageDraw

if __name__ == '__main__':
    x_center = 250
    y_center = 250
    sides = 5
    radius = 200
    coords = [
        (x_center + radius * math.cos(2 * math.pi * i / sides), y_center + radius * math.sin(2 * math.pi * i / sides))
        for i in range(1, sides + 1)]

    img = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.polygon((coords), fill="lightblue", outline=(255, 0, 0))
    img.show()
