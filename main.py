import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Circle, Ellipse, Polygon, Rectangle
from textblob import TextBlob
import numpy as np

def generate_color_shape_size():
    user_text = input("Describe your mood, or insert any text: ").lower()

    # Analyze sentiment using TextBlob
    blob = TextBlob(user_text)
    sentiment = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)
    subjectivity = blob.sentiment.subjectivity  # Get sentiment subjectivity (0 to 1)

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

    # Determine shape based on nature of the text
    if sentiment > 0.5 and subjectivity < 0.5:
        shape = 'triangle'  # Positive and objective
    elif sentiment > 0.5 and subjectivity >= 0.5:
        shape = 'star'  # Positive and subjective
    elif sentiment <= 0.5 and sentiment > 0 and subjectivity < 0.5:
        shape = 'square'  # Slightly positive and objective
    elif sentiment <= 0.5 and sentiment > 0 and subjectivity >= 0.5:
        shape = 'circle'  # Slightly positive and subjective
    elif sentiment <= 0 and sentiment > -0.5 and subjectivity < 0.5:
        shape = 'ellipse'  # Slightly negative and objective
    elif sentiment <= 0 and sentiment > -0.5 and subjectivity >= 0.5:
        shape = 'pentagon'  # Slightly negative and subjective
    elif sentiment <= -0.5 and subjectivity < 0.5:
        shape = 'diamond'  # Negative and objective
    elif sentiment <= -0.5 and subjectivity >= 0.5:
        shape = 'hexagon'  # Negative and subjective
    else:
        shape = 'rectangle'  # Neutral or unknown

    # Determine size based on the absolute value of sentiment polarity
    if abs(sentiment) > 0.75:
        size = 3
    elif abs(sentiment) > 0.5:
        size = 2
    else:
        size = 1

    # Print the generated color, shape, and size
    print(f"Based on your description,")
    print(f"Your generated color is: {color}")
    print(f"Your generated shape is: {shape}")
    print(f"Your generated size is: {size}")

    # Draw the shape with the specified color and size
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')
    
    if shape == 'triangle':
        polygon = RegularPolygon((0.5, 0.5), numVertices=3, radius=size*0.1, color=color)
    elif shape == 'star':
        polygon = RegularPolygon((0.5, 0.5), numVertices=5, radius=size*0.1, color=color)
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

# Calling the function to generate color, shape, and size based on user input
generate_color_shape_size()
