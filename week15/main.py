from PIL import Image, ImageDraw, ImageFont

with Image.open("./NCNU.jpg") as image:
    fonts = [
        ImageFont.truetype("./font01.ttf", size=18),
        ImageFont.truetype("./font02.ttf", size=22),
    ]
    messages = ["謝禹沆", "111213515"]
    width, height = image.size
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), messages[0], font=fonts[0])
    draw.text(
        ((width - w) / 2, (height - h) / 2 + 15),
        messages[0],
        font=fonts[0],
        fill="black",
    )
    _, _, w, h = draw.textbbox((0, 0), messages[1], font=fonts[1])
    draw.text(
        ((width - w) / 2, (height - h) / 2 - 15),
        messages[1],
        font=fonts[1],
        fill="black",
    )

    image.save("111213515_謝禹沆.jpg", "JPEG")
