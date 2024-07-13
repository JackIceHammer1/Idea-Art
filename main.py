from textblob import TextBlob

def generate_color_and_shape():
    user_text = input("Describe your mood and characteristics: ").lower()

    # Analyze sentiment using TextBlob
    blob = TextBlob(user_text)
    sentiment = blob.sentiment.polarity  # Get sentiment polarity (-1 to 1)

    # Determine color based on sentiment polarity
    if sentiment > 0.5:
        color = 'yellow'
    elif sentiment > 0:
        color = 'green'
    elif sentiment < -0.5:
        color = 'blue'
    elif sentiment < 0:
        color = 'gray'
    else:
        color = 'white'  # Default color if sentiment is neutral

    # Determine shape based on characteristics in the text
    characteristics = ['energetic', 'gentle', 'strong', 'soft', 'creative']
    shape = 'unknown'  # Default shape if no characteristics match
    for char in characteristics:
        if char in user_text:
            shape = char + ' shape'
            break  # Exit loop on first match

    # Print the generated color and shape
    print(f"Based on your description,")
    print(f"Your generated color is: {color}")
    print(f"Your generated shape is: {shape}")

# Calling the function to generate color and shape based on user input
generate_color_and_shape()
