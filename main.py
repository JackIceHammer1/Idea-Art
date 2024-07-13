from textblob import TextBlob

def generate_color_shape_size():
    user_text = input("Describe your mood and characteristics: ").lower()

    # Analyze sentiment using TextBlob
    blob = TextBlob(user_text)
    sentiment = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)
    subjectivity = blob.sentiment.subjectivity  # Get sentiment subjectivity (0 to 1)

    # Determine color based on sentiment polarity
    if sentiment > 0.75:
        color = 'yellow'
    elif sentiment > 0.5:
        color = 'orange'
    elif sentiment > 0.25:
        color = 'light green'
    elif sentiment > 0:
        color = 'green'
    elif sentiment > -0.25:
        color = 'light blue'
    elif sentiment > -0.5:
        color = 'blue'
    elif sentiment > -0.75:
        color = 'purple'
    else:
        color = 'dark blue'

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
        size = 'large'
    elif abs(sentiment) > 0.5:
        size = 'medium'
    else:
        size = 'small'

    # Print the generated color, shape, and size
    print(f"Based on your description,")
    print(f"Your generated color is: {color}")
    print(f"Your generated shape is: {shape}")
    print(f"Your generated size is: {size}")

# Calling the function to generate color, shape, and size based on user input
generate_color_shape_size()
