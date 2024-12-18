from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model for text generation
caption_generator = pipeline('text-generation', model='gpt2')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Generate caption route
@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    if request.method == 'POST':
        # Get the topic from the form
        topic = request.form['topic']
        
        # Create a prompt based on the topic
        prompt = f"Write a creative Instagram caption about {topic}."
        
        # Generate a caption using the pre-trained model
        captions = caption_generator(prompt, max_length=50, num_return_sequences=1)
        
        # Extract the generated caption
        caption = captions[0]['generated_text']
        
        # Return the caption to the user
        return render_template('index.html', topic=topic, caption=caption)

if __name__ == "__main__":
    app.run(debug=True)
