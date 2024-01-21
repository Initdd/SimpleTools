
from PIL import Image
import argparse
import os

def amplify_image(input_path, output_path, factor):
    try:
        # Open the image
        img = Image.open(input_path)

        # Get the size of the original image
        width, height = img.size

        # Calculate the new size based on the amplification factor
        new_width = int(width * factor)
        new_height = int(height * factor)

        # Resize the image
        amplified_img = img.resize((new_width, new_height))

        # Save the amplified image
        _, extension = os.path.splitext(input_path)
        amplified_img.save(output_path+extension)
        return f"Image saved to {output_path}"

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Amplify an image by a factor")

    # Add arguments
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("factor", type=float, help="Amplification factor")

    # Parse arguments
    args = parser.parse_args()

    # Call the amplify_image function with the provided arguments
    amplify_image(args.input, args.output, args.factor)
