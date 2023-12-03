import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
img_gus= Image.open("images/Gus.png")
# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns([7, 3])
    with left_column:
        st.title("Howdy,  I'm Gus! :face_with_cowboy_hat:")
        st.subheader("Data Guy at Northrop Grumman ")
        st.write(
            "I enjoy solving difficult problems with creative data-driven solutions."
        )
        st.write("[Learn More >](https://linkedin.com/agustus)")
    with right_column:
        st.image(img_gus, caption= "Speaking at the University of Texas at Dallas Data symposium",width=250)


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
           """
Welcome to my portfolio! I'm Gus Phillips, your go-to person for turning data into practical insights. I have a knack for making sense of complex information, using tools to spot trends and help our business make smarter decisions. I work closely with teams, turning their needs into easy-to-understand data solutions. I'm all about keeping our data safe and sound, and I'm always learning to bring the latest and greatest to the table. Check out my portfolio to see how I make data work for us!          """
           )
        st.write(":smile:")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# # ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Coming Soon! ")
#         st.write(
#             """I can create things I swear! 
#             """
#         )
#         st.markdown("[Watch Video...](https://www.youtube.com/shorts/MSsA6y_JW6A)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("Don't worry things will be here")
#         st.write(
#             """
#             Wow I bet something belongs here eventually
#             """
#         )
#         st.markdown("[Watch Video...](https://www.youtube.com/watch?v=eTLi1gk5h6U)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write(
            "Feel free to reach out to me on Linkedin @ https://linkedin.com/agustus"
        )
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/pleasetrinket@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
