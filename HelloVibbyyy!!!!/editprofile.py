import streamlit as st
from PIL import Image
import io

# Set page config
st.set_page_config(layout="centered")
st.image("editprofile.png", use_container_width=True)

# Custom CSS for styling
st.markdown("""
    <style>
    .header-text {
        font-family: 'Brush Script MT', cursive;
        font-size: 3em;
        text-align: center;
        color: #e91e63;
        margin-bottom: 20px;
        position: relative;
    }
    .header-text::after {
        content: '';
        display: block;
        width: 80px;
        height: 15px;
        background-color: #f8bbd0;
        border-radius: 50%;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(15deg);
        z-index: -1;
    }
    .profile-pic-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }
    .profile-pic-placeholder {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background-color: #f0f0f0;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #ccc;
        font-size: 3em;
        border: 2px solid #ddd;
        overflow: hidden;
    }
    .profile-pic-placeholder img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .stTextInput label, .stSelectbox label {
        font-weight: bold;
        color: #e91e63;
        margin-bottom: 5px;
        display: block;
        text-align: center;
        font-size: 0.9em;
        text-transform: uppercase;
    }
    .stTextInput > div > div > input, .stSelectbox > div > div {
        border-radius: 20px;
        padding: 10px 15px;
        border: 1px solid #f8bbd0;
        background-color: #fdfdfd;
        color: #333;
        text-align: center;
    }
    .stButton > button {
        width: 100%;
        border-radius: 25px;
        padding: 12px 20px;
        background-color: #e9a8cd;
        font-size: 1.1em;
        font-weight: bold;
        text-transform: uppercase;
        margin-top: 15px;
    }
    .stButton > button:first-of-type {
        background-color: #e9a8cd;
        color: white;
        border: none;
    }
    .stButton > button:last-of-type {
        background-color: #e9a8cd;
        color: white;
        border: none;
    }
    .stButton > button:hover {
        opacity: 0.9;
    }
    .stFileUploader {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State Initialization ---
if 'profile_name' not in st.session_state:
    st.session_state.profile_name = "Jiah Mashaal"
if 'profile_age_range' not in st.session_state:
    st.session_state.profile_age_range = "15-29"
if 'profile_pic_bytes' not in st.session_state:
    st.session_state.profile_pic_bytes = None
if 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = False

# --- Profile Picture Display ---
st.markdown('<div class="profile-pic-container">', unsafe_allow_html=True)
if st.session_state.profile_pic_bytes:
    st.image(
        st.session_state.profile_pic_bytes,
        width=150,
        use_container_width=False,
        output_format="PNG",
        caption=""
    )
else:
    st.markdown('<div class="profile-pic-placeholder"><i class="fa fa-camera"></i></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Profile Picture Upload (only in edit mode) ---
if st.session_state.edit_mode:
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], help="Upload a new profile picture")
    if uploaded_file is not None:
        st.session_state.profile_pic_bytes = uploaded_file.read()
        st.rerun()  # ✅ Updated
else:
    if st.session_state.profile_pic_bytes is None:
        st.markdown('<div style="text-align: center; color: #aaa; margin-bottom: 20px;">Upload a profile picture</div>', unsafe_allow_html=True)

# --- Profile Fields ---
# --- Profile Fields ---
with st.form("profile_form"):
    st.markdown('<p style="text-align:center; font-weight:bold; color:#e91e63; margin-bottom: 5px;">NAME</p>', unsafe_allow_html=True)
    new_name = st.text_input("", value=st.session_state.profile_name, key="name_input", disabled=not st.session_state.edit_mode)

    st.markdown('<p style="text-align:center; font-weight:bold; color:#e91e63; margin-bottom: 5px; margin-top:20px;">AGE</p>', unsafe_allow_html=True)
    
    # ✅ Change here: use number input instead of dropdown
    new_age = st.number_input(
        "",
        min_value=1,
        max_value=120,
        value=int(st.session_state.profile_age_range) if str(st.session_state.profile_age_range).isdigit() else 18,
        key="age_input",
        disabled=not st.session_state.edit_mode
    )

    if st.form_submit_button("Save"):
        st.session_state.profile_name = new_name
        st.session_state.profile_age_range = str(new_age)  # store as string to keep session consistency
        st.session_state.edit_mode = False
        st.success("Profile saved successfully!")
        st.rerun()

# --- Edit Profile Button ---
if st.button("Edit Profile"):
    st.session_state.edit_mode = not st.session_state.edit_mode
    st.rerun()  # ✅ Updated

# --- Add Font Awesome ---
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
