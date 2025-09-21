import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Create Profile",
    page_icon="📝", # Changed icon for a profile page
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.image("createprofile.png", use_container_width=True)
# --- Custom CSS for Styling ---
st.markdown("""
<style>
    .reportview-container {
        background: #ffffff; /* White background */
    }
    .main .block-container {
        padding-top: 2rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 2rem;
        max-width: 700px;
    }
    /* Hide Streamlit's default elements if you want a cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .profile-banner {
        background-color: #f7e6f8; /* Light pink background */
        border-radius: 15px; /* Slightly rounded corners */
        padding: 20px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    .profile-banner h1 {
        font-family: 'Brush Script MT', cursive; /* Script font */
        color: #5d3a5e; /* Darker purple/pink for text */
        font-size: 3em; /* Larger font size */
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .instruction-text {
        text-align: center;
        margin-bottom: 20px;
        color: #555;
        font-size: 1.1em;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 1px solid #ddd;
        padding: 10px;
        font-size: 1.1em;
        background-color: #f9f9f9; /* Light grey background for input */
        color: #333;
    }
    .stTextInput label {
        font-weight: bold;
        color: #666;
        margin-bottom: 5px;
        display: block; /* Make label a block to allow margin-bottom */
    }
    /* Style for the Streamlit button */
    .stButton > button {
        width: 100%;
        background-color: #e9a8cd; /* Pink button color */
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        border: none;
        font-size: 1.3em;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin-top: 30px; /* Space above the button */
    }
    .stButton > button:hover {
        background-color: #d18ab8; /* Slightly darker pink on hover */
    }
</style>
""", unsafe_allow_html=True)

# --- Main Content ---

# Create Profile Banner
# st.markdown(f"""
# <div class="profile-banner">
#     <h1>Create Profile</h1>
# </div>
# """, unsafe_allow_html=True)

# "New Register?" instruction
st.markdown('<p class="instruction-text">New Register?</p>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("create_profile_form"):
    st.write("") # Add a little space

    # Email Input
    email = st.text_input("EMAIL", placeholder="hello@reallygreatsite.com", label_visibility="collapsed")
    st.markdown('<label style="font-weight: bold; color: #666; margin-bottom: 5px; display: block;">EMAIL</label>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top: -30px;"></div>', unsafe_allow_html=True) # Adjust position if needed

    # Password Input
    st.write("") # Add a little space
    password = st.text_input("PASSWORD", type="password", placeholder="****", label_visibility="collapsed")
    st.markdown('<label style="font-weight: bold; color: #666; margin-bottom: 5px; display: block;">PASSWORD</label>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top: -30px;"></div>', unsafe_allow_html=True) # Adjust position if needed

    # Confirm Password Input
    st.write("") # Add a little space
    confirm_password = st.text_input("CONFIRM PASSWORD", type="password", placeholder="****", label_visibility="collapsed")
    st.markdown('<label style="font-weight: bold; color: #666; margin-bottom: 5px; display: block;">CONFIRM PASSWORD</label>', unsafe_allow_html=True)
    st.markdown(f'<div style="margin-top: -30px;"></div>', unsafe_allow_html=True) # Adjust position if needed

    # The actual labels are added using markdown to get precise styling and placement.
    # The st.text_input's own label is hidden (`label_visibility="collapsed"`)
    # This is a common workaround to fully customize labels with Streamlit's current capabilities.


    # Sign Up Button
    submitted = st.form_submit_button("Sign up")

    if submitted:
        if email and password and confirm_password:
            if password == confirm_password:
                st.success("Profile created successfully! (This is a prototype, no actual profile stored)")
                # Here you would add your backend logic to store user data
                st.write(f"Email: {email}")
            else:
                st.error("Passwords do not match.")
        else:
            st.error("Please fill in all fields.")