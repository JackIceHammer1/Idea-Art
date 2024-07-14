import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle, Ellipse, Polygon, Rectangle
from transformers import pipeline
import numpy as np

# Load sentiment analysis pipeline from transformers
sentiment_analysis = pipeline('sentiment-analysis')

def analyze_text_and_generate_shape(text):
    # Analyze sentiment using transformers
    result = sentiment_analysis(text)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        sentiment = score
    else:
        sentiment = -score

    # Determine color based on sentiment polarity
    if sentiment > 0.75:
        color = '#FFFF00'  # yellow
    elif sentiment > 0.5:
        color = '#FFA500'  # orange
    elif sentiment > 0.25:
        color = '#90EE90'  # light green
    elif sentiment > 0:
        color = '#008000'  # green
    elif sentiment > -0.25:
        color = '#ADD8E6'  # light blue
    elif sentiment > -0.5:
        color = '#0000FF'  # blue
    elif sentiment > -0.75:
        color = '#800080'  # purple
    else:
        color = '#00008B'  # dark blue

    # Determine shape based on sentiment score
    if sentiment > 0.75:
        shape = 'star'
    elif sentiment > 0.5:
        shape = 'hexagon'
    elif sentiment > 0.25:
        shape = 'pentagon'
    elif sentiment > 0:
        shape = 'triangle'
    elif sentiment > -0.25:
        shape = 'square'
    elif sentiment > -0.5:
        shape = 'diamond'
    elif sentiment > -0.75:
        shape = 'ellipse'
    else:
        shape = 'circle'

    # Determine size based on the absolute value of sentiment polarity
    if abs(sentiment) > 0.75:
        size = 3
    elif abs(sentiment) > 0.5:
        size = 2
    else:
        size = 1

    return color, shape, size

def draw_shape(color, shape, size):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    if shape == 'triangle':
        polygon = RegularPolygon((0.5, 0.5), numVertices=3, radius=size*0.1, color=color)
    elif shape == 'star':
        polygon = RegularPolygon((0.5, 0.5), numVertices=5, radius=size*0.1, color=color, orientation=np.pi/10)
    elif shape == 'square':
        polygon = RegularPolygon((0.5, 0.5), numVertices=4, radius=size*0.1, color=color)
    elif shape == 'circle':
        polygon = Circle((0.5, 0.5), radius=size*0.1, color=color)
    elif shape == 'ellipse':
        polygon = Ellipse((0.5, 0.5), width=size*0.2, height=size*0.1, color=color)
    elif shape == 'pentagon':
        polygon = RegularPolygon((0.5, 0.5), numVertices=5, radius=size*0.1, color=color)
    elif shape == 'diamond':
        polygon = RegularPolygon((0.5, 0.5), numVertices=4, radius=size*0.1, color=color, orientation=np.pi/4)
    elif shape == 'hexagon':
        polygon = RegularPolygon((0.5, 0.5), numVertices=6, radius=size*0.1, color=color)
    elif shape == 'rectangle':
        polygon = Rectangle((0.4, 0.4), width=size*0.2, height=size*0.1, color=color)
    
    ax.add_patch(polygon)
    plt.show()

def on_generate_button_click():
    text = simpledialog.askstring("Input", "Describe your mood and characteristics:")
    if text:
        color, shape, size = analyze_text_and_generate_shape(text)
        draw_shape(color, shape, size)

# Create the main window
root = tk.Tk()
root.title("Mood Shape Generator")

# Create a button to generate shape
generate_button = tk.Button(root, text="Generate Shape", command=on_generate_button_click)
generate_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
