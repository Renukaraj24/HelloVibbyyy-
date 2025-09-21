import streamlit as st

st.set_page_config(layout="centered")
st.image("tkub.png", use_container_width=True)
# --- Custom CSS for basic styling (optional, but helps with visual resemblance) ---
st.markdown("""
<style>
    .reportview-container .main .block-container{
        max-width: 700px;
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
    }
    .stToggle>label>div:nth-child(1) {
        width: 40px !important;
        height: 50px !important;
        background-color: #e9a8cd;
        border-radius: 10px;
        position: relative;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .stToggle>label>div:nth-child(1)::after {
        content: '';
        position: absolute;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: #e9a8cd;
        top: 2px;
        left: 2px;
        transition: left 0.2s;
    }
    .stToggle>label>div:nth-child(1)[data-checked="true"] {
        background-color: #e9a8cd; /* Light pink for checked state */
    }
    .stToggle>label>div:nth-child(1)[data-checked="true"]::after {
        left: 22px;
        background-color: #fff;
    }
    .stToggle>label>div:nth-child(2) {
        margin-left: 10px;
        font-size: 1rem;
        background-color: #e9a8cd;
    }
    .stMarkdown h3 {
        text-align: center;
        color: #e9a8cd; /* Hot pink for the title */
        font-family: 'Brush Script MT', cursive; /* Example of a script font, may not render on all systems */
        font-size: 3em;
        margin-bottom: 20px;
    }
    .question-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
        padding: 5px 0;
    }
    .question-item {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: flex-end; /* Align text to the right for the first item, left for the second */
        padding: 0 10px;
    }
    .question-item.left {
        justify-content: flex-start;
        text-align: right;
    }
    .question-item.right {
        justify-content: flex-end;
        text-align: left;
    }
    .stButton>button {
        background-color: #e9a8cd ;
        color: white;
        border-radius: 20px;
        padding: 10px 30px;
        border: none;
        font-size: 1.2em;
        margin-top: 30px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- Title ---
# st.markdown("<h3>To Know You Better</h3>", unsafe_allow_html=True)

# --- Define your questions ---
questions = [
    ("Introvert", "Extrovert"),
    ("Long Walk", "Run"),
    ("Coffee", "Tea"),
    ("Listen to music", "Read a Book"),
    ("Indoor", "Outdoor"),
    ("Cook at Home", "Order from hotel"),
    ("Movie Night", "Game Night"),
    ("Drawing", "Painting"),
    ("Like pets", "Like plants"),
    ("Adventure", "Alone time"),
    ("Travelling", "Dance"),
    ("Photography", "Solo trip"),
    ("Family time fav", "Spend time with bestie"),
    ("Gang Leader", "Audience"),
]

# --- Create a dictionary to store toggle states ---
user_choices = {}

# --- Layout the toggles in two columns ---
for i in range(len(questions)):
    col1, col2 = st.columns(2)
    
    with col1:
        # Streamlit's st.toggle expects a label on the right by default.
        # We simulate the left-aligned text by making the toggle control appear first.
        # For the left options, we want the text to be associated with the toggle.
        # The key is crucial for Streamlit to manage the state of each toggle.
        user_choices[questions[i][0]] = st.toggle(questions[i][0], key=f"toggle_{questions[i][0]}")

    with col2:
        user_choices[questions[i][1]] = st.toggle(questions[i][1], key=f"toggle_{questions[i][1]}")


# --- Save Button ---
if st.button("Save"):
    st.write("Your choices have been saved!")
    st.json(user_choices) # Display choices for demonstration