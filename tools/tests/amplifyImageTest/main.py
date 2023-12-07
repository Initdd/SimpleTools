
from PIL import Image
import argparse
import sys
import unittest
import os


sys.path.insert(0, '../../')
from amplifyImage import *

class TestAmplifyImage(unittest.TestCase):

    def test_amplify_image(self):
        # Input and output paths for testing
        input_path = "testLogo.png"
        output_path = "testLogo_res.png"
        factor = 2.0

        # Create a small test image
        self.create_test_image(input_path)

        # Call the amplify_image function
        amplify_image(input_path, output_path, factor)

        # Check if the output image exists
        self.assertTrue(os.path.exists(output_path))

        # Clean up: Remove the test images
        #os.remove(input_path)
        #os.remove(output_path)

    def create_test_image(self, file_path):
        # Create a small test image for testing
        from PIL import Image
        img = Image.new("RGB", (100, 100), "white")
        img.save(file_path)

if __name__ == '__main__':
    unittest.main()

