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

    # Hiển thị ảnh và liên kết trong cùng một div
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; height: 100vh; justify-content: center;">
            <img src="data:image/png;base64,{img_data}" style="max-width: 50%; height: auto;"/>
            <a href="https://forms.gle/RHqUBMKBeeJUgMD6A" 
               target="_blank" 
               style="font-size: 20px; color: blue; text-decoration: none; margin-top: 10px; text-align: center; max-width: 600px;">
                Nhấn vào đây, cho Tomi xin feedback để cải thiện hơn nha, Tomi luôn luôn lắng nghe và sẽ cố gắng hiểu nè!
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.error("Ảnh tomi.png không tồn tại trong thư mục 'images/'.")

