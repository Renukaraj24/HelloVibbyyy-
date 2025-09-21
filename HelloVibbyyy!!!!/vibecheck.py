import streamlit as st

# --- Page Configuration ---
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
st.image("vibecheck.png", use_container_width=True)
# --- Custom CSS for Styling ---
st.markdown("""
<style>
    /* Main body background and font */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f8f8;
    }

    /* Center content on the page */
    .stApp {
        max-width: 600px;
        margin: auto;
        padding-top: 20px;
    }

    /* Header styling for "Vibe Check??" */
    .vibe-header {
        text-align: center;
        margin-bottom: 40px;
        position: relative;
    }
    .vibe-header h1 {
        font-family: 'Brush Script MT', cursive;
        font-size: 3.5em;
        color: #333;
        margin-top: 20px;
        z-index: 2;
        position: relative;
    }
    .vibe-header .splash {
        position: absolute;
        top: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 300px;
        height: 100px;
        background: url("https://i.imgur.com/your-pink-splash-image.png") no-repeat center center;
        background-size: contain;
        z-index: 1;
        opacity: 0.8;
    }
    .vibe-header .splash::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        background-color: #f7e0e7;
        border-radius: 50% 50% 30% 30%;
        transform: rotate(3deg);
        filter: blur(10px);
    }

    /* Emoji button container grid */
    .emoji-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        justify-items: center;
        align-items: center;
        margin-bottom: 50px;
    }

    /* Style the Streamlit buttons to look like emoji cards */
    .stButton>button {
        background: none;
        border: none;
        padding: 0;
        cursor: pointer;
    }

    .emoji-card {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .emoji-card img {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: contain;
        margin-bottom: 5px;
    }

    .emoji-card span {
        background-color: #e0e0e0;
        border-radius: 5px;
        padding: 5px 10px;
        font-size: 0.9em;
        color: #555;
        white-space: nowrap;
    }

    /* Selected state */
    .emoji-card.selected img {
        border: 2px solid #f0a8c2;
    }
    .emoji-card.selected span {
        background-color: #fcdfe8;
        font-weight: bold;
        border: 1px solid #f0a8c2;
    }

    /* Next button styling */
    .next-button {
        text-align: center;
        margin-top: 30px;
    }
    .stButton>button.next-btn {
        background-color: #e6a8c2;
        color: white;
        padding: 12px 40px;
        border-radius: 10px;
        border: none;
        font-size: 1.2em;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.2s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton>button.next-btn:hover {
        background-color: #d18fae;
    }
</style>
""", unsafe_allow_html=True)

# --- Emoji Data with OpenMoji CDN ---
emoji_data = {
    "Happy": "https://emojicdn.elk.sh/😊",
    "Cry": "https://emojicdn.elk.sh/😢",
    "Exhaust": "https://emojicdn.elk.sh/😩",
    "Stress": "https://emojicdn.elk.sh/😫",
    "Angry": "https://emojicdn.elk.sh/😡",
    "Shock": "https://emojicdn.elk.sh/😱",
    "Fever": "https://emojicdn.elk.sh/🤒",
    "Sleepy": "https://emojicdn.elk.sh/😴",
    "Hungry": "https://emojicdn.elk.sh/😋",
    "Sad": "https://emojicdn.elk.sh/😞",
    "Excite": "https://emojicdn.elk.sh/🥳",
    "Frustrate": "https://emojicdn.elk.sh/😖",
    "Silence": "https://emojicdn.elk.sh/🤐",
    "Confuse": "https://emojicdn.elk.sh/😕",
    "Relax": "https://emojicdn.elk.sh/😌",
    "Worry": "https://emojicdn.elk.sh/😟",
}


# --- Session State Initialization ---
if 'selected_emojis' not in st.session_state:
    st.session_state.selected_emojis = []

# --- Header ---
# st.markdown(f"""
# <div class="vibe-header">
#     <div class="splash"></div>
#     <h1>Vibe Check??</h1>
# </div>
# """, unsafe_allow_html=True)

# --- Emoji Grid ---
st.markdown('<div class="emoji-grid">', unsafe_allow_html=True)
cols = st.columns(4)

for i, (vibe, img_url) in enumerate(emoji_data.items()):
    with cols[i % 4]:
        is_selected = vibe in st.session_state.selected_emojis
        selected_class = "selected" if is_selected else ""

        # Plain button (no unsafe_allow_html)
        if st.button(vibe, key=f"emoji_btn_{vibe}"):
            if is_selected:
                st.session_state.selected_emojis.remove(vibe)
            else:
                st.session_state.selected_emojis.append(vibe)
            st.rerun()

        # Render emoji card below the button (CSS styled)
        st.markdown(f"""
        <div class="emoji-card {selected_class}">
            <img src="{img_url}" />
            <span>{vibe}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Next Button ---
st.markdown('<div class="next-button">', unsafe_allow_html=True)
if st.button("Next", key="next_button", help="Proceed to next", type="primary"):
    if st.session_state.selected_emojis:
        st.success(f"You selected: {', '.join(st.session_state.selected_emojis)}")
        st.write("Selected emojis will be remembered for the next step.")
    else:
        st.warning("Please select at least one emoji before proceeding.")
st.markdown('</div>', unsafe_allow_html=True) 