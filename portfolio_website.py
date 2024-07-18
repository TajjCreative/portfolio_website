import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown('<h1 class="animated-title">Tajj Creative Portfolio Website</h1>', unsafe_allow_html=True)

st.markdown("""
    <style>
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .centered img {
        margin-top: 20px;
        transition: transform 0.3s; /* Animation */
    }
    .centered img:hover {
        transform: scale(1.1); /* Zoom effect on hover */
    }
    .slider-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .slider-container .stSlider > div:nth-child(2) > div > div > div > div {
        background-color: red;
        color: white;
    }
    .blue-title {
        color: blue;
    }
    .nav-menu {
        display: flex;
        justify-content: space-around;
        background-color: #f8f9fa;
        padding: 10px;
        margin-bottom: 20px;
    }
    .nav-menu a {
        text-decoration: none;
        color: black;
        font-weight: bold;
    }
    .nav-menu a:hover {
        color: #007bff;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .animated-title {
        animation: fadeIn 2s ease-in-out infinite; /* Added infinite loop */
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="nav-menu">
        <a href="#tajj-s-ai-bot">Tajj's AI Bot</a>
        <a href="#youtube-channel">Youtube Channel</a>
        <a href="#my-setup">My setup</a>
        <a href="#my-skills">My Skills</a>
        <a href="#gallery">Gallery</a>
        <a href="#contact">CONTACT</a>
    </div>
    """, unsafe_allow_html=True)

# Tajj's AI Bot Section
st.markdown('<div id="tajj-s-ai-bot" class="centered">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Hi :wave:")
    st.markdown('<h1 class="blue-title">I am Imtiaz Tajj</h1>', unsafe_allow_html=True)
with col2:
    st.image("images/profile-pic.png", width=300)  # Increased the width to 300

persona = """
I am Imtiaz Tajj from Khaplu, Gilgit-Baltistan, Pakistan. 
I graduated with a degree in Computer Science from the University 
of Baltistan Skardu in 2023. Currently, I work as an IT instructor 
at Uswa Public School for Girls in Yultar, Skardu, and serve as a 
program coordinator for CodeGirls projects at DPAK IT. I am self-motivated 
and passionate about learning new things. My skill set includes web development 
and freelancing. Additionally, 
I run a YouTube channel: Tajj Creative (http://www.youtube.com/tajjcreative).
If you don't know the answer then you say "That's secret".
"""

st.title("Tajj's AI Bot")
user_question = st.text_input("Ask anything about me")
if st.button("Ask", use_container_width=True):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)
st.markdown('</div>', unsafe_allow_html=True)

# Youtube Channel Section
st.markdown('<div id="youtube-channel">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Tajj Creative Youtube Channel")
    st.write("- 2K+ Subscribers")
    st.write("- Over 100+ Free Tutorials")
    st.write("- 20K+ Views")
    st.write("- 98K Views + watch time")

with col2:
    st.video("https://www.youtube.com/watch?v=VO2G1DnHbAE&t=38s")
st.markdown('</div>', unsafe_allow_html=True)

# My Setup Section
st.markdown('<div id="my-setup">', unsafe_allow_html=True)
st.title("My setup")
st.image("images/image_3.jpg")
st.markdown('</div>', unsafe_allow_html=True)

# My Skills Section
st.markdown('<div id="my-skills" class="slider-container">', unsafe_allow_html=True)
st.title("My Skills")
st.slider("Communication", 0, 100, 80)
st.slider("Teacher", 0, 100, 60)
st.slider("Programming", 0, 100, 70)
st.markdown('</div>', unsafe_allow_html=True)

# Gallery Section
st.markdown('<div id="gallery">', unsafe_allow_html=True)
st.title("Gallery")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/image_1.jpg", width=200)
    st.image("images/image_2.jpg", width=200)
    st.image("images/image_13.jpg", width=200)
    st.image("images/image_5.jpg", width=200)
with col2:
    st.image("images/image_6.jpg", width=200)
    st.image("images/image_7.jpg", width=200)
    st.image("images/image_8.jpg", width=200)
    st.image("images/image_14.jpg", width=200)
with col3:
    st.image("images/image_9.jpg", width=200)
    st.write("")
    st.write("")
    st.image("images/image_11.jpg", width=200)
    st.image("images/image_12.jpg", width=200)
    st.image("images/image_5.jpg", width=200)
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact">', unsafe_allow_html=True)
st.write(" ")
st.write("CONTACT")
st.subheader("For any queries, please contact me at")
st.write("tajjcreative123@gmail.com")
st.markdown('</div>', unsafe_allow_html=True)
