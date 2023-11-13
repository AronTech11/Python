# # Name = Taluba Aron Hopson
# # Student ID = 101747537

from PIL import Image

class ImageProcessor:
    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def display_image_dimensions(self):
        width, height = self.image.size
        print(f"Image width: {width} pixels")
        print(f"Image height: {height} pixels")

    def process_channels_and_display(self):
        r, g, b = self.image.split()
        grey_image = Image.new('L', self.image.size)
        grey_image.paste(r)

        width, height = self.image.size
        composite_image = Image.new('RGB', (width * 2, height *2))
        composite_image.paste(self.image, (0, 0))
        composite_image.paste(r, (width, 0))
        composite_image.paste(g, (0, height))
        composite_image.paste(b, (width, height))

        # Display the composite image
        composite_image.show()

        # Display the red channel (grayscale image)
        grey_image.show()

def main():
    # Specify the image file path
    image_path = 'img.jpg'

    # Create an ImageProcessor instance and process the image
    processor = ImageProcessor(image_path)

    # Display image dimensions and process channels
    processor.display_image_dimensions()
    processor.process_channels_and_display()

if __name__ == "__main__":
    main()
