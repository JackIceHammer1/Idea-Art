# Mood Shape Generator

## Description

The Mood Shape Generator is a Python application that generates a unique shape, color, and size based on the user's mood and characteristics. The application uses natural language processing (NLP) to analyze the user's input and determine the appropriate visual representation. The shapes are displayed with a background color and can be revisited from a menu.

## Features

- Text analysis using TextBlob and spaCy for sentiment analysis.
- Generates shapes such as triangles, stars, squares, circles, ellipses, pentagons, diamonds, hexagons, and rectangles.
- Determines shape color based on sentiment polarity.
- Adjusts shape size based on the strength of the sentiment.
- Displays shapes with a random background color (different from the shape color).
- Allows users to revisit previous drawings from a menu.
- Professional and user-friendly interface using `tkinter` and `ttk` widgets.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `matplotlib` (`pip install matplotlib`)
- `textblob` (`pip install textblob`)
- `spacy` (`pip install spacy`)
- spaCy English model (`python -m spacy download en_core_web_sm`)
- `numpy` (`pip install numpy`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/mood-shape-generator.git
    cd mood-shape-generator
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Enter your mood and characteristics when prompted.

3. A shape representing your mood will be displayed in a new window.

4. To generate a new shape, click the "Generate Shape" button again.

5. To revisit previous drawings, use the "File" menu and select "Open Previous Drawing".

## File Structure

- `main.py`: Main script to run the application.
- `README.md`: This file.
- `requirements.txt`: List of required Python packages.

## Future Enhancements

- Improve text analysis with more advanced NLP techniques.
- Add more shapes and colors.
- Save generated shapes as image files.
- Allow users to customize shape generation parameters.