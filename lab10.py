from PIL import Image

# Open an image file
image = Image.open('img.jpg')

# Access the red channel using split
r, g, b = image.split()

# You can also create a blank "R" image if you only need the red channel
r_channel = Image.new('L', image.size)
r_channel.paste(r)


# Display the original image
image.show()
# Display the red channel (grayscale image)
r_channel.show()
