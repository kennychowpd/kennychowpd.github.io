import sys
from PIL import Image, ImageOps


if len(sys.argv) != 3:
    sys.exit()

portrait = Image.open(sys.argv[1])
shirt = Image.open("shirt.png")


portrait = ImageOps.fit(portrait, (600, 600), bleed=0.10, centering=(0.5, 0.8))

portrait.paste(shirt, shirt)

portrait.save(sys.argv[2])
