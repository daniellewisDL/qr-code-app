import streamlit as st
import qrcode
from PIL import Image
from numpy import asarray

st.header('Simple QR Code generator')
user_input = st.text_input("Enter link to website, hidden message, or any text!", value="https://daniellewisdl.github.io/")

st.write("Data to be encoded:")
st.write("{}".format(user_input))

if st.button('Generate'):
    img = Image.fromarray(asarray(qrcode.make(user_input)))
    st.image(img)


code="""
import streamlit as st
import qrcode
from PIL import Image
from numpy import asarray

st.header('Simple QR Code generator')
user_input = st.text_input("Enter link to website, hidden message, or any text!")

st.write("Data to be encoded:")
st.write("{}".format(user_input))

if st.button('Generate'):
    img = Image.fromarray(asarray(qrcode.make(user_input)))
    st.image(img)
"""

st.markdown('---')
code_expander = st.expander(label="See this app's code up to this point")
with code_expander:
    st.code(code, language="python")

from os import path
import base64

# Thanks to GokulNC for this code snippet
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
def get_img_with_href(local_img_path, target_url):
    img_format = path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" target="_blank">
            <img src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code

st.markdown('---')
png_html = get_img_with_href('GitHub-Mark-32px.png', 'https://github.com/daniellewisDL/qr-code-app')
st.markdown(png_html, unsafe_allow_html=True)
png_html = get_img_with_href('GitHub-Mark-Light-32px.png', 'https://github.com/daniellewisDL/qr-code-app')
st.markdown(png_html, unsafe_allow_html=True)
