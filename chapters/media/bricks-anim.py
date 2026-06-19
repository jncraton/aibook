from PIL import Image, ImageDraw, ImageFont, ImageOps
from collections import deque
import os

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

INPUT_FILE = "bricks-anim-input.xbm"
OUTPUT_DIR = "frames"

SCALE = 8

# 4-connected neighborhood
NEIGHBORS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

# Colors for discovered connected components
COLORS = [
    (255, 0, 0),
    (0, 180, 0),
    (0, 0, 255),
    (255, 140, 0),
    (180, 0, 180),
    (0, 180, 180),
    (180, 120, 0),
]

# ------------------------------------------------------------
# Load XBM
#
# After inversion:
#     White = background
#     Black = foreground objects
# ------------------------------------------------------------

img = Image.open(INPUT_FILE).convert("L")
img = ImageOps.invert(img)
img = img.convert("1")

WIDTH, HEIGHT = img.size

font = ImageFont.load_default()

visited = [[False] * WIDTH for _ in range(HEIGHT)]

component_pixels = {}
labels = []

frame = 0
component = 0

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------


def draw_frame(cursor=None):
    global frame

    canvas = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(canvas)

    #
    # Draw image
    #

    for y in range(HEIGHT):
        for x in range(WIDTH):

            # foreground pixels are BLACK after inversion
            if img.getpixel((x, y)) == 0:

                color = component_pixels.get((x, y), (0, 0, 0))
                draw.point((x, y), fill=color)

    #
    # Draw labels
    #

    for label, lx, ly in labels:
        draw.text((lx, ly), str(label), fill="black", font=font)

    #
    # Draw scan cursor
    #

    if cursor is not None:
        x, y = cursor
        draw.rectangle((x - 1, y - 1, x + 1, y + 1), outline="red")

    #
    # Scale image
    #

    canvas = canvas.resize(
        (WIDTH * SCALE, HEIGHT * SCALE),
        Image.NEAREST,
    )

    canvas.save(
        os.path.join(
            OUTPUT_DIR,
            f"frame_{frame:04d}.png"
        )
    )

    frame += 1


# ------------------------------------------------------------
# Raster scan
# ------------------------------------------------------------

for y in range(HEIGHT):

    for x in range(WIDTH):

        draw_frame((x, y))

        if visited[y][x]:
            continue

        visited[y][x] = True

        #
        # Skip white background
        #

        if img.getpixel((x, y)) != 0:
            continue

        #
        # New connected component
        #

        component += 1
        color = COLORS[(component - 1) % len(COLORS)]

        queue = deque([(x, y)])
        pixels = []

        while queue:

            px, py = queue.popleft()

            #
            # Ignore background
            #

            if img.getpixel((px, py)) != 0:
                continue

            pixels.append((px, py))
            component_pixels[(px, py)] = color

            draw_frame((px, py))

            for dx, dy in NEIGHBORS:

                nx = px + dx
                ny = py + dy

                if nx < 0 or ny < 0:
                    continue

                if nx >= WIDTH or ny >= HEIGHT:
                    continue

                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True

                if img.getpixel((nx, ny)) == 0:
                    queue.append((nx, ny))

        #
        # Place component label near centroid
        #

        cx = sum(p[0] for p in pixels) // len(pixels)
        cy = sum(p[1] for p in pixels) // len(pixels)

        labels.append((component, cx - 2, cy - 3))

        draw_frame()

print(f"Wrote {frame} frames to '{OUTPUT_DIR}'.")