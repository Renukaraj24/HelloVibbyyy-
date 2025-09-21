import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Scrapbook with Text Notes", layout="wide")
st.image("scrapbooklogo.png")
st.title("Interactive Scrapbook - Add Elements & Text Notes")

# Convert image files to base64 data URLs
def img_file_to_data_url(file_path):
    with open(file_path, "rb") as img_f:
        b64_str = base64.b64encode(img_f.read()).decode()
        if file_path.endswith(".png"):
            mime = "image/png"
        elif file_path.endswith(".jpg") or file_path.endswith(".jpeg"):
            mime = "image/jpeg"
        else:
            mime = "image/png"
        return f"data:{mime};base64,{b64_str}"

# Your scrapbook element images — update paths if needed
element_imgs = [
    ("Brown Sticky", img_file_to_data_url("scrapbookelements/brownboxpaper.png")),
    ("Ripped Paper", img_file_to_data_url("scrapbookelements/plainbigbroeinyellowpage.png")),
    ("Plaid Tape", img_file_to_data_url("scrapbookelements/yellowboxbox.png")),
    ("Line Line", img_file_to_data_url("scrapbookelements/lineline.png")),
    ("Slime Line", img_file_to_data_url("scrapbookelements/bigslimpage.png")),
    ("Big Box", img_file_to_data_url("scrapbookelements/bigbox.png")),
    ("Brown Horizontal Paper", img_file_to_data_url("scrapbookelements/bigbrownhorizontalpage.png")),
]

# Prepare buttons and base64 list for JS images
js_imgs_code = "[" + ", ".join(f'"{img}"' for _, img in element_imgs) + "]"
btn_htmls = []
for idx, (label, _) in enumerate(element_imgs):
    btn_htmls.append(
        f'''<button class="element-btn" title="{label}" onclick="addElement({idx})">
                <img src="{element_imgs[idx][1]}" style="height:36px; max-width: 80px; object-fit: contain;">
            </button>'''
    )

css = """
<style>
.scrapbook-bg {
    width: 100vw;
    height: 820px;
    background: #faf6ee;
    border-radius: 0;
    margin: 0;
    position: relative;
    border: none;
    box-shadow: none;
}

.toolbar {
    width: 100vw;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    gap: 18px;
    padding: 1rem 5vw;
    box-sizing: border-box;
    background-color: #efeadf;
}

.element-btn {
    background: #eacba6;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    padding: 4px 10px;
    box-shadow: 0 2px 10px #eadcb7a0;
    transition: transform 0.2s ease;
}
.element-btn:hover {
    transform: scale(1.1);
}
.scrap-img-elem, .text-note {
    position: absolute;
    cursor: grab;
    user-select: none;
    border-radius: 8px;
}

.scrap-img-elem {
    max-width: 140px;
    max-height: 120px;
}

.text-note {
    min-width: 120px;
    min-height: 70px;
    background: #fffacd;
    padding: 10px 15px;
    border: 2px solid #f3eacb;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    resize: both;
    overflow: auto;
    cursor: text;
    color: #222;
}
</style>
"""

html_code = f"""
{css}
<div class="toolbar">
{''.join(btn_htmls)}
<button class="element-btn" onclick="addTextNote()">Add Text Note</button>
</div>
<div class="scrapbook-bg" id="scrapbook-bg"></div>
<script>
// Store image data URLs in JS array
window.elementImgs = {js_imgs_code};

// Add image element to scrapbook on button click
function addElement(idx) {{
    let img = document.createElement('img');
    img.src = window.elementImgs[idx];
    img.className = "scrap-img-elem";
    setPositionRandom(img);
    img.draggable = true;
    img.onmousedown = dragMouseDown;
    document.getElementById('scrapbook-bg').appendChild(img);
}}

// Add editable text note
function addTextNote() {{
    let note = document.createElement('div');
    note.className = "text-note";
    note.contentEditable = true;
    note.textContent = "New note...";
    setPositionRandom(note);
    note.onmousedown = dragMouseDown;
    document.getElementById('scrapbook-bg').appendChild(note);
}}

// Set random position within scrapbook background
function setPositionRandom(el) {{
    let bg = document.getElementById('scrapbook-bg').getBoundingClientRect();
    el.style.left = (30 + Math.random()*(bg.width - 150)) + "px";
    el.style.top = (30 + Math.random()*(bg.height - 100)) + "px";
}}

// Drag logic common for images and text notes
let dragTarget = null, offsetX = 0, offsetY = 0;

function dragMouseDown(e) {{
    dragTarget = e.target;
    offsetX = e.clientX - dragTarget.offsetLeft;
    offsetY = e.clientY - dragTarget.offsetTop;
    // To allow resize on text note, disable drag if click on resize handle
    if(e.target.classList.contains('text-note')) {{
        // do nothing on drag if over resize handle; simple version
    }}
    document.onmousemove = elementDrag;
    document.onmouseup = stopDrag;
}}

function elementDrag(e) {{
    if(!dragTarget) return;
    let bg = document.getElementById('scrapbook-bg').getBoundingClientRect();
    let left = e.clientX - bg.left - offsetX;
    let top = e.clientY - bg.top - offsetY;
    left = Math.max(0, Math.min(left, bg.width - dragTarget.offsetWidth));
    top = Math.max(0, Math.min(top, bg.height - dragTarget.offsetHeight));
    dragTarget.style.left = left + 'px';
    dragTarget.style.top = top + 'px';
}}

function stopDrag(e) {{
    dragTarget = null;
    document.onmousemove = null;
    document.onmouseup = null;
}}
</script>
"""

components.html(html_code, height=860, width=1024)
st.caption("Add scrapbook elements or text notes. Drag and resize text freely on the scrapbook.")
