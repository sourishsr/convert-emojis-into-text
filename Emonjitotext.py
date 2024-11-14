import emoji

def convert_emoji_to_text(text):
    return emoji.demojize(text)

# Example usage
text_with_emoji = "I love 🐍 and 💻!"
text_without_emoji = convert_emoji_to_text(text_with_emoji)

print("Original Text:", text_with_emoji)
print("Converted Text:", text_without_emoji)
