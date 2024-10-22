import streamlit as st
import os
import base64

# Đường dẫn đến ảnh
image_path = "images/Tomi-Sticker_Part1_18.png"

# Kiểm tra xem ảnh có tồn tại không
if os.path.exists(image_path):
    # Đọc và mã hóa ảnh dưới dạng base64
    with open(image_path, "rb") as img_file:
        img_data = base64.b64encode(img_file.read()).decode()

    # Hiển thị ảnh ở giữa màn hình
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
            <img src="data:image/png;base64,{img_data}" style="max-width: 50%; height: auto;"/>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.error("Ảnh tomi.png không tồn tại trong thư mục 'images/'.")

# Thêm liên kết tới Google Form
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: 20px;">
        <a href="https://docs.google.com/forms/d/e/1FAIpQLSfp7fn-ncGWmHHoX4GYgEjSAjmWUcfFaUGnKTggx35p8OLu6A/viewform?pli=1" 
           target="_blank" style="font-size: 20px; color: blue; text-decoration: none;">
            Đi tới biểu mẫu Google Form
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
