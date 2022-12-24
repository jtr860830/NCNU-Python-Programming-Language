from PIL import Image, ImageDraw, ImageFont

with Image.open("./NCNU.jpg") as image:
    name = "謝禹沆"
    sn = "111213515"
    width, height = image.size
    draw = ImageDraw.Draw(image)
    fonts = [
        ImageFont.truetype("./font01.ttf", size=18),
        ImageFont.truetype("./font02.ttf", size=22),
    ]
    _, _, w, h = draw.textbbox((0, 0), name, font=fonts[0])
    draw.text(
        ((width - w) / 2, (height - h) / 2 + 15),
        name,
        font=fonts[0],
        fill="black",
    )
    _, _, w, h = draw.textbbox((0, 0), sn, font=fonts[1])
    draw.text(
        ((width - w) / 2, (height - h) / 2 - 15),
        sn,
        font=fonts[1],
        fill="black",
    )

    image.save(f"{sn}_{name}.jpg", "JPEG")
