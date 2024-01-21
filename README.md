# Amplify Tools

This Tkinter-based GUI application providing simple tools for
people not that used to technology, like your grandparents 😉


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Installation

1. Install Python 3 on your machine. You can download it from the official website:
    https://www.python.org/downloads/

3. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Initdd/SimpleTools.git
    ```

4. Navigate to the project directory:

    ```bash
    cd SimpleTools
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    May not work on Linux. If so, try to install the dependencies manually.

    Some dependencies are omitted, as they are already included in the Python standard library.


## Usage

1. Run the application by executing the following command:

    * On Windows:

    ```bash
    python main.py 
    # or
    py main.py
    ```

    * On Linux:
    
    ```bash
    python3 main.py
    ```

    The app will launch, providing a simple menu for the diferent functions

## Features

* Resize Font in Word Document:  
    - Select a Word document (.docx) or (.doc).
    - Specify the resizing factor.
    - Click the Submit button to resize the font in the document.

* Amplify Image:  
    - Choose an image file (*.png, *.jpg, *.jpeg, *.gif).
    - Set the resizing factor.  
    - Click the Submit to amplify the image.

* Multi-Language Support:  
    - The application supports multiple languages, and strings can be easily customized.

## Dependencies

The app relies on the following tools and libraries:

* Tkinter: The standard GUI toolkit for Python.
* json: Standard JSON library for Python.
* Pillow: Python Imaging Library (PIL).
* python-docx: Python library for creating and updating Microsoft Word (.docx) files.

## Contributing

I welcome contributions that enhance functionality, fix issues, or improve the overall quality of the application.

