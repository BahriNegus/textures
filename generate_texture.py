from PIL import Image, ImageDraw
import random

# Constants
WIDTH = 2048
HEIGHT = 2048
TILE_SIZE = 256
FURROW_WIDTH = 10
FURROW_COLOR = (139, 69, 19)

# Create a new image with a white background
image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))

draw = ImageDraw.Draw(image)

# Create the field pattern
for y in range(0, HEIGHT, TILE_SIZE):
    for x in range(0, WIDTH, TILE_SIZE):
        # Randomly determine the color variation for the tile
        grass_color = (34 + random.randint(-10, 10), 139 + random.randint(-10, 10), 34 + random.randint(-10, 10))
        draw.rectangle([x, y, x + TILE_SIZE, y + TILE_SIZE], fill=grass_color)
        
        # Draw furrows
        for furrow in range(0, TILE_SIZE, 50):
            if random.random() < 0.5:  # Random furrow placement
                draw.line([x + furrow, y, x + furrow, y + TILE_SIZE], fill=FURROW_COLOR, width=FURROW_WIDTH)
                draw.line([x, y + furrow, x + TILE_SIZE, y + furrow], fill=FURROW_COLOR, width=FURROW_WIDTH)

# Save the texture image
image.save("medieval_field.png")