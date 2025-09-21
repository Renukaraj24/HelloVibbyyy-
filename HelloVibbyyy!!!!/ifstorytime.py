import streamlit as st
from transformers import pipeline, set_seed
import random

# --- 1. Load the ML Model ---
@st.cache_resource  # Cache the model to avoid reloading on every rerun
def load_story_generator():
    # You can choose 'gpt2', 'distilgpt2', or another suitable model
    generator = pipeline('text-generation', model='distilgpt2')
    return generator

story_generator = load_story_generator()
set_seed(random.randint(0, 1000))  # Set a random seed for diverse stories

# --- 2. Streamlit UI (Matching your image) ---

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")  # ✅ fixed invalid arg

# Custom CSS for the UI - this will require careful tweaking
st.markdown("""
<style>
    /* Main app container styling */
    .stApp {
        background: white; /* Or a light pattern matching your background */
        border-radius: 25px; /* Rounded corners for the "phone" */
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        max-width: 400px; /* Phone width */
        margin: auto;
        padding: 20px;
        position: relative;
        overflow: hidden; /* To contain background elements */
        border: 1px solid #ddd; /* Subtle phone border */
    }

    /* Top bar (for time, signal - purely aesthetic for this example) */
    .header-bar {
        display: flex;
        justify-content: flex-end; /* Align icons to the right */
        font-size: 0.8em;
        color: #888;
        padding-bottom: 15px;
    }

    .header-bar span {
        margin-left: 10px;
    }

    /* Story Time Header */
    .story-time-header {
        text-align: center;
        margin-bottom: 20px;
        position: relative;
    }

    .story-time-header img {
        width: 80%; /* Adjust as needed */
        max-width: 250px;
        height: auto;
        opacity: 0.8; /* Slightly transparent like in the image */
    }

    .story-time-header h1 {
        font-family: 'Brush Script MT', cursive; /* Or a similar script font */
        font-size: 3em;
        color: #d17a94; /* Pinkish color from image */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* Description text */
    .description-text {
        text-align: center;
        font-size: 0.9em;
        color: #555;
        margin-bottom: 30px;
    }

    /* Search Box */
    .stTextInput > div > div > input {
        border-radius: 25px;
        padding: 10px 20px;
        border: 1px solid #ccc;
        box-shadow: none;
    }

    .stTextInput > label {
        display: none; /* Hide default Streamlit label */
    }

    /* Story Output */
    .story-output {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        border: 1px solid #eee;
        line-height: 1.6;
        color: #333;
    }

    /* Next Button */
    .stButton > button {
        background-color: #d17a94; /* Pinkish color */
        color: white;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 1.1em;
        border: none;
        width: 100%;
        margin-top: 30px;
        box-shadow: 0 4px 10px rgba(209, 122, 148, 0.4);
    }
    .stButton > button:hover {
        background-color: #c06b85; /* Slightly darker on hover */
    }
</style>
""", unsafe_allow_html=True)

# --- Header Bar (Aesthetic only) ---
st.markdown("""
<div class="header-bar">
    <span>9:41</span>
    <span>📶</span>
    <span>🔋</span>
</div>
""", unsafe_allow_html=True)

# --- Story Time Header ---
st.markdown(f"""
<div class="story-time-header">
    <img src="https://i.imgur.com/your-story-time-image.png" alt="Story Time" style="display:none;"> <!-- Placeholder for your image --> 
    <div style="background-color: #f7e0e7; border-radius: 20px; padding: 20px; width: 80%; margin: auto;">
        <h1 style="font-family: 'Brush Script MT', cursive; font-size: 3em; color: #d17a94;">Story Time</h1>
    </div>
</div>
""", unsafe_allow_html=True) # ✅ fixed comment syntax

st.markdown("""
<p class="description-text">
    AI powered true event based story with moral based on your current mood
</p>
""", unsafe_allow_html=True)

# --- Search Box ---
mood_input = st.text_input("Enter your mood", placeholder="Motivational, Loneliness, Joy...", label_visibility="collapsed")

# --- Story Generation Logic ---
story_placeholder = st.empty() # Create an empty placeholder for the story

if mood_input:
    # --- Generate Story ---
    prompt = f"As a compassionate therapist, I want to tell you a short story about {mood_input}. This story will have a gentle moral to help you reflect. Here it is:\n\nOnce upon a time,"
    
    with st.spinner("Crafting your story..."):
        generated_text = story_generator(
            prompt, 
            max_new_tokens=200,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.9,
            top_k=50,
            top_p=0.95
        )
        
        full_story = generated_text[0]['generated_text']
        story_content = full_story.replace(prompt, "").strip()
        
        story_placeholder.markdown(f'<div class="story-output">{story_content}</div>', unsafe_allow_html=True)
else:
    st.image("https://i.imgur.com/your-sundar-pichai-image.png") # Replace with your actual image URL
    st.markdown("""
    <div class="story-output">
        Sundar Pichai, the CEO of Google and Alphabet, grew up in a modest home in Chennai where his family didn't even own a telephone for years. Despite financial struggles, he worked hard in school and secured a place at IIT Kharagpur, later earning an opportunity to study at Stanford. With determination and focus, he joined Google and played a key role in developing Google Chrome, which became one of the world's most used browsers. Step by step, he rose through challenges to finally become the CEO of Google and later Alphabet. His journey shows that humble beginnings can never stop big dreams—hard work, patience, and perseverance can take you to unimaginable heights.
    </div>
    """, unsafe_allow_html=True)

# --- Next Button ---
st.button("Next")
