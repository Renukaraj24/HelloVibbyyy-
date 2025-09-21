import streamlit as st
import base64
from pathlib import Path
st.image("todonow.png", use_container_width=True)
# Helper to load an image and encode it to base64
def img_to_base64(image_path):
    img_bytes = Path(image_path).read_bytes()
    return base64.b64encode(img_bytes).decode()

# --- Custom CSS for layout and style ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
    .header-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 60%%;
        margin-bottom: -26px;
    }
    .activity-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px 24px;
        justify-items: center;
        margin: 0 auto 20px auto;
        width: 260px;
    }
    .activity-cell {
        display: flex;
        flex-direction: column;
        align-items: center;
        background: #fff;
        border-radius: 16px;
        width: 120px;
        padding: 10px 7px 13px 7px;
        box-shadow: 0 3px 22px rgba(191,151,197,0.11);
    }
    .activity-img {
        width: 65px;
        height: 65px;
        object-fit: contain;
        margin-bottom: 6px;
        margin-top: 2px;
    }
    .activity-name {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.02em;
        color: #6a0572;
        text-align: center;
        margin-bottom: 2px;
        margin-top: 2px;
        line-height: 1.15em;
    }
    .main-header {
        text-align: center;
        font-family: 'Pacifico', cursive;
        font-size: 2.2em;
        color: #222;
        letter-spacing: 0.5px;
        background: none;
        margin-bottom: 6px;
        margin-top: 21px;
    }
    .next-btn {
        background-color: #e9a8cd;
        color: white;
        font-size: 1.30em;
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 13px;
        border: none;
        width: 75%%;
        margin-top: 33px;
        margin-bottom: 13px;
        cursor: pointer;
        transition: background-color 0.3s;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .next-btn:hover {
        background-color: #e087bd;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
# st.markdown(
#     "<div class='main-header'>What do you like to do now????</div>",
#     unsafe_allow_html=True
# )

# --- Activity/option grid ---
activities = [
    {'label': 'Story Time', 'image': 'storytime.png'},
    {'label': 'Best quotes', 'image': 'bestquote.png'},
    {'label': 'Chatbot', 'image': 'chatbot.png'},
    {'label': 'Movie clips', 'image': 'movieclip.png'},
    {'label': 'Tracker and Streaks', 'image': 'tracksnstreaks.png'},
    {'label': 'Meditation', 'image': 'meditation.png'}
]

# Add the base64 image string to each activity
for activity in activities:
    activity['image_base64'] = img_to_base64(activity['image'])

st.markdown("<div class='activity-grid'>", unsafe_allow_html=True)
for item in activities:
    st.markdown(
        f"""
        <div class='activity-cell'>
            <img class='activity-img' src='data:image/png;base64,{item['image_base64']}' />
            <div class='activity-name'>{item['label']}</div>
        </div>
        """, unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)

# --- Next button centered ---
st.markdown(
    "<button class='next-btn'>Next</button>",
    unsafe_allow_html=True
)
