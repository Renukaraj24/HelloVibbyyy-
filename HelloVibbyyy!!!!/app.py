import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Vibby's Wellness App",
    page_icon="🌸", # You can choose a different emoji
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.image("hellovibbylogo.png", use_container_width=True)
# --- Custom CSS for Styling ---
# This CSS attempts to mimic the look from your image
st.markdown("""
<style>
    .reportview-container {
        background: #ffffff; # White background for the app
    }
    .main .block-container {
        padding-top: 2rem; # Adjust top padding
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
        max-width: 700px; # Adjust max-width if needed
    }
    .stImage {
        text-align: center; # Center the image
        margin-bottom: 20px;
    }
    .custom-banner {
        background-color: #f7e6f8; /* Light pink background for the banner */
        border-radius: 15px; /* Slightly rounded corners */
        padding: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    .custom-banner h1 {
        font-family: 'Brush Script MT', cursive; /* Example script font, might not be available on all systems */
        color: #5d3a5e; /* Darker purple/pink for text */
        font-size: 3em; /* Larger font size */
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .custom-banner p {
        font-family: 'Arial', sans-serif;
        color: #8c6a8d; /* A lighter shade for the subtitle */
        font-size: 1.1em;
        margin-top: 0;
    }
    .placeholder-bar-pink {
        background-color: #f7e6f8; /* Same as banner pink */
        height: 30px;
        width: 80%; /* Adjust width as needed */
        margin: 15px auto; /* Center it with auto margins */
        border-radius: 10px;
    }
    .placeholder-bar-grey {
        background-color: #f0f0f0; /* Light grey */
        height: 20px;
        width: 60%; /* Adjust width as needed */
        margin: 15px auto; /* Center it */
        border-radius: 10px;
    }
    /* Streamlit's default elements might need adjustment if you want a cleaner look */
    /* For example, hiding the default Streamlit header and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# --- Main Content ---

# Optional: You can put your main logo here.
# Make sure 'your_logo.png' is in the same directory as your Python script,
# or provide the full path to the image.
# st.image("your_logo.png", use_column_width=True) # Uncomment and replace "your_logo.png"

# Placeholder for your banner content
# st.markdown(f"""
# <div class="custom-banner">
#     <h1>Unlocked mental wellness solution</h1>
    
# </div>
# """, unsafe_allow_html=True)

# Placeholder bars
st.markdown('<div class="placeholder-bar-pink"></div>', unsafe_allow_html=True)
st.markdown('<div class="placeholder-bar-grey"></div>', unsafe_allow_html=True)
st.markdown('<div class="placeholder-bar-pink" style="width: 70%;"></div>', unsafe_allow_html=True) # Another one, slightly different width