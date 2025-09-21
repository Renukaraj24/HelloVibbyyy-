
import streamlit as st
import base64
st.image("reflectonurthoughts.png", use_container_width=True)
# Helper to convert image to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(layout="centered", page_title="Reflect on your thoughts")

    # Use your note card image as background for cards (replace this with your card filename)
    card_file = "image.png"  # Example; replace with your own if needed
    card_bg = get_img_as_base64(card_file)

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Handlee&family=Montserrat:wght@400;700&family=Pacifico&display=swap');

    .main-header {
        font-family: 'Pacifico', cursive;
        font-size: 2.3em;
        text-align: center;
        color: #302424;
        margin-bottom: 8px;
        margin-top: 10px;
        letter-spacing: 1px;
    }
    .sub-header {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2em;
        text-align: center;
        color: #62485e;
        margin-bottom: 32px;
        letter-spacing: 0.8px;
    }
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 28px 22px;
        justify-items: center;
        margin-bottom: 32px;
    }

    .note-card {
        width: 450px;
        height: 180px;
        background: url("data:image/jpg;base64,%s") no-repeat center/cover;
        box-shadow: 1px 2.5px 14px rgba(100,70,90,0.11);
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        position: relative;
        border-radius: 9px;
        padding: 14px 20px 8px 20px;
        font-family: 'Handlee', cursive;
    }

    .note-emoji {
        font-size: 2.1em;
        margin-right: 10px;
        margin-top: 4px;
        flex-shrink: 0;
    }
    .note-prompt {
        font-size: 1.08em;
        margin-top: 3px;
        color: #232021;
        font-family: 'Handlee', cursive;
        width: 170px;
        border: none;
        background: transparent;
        outline: none;
        resize: none;
        line-height: 1.5;
    }
    .save-btn {
        display: block;
        margin: 0 auto 10px auto;
        background-color: #e9a8cd;
        border: none;
        color: #fff;
        font-size: 1.4em;
        font-family: 'Montserrat', sans-serif;
        font-weight: bold;
        padding: 0.48em 3.7em;
        border-radius: 17px;
        box-shadow: 1.5px 3px 10px rgba(120,40,70,0.09);
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .save-btn:hover {
        background: #e9a8cd;
    }
    </style>
    """ % card_bg, unsafe_allow_html=True)

    # st.markdown('<div class="main-header">Reflect on your thoughts</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">What made you feel like this???</div>', unsafe_allow_html=True)

    prompts = [
        ("😁", "My friend gave me surprise today"),
        ("😘", "She gave me a gift"),
        ("😊", "I have no assignments today"),
        ("😰", "I have exams tomorrow"),
        ("😲", "Syllabus is so big to finish in 1 day"),
        ("😥", "Subject is soo vast"),
        ("😡", ""),
        ("😤", "Sir gave us surprise test"),
        ("😕", ""),
        ("😴", "It's 10pm ... I'll go to bed"),
    ]

    user_inputs = []
    st.markdown('<div class="cards-grid">', unsafe_allow_html=True)
    for idx, (emoji, prompt) in enumerate(prompts):
        # Each card
        default_val = prompt
        input_id = f"thought_note_{idx}"

        st.markdown(f'''
            <div class="note-card">
                <span class="note-emoji">{emoji}</span>
                <textarea class="note-prompt" rows="2" id="{input_id}" name="{input_id}" placeholder="Write here...">{default_val}</textarea>
            </div>
        ''', unsafe_allow_html=True)
        user_inputs.append({"id": input_id, "emoji": emoji, "prompt": prompt})
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Save", key="save_btn"):
    # your save logic

        st.success("Notes saved! 🎉")
        # for i, text in enumerate(note_values):
        #     st.write(f"**{prompts[i][0]}**: {text if text else '_No input_'}")

if __name__ == "__main__":
    main()
