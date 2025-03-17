# Advanced NLP & Image Processing System

A comprehensive desktop application integrating Natural Language Processing (NLP) and Image Processing features into a single professional GUI. This project leverages powerful libraries such as OpenCV, PyTesseract, NLTK, and Sumy, providing robust tools for OCR, image manipulation, text summarization, sentiment analysis, and document management.

## Features

- **Optical Character Recognition (OCR):** Extract text from images using PyTesseract.
- **Image Processing Tools:** Apply grayscale, thresholding, and resizing operations on images using OpenCV.
- **Watermarking:** Easily add customizable text watermarks to images with adjustable font size, color, and position.
- **NLP Tools:** 
  - **Summarization:** Generate concise summaries using the LSA algorithm from Sumy.
  - **Sentiment Analysis:** Analyze the sentiment of text using NLTK's VADER.
- **Document Management:** Store, update, and delete documents with summaries and sentiment results in an SQLite database.
- **Logging System:** Track application events and operations with a built-in logger.
- **Customizable Settings:** Adjust camera index and OCR language via a dedicated settings panel.
- **Professional GUI:** An interactive and user-friendly interface built with PyQt5, featuring smooth animations and modern styling.

## Requirements

- Python 3.6+
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [PyTesseract](https://pypi.org/project/pytesseract/)
- [NLTK](https://www.nltk.org/)
- [Sumy](https://pypi.org/project/sumy/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/advanced-nlp-image-processing.git
   cd advanced-nlp-image-processing

    Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

If a requirements.txt file is not provided, install packages manually:

    pip install opencv-python pytesseract nltk sumy PyQt5 Pillow

    Download NLTK Data:

    The application downloads the necessary NLTK data (e.g., punkt, vader_lexicon) on startup. Ensure that your environment has internet access for the initial run.

Usage

Run the application by executing the main script:

python main.py

Upon launch, a splash screen will display briefly before opening the main interface. Navigate through the tabs to access various functionalities such as document input, image processing, watermarking, NLP tools, and document management.
Project Structure

    main.py – Entry point of the application.
    config_nlp.json – Configuration file to store user settings.
    nlp_image.db – SQLite database file for storing documents.
    Other modules include classes for OCR, image processing, NLP processing, UI components, and logging.

Contributing

Contributions are welcome. Feel free to fork the repository and submit pull requests with improvements or bug fixes. Please ensure your contributions adhere to the project’s coding style and pass all tests.
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements

    OpenCV
    PyTesseract
    NLTK
    Sumy
    PyQt5
    Pillow
