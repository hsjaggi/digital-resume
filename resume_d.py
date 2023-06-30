from pathlib import Path

# import requests
import streamlit as st
from PIL import Image
# try:
#     from typing import Literal
# except ImportError:
#     from typing_extensions import Literal

# from streamlit_lottie import st_lottie

#----animation--------
# def load_lottieurl(url):
#     response = requests.get(url)
#     if response.status_code != 200:
#         return None
#     return response.json()

#---Path Settings---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file1 = current_dir / "styles" / "main.css"
css_file2 = current_dir / "styles" / "style.css"
resume_file = current_dir / "files" / "Harsohrab's Resume.pdf"
profile_pic = current_dir / "files" / "profile-pic-0.png"

#----General Settings------
PAGE_TITLE = "Digital Resume | Harsohrab Singh"
PAGE_ICON = ":wave:"   #PAGE_ICON = "random"
NAME = "HARSOHRAB SINGH"
DESCRIPTION = """
Data Analytics Expert assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "harsohrab.singh@gmail.com"
SOCIAL_MEDIA = {
    "LINKEDIN":"https://www.linkedin.com/in/harsohrab-singh-935748128",
    "GitHub":"https://github.com/hsjaggi"
}
PROJECTS = {
    "Web-Scrapping using Selenium & Beautiful Soup":"https://github.com/hsjaggi/flipkart-scrapping",
    "Data Exploration Using SQL & Visualization in Tableau":"https://github.com/hsjaggi/Amazon-Webscrapping"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#----Load CSS, PDF & Profile Pic
with open(css_file1) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(css_file2) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()   
profile_pic = Image.open(profile_pic)
# lottie_animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tljjahng.json")


#---------Hero Section--------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",

    )
    st.write(" ", EMAIL)


#------Social Links------
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#------Skills-----------
st.write("#")
# left_column, right_column = st.columns(2, gap="medium")
# with left_column:
st.write("\n")
st.subheader("Technical Skills")
st.write(
"""
- Programming: SQL, Python (Numpy, Pandas)
- Visualization: Tableau, MS Excel, Plotly
- Database: MySQL, SQL Server
"""
)
  
# with right_column:
#     st_lottie(lottie_animation, height = 200, key="coding")

#-----Experience & Qualifications-------

st.write("\n")
st.subheader("Professional Experience")
st.write("---")

#------job-----------
with st.container():
    st.write("Senior System Engineer | Infosys Ltd.")
    st.write("01/2019 - 09/2021")
    st.write(
            """
        ► Fetched data from several sources including: DB2, flat files, VSAM; extracted, transformed and loaded into various HDFS
        systems via Confidential scripts.

        ► Interfaced with key stakeholders and applied technical proficiency across different stages of the Software Development 
        Life Cycle including Requirements Elicitation, Application Architecture definition and Design
        """
        )

#------Projects----
st.write("#")
st.subheader("Personal Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


#-----Contact-----
with st.container():
    st.write("---")
    st.subheader("Get in Touch with Me!")
    st.write("##")

# https://formsubmit.co/hsv3.singh@gmail.com
    #Contact Form---https://formsubmit.co/ 
    contact_form = """
    <form action="4b097a17db502f5546ab82680fb46e02" method="POST">
        <input type="hidden" name="_captcha" value="false">    
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name = "message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

