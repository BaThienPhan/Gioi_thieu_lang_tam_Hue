import streamlit as st
from PIL import Image
import requests
from io import BytesIO
# Cài đặt trang
st.set_page_config(page_title="Giới thiệu khí hậu và Du lịch ở Huế",
                   page_icon=":city_sunset:", layout="wide")

# CSS tùy chỉnh
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #b30000;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #b30000;
        font-size: 2em;
        font-weight: bold;
        margin: 20px 0 10px 0;
    }
    .text {
        color: #000000;
        font-size: 1.2em;
        line-height: 1.6;
    }
    .content-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .image-box {
        flex: 1;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 10px;
        text-align: center;
    }
    .image-box img {
        width: 100%;
        border-radius: 10px;
    }
    .image-caption {
        text-align: center;
        font-style: italic;
        color: #888888;
        font-size: 1em;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    /* Tùy chỉnh giao diện cho thanh tabbar */
    .sidebar .sidebar-content {
        background-color: #333;
        color: white;
    }
    .sidebar .sidebar-content .element-container {
        background-color: #333;
        color: white;
        border: none;
    }
    .sidebar .sidebar-content button {
        background-color: #444;
        color: white;
        border: none;
        border-radius: 5px;
        margin: 5px 0;
        padding: 10px 15px;
        cursor: pointer;
    }
    .sidebar .sidebar-content button:hover {
        background-color: #555;
    }
    .sidebar .sidebar-content button:focus {
        background-color: #555;
        outline: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Thanh Tabbar nằm dọc
tab = st.sidebar.radio("NỘI DUNG", [
    "HUẾ", "ĐẶC TRƯNG KHÍ HẬU", "CÁC MÙA TRONG NĂM", "DU LỊCH HUẾ"])

# Hàm tải ảnh từ URL
def load_image(url):
   response = requests.get(url)
   return Image.open(BytesIO(response.content))

# Hiển thị ảnh sử dụng Streamlit
# st.image(load_image("https://github.com/BaThienPhan/App_Dien_Kien_Trung/raw/main/vi-tri-1.jpg"),
#                 caption="Điện Kiến Trung thời Pháp", use_column_width=True)

# Giới thiệu Huế
if tab == "HUẾ":
    st.markdown("<div class='title'>HUẾ - THÀNH PHỐ MỘNG MƠ</div>",
                unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.05])

    with col1:
        # Thay thế bằng đường dẫn tới hình ảnh của bạn
        st.image(load_image("https://github.com/BaThienPhan/Khi-hau-va-du-lich-Hue/raw/main/gt-hue-1.jpg"),
                 caption="Cố đô Huế", use_column_width=True)
    with col2:
        # Thay thế bằng đường dẫn tới hình ảnh của bạn
        st.image(load_image("https://github.com/BaThienPhan/Khi-hau-va-du-lich-Hue/raw/main/gt-hue-2.jpg"), caption="Vị trí Huế trên bản đồ Việt Nam",
                 use_column_width=True)
    st.markdown("""
        <div class='text'>
        <p>
        Huế là một thành phố nằm ở miền Trung Việt Nam, được biết đến với bề dày lịch sử và văn hóa phong phú. 
        Đây từng là kinh đô của triều đại nhà Nguyễn, triều đại phong kiến cuối cùng của Việt Nam, từ năm 1802 đến năm 1945. 
        Thành phố Huế không chỉ nổi tiếng với kiến trúc cổ kính, các di tích lịch sử, mà còn với những lễ hội truyền thống và nền ẩm thực đặc sắc.</p>
        </div>
    """, unsafe_allow_html=True)
# Đặc trưng khí hậu
elif tab == "ĐẶC TRƯNG KHÍ HẬU":
    st.markdown("<div class='subtitle'>ĐẶC TRƯNG KHÍ HẬU</div>",
                unsafe_allow_html=True)

    col3, col4, col5 = st.columns(3)

    with col3:
        # Thay thế bằng đường dẫn tới hình ảnh của bạn
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/kh-1.jpg",
                 caption="", use_column_width=True)
    with col4:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/kh-2.png",
                 caption="", use_column_width=True)
    with col5:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/kh-3.jpg",
                 caption="", use_column_width=True)
    st.markdown("""
        <div class='text'>
            <p></p>
            <ul>
                <li><b></b>Vị trí địa lý của Huế nằm ở phía Nam của khu vực duyên hải Bắc Trung Bộ và thuộc vùng nội chí tuyến nên có nền nhiệt khá cao, đặc trưng khí hậu nóng ẩm. Mặt khác, Huế nằm trong khu vực chuyển tiếp khí hậu giữa hai miền Bắc và Nam nước ta, do đó khí hậu Huế cũng chịu tác động của chế độ gió mùa khá đa dạng và luôn có sự giao thoa giữa 2 miền khí hậu.</li>
                <li><b></b>Nhìn chung, phần lớn diện tích của Huế là đồi núi, hầu hết các dãy núi có độ cao khá lớn tạo thành bức tường vòng cung chắn gió Tây Nam khô nóng vào mùa hè và đón gió Đông Bắc về mùa đông.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Các mùa trong năm
elif tab == "CÁC MÙA TRONG NĂM":
    st.markdown("<div class='subtitle'>CÁC MÙA TRONG NĂM</div>",
                unsafe_allow_html=True)
    col6, col7 = st.columns([1.45, 1])

    with col6:
        # Thay thế bằng đường dẫn tới hình ảnh của bạn
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-1.jpg",
                 caption="", use_column_width=True)
    with col7:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-2.png",
                 caption="", use_column_width=True)
    st.markdown("""
        <div class='text'>
            <p>Thời tiết Huế trong năm phân hóa rõ rệt theo hai khuynh hướng</p>
            <ul>
                <li><b>Mùa khô nóng:</b> Mùa khô nóng:Từ tháng 5 - tháng 9 với sự ảnh hưởng của gió 
                Tây Nam nên thời tiết khá nóng và có mưa rào vào buổi chiều.
                Nhiệt độ trung bình: 30 - 32 độ C.</li>
                <li><b>Mùa ẩm, lạnh:</b> tháng 10 - tháng 3 năm sau với sự  ảnh hưởng của gió 
                mùa Đông Bắc nên thời tiết mưa nhiều và khá lạnh. 
                Nhiệt độ trung bình: 20 - 22 độ C.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# Du lịch Huế
elif tab == "DU LỊCH HUẾ":
    st.markdown("<div class='subtitle'>ĐÓN NẮNG ĐẦU XUÂN (Tháng 1-3)</div>",
                unsafe_allow_html=True)
    st.markdown("""
        <div class='text'>
        <p>
        Nhìn chung, phần lớn diện tích của Huế là đồi núi, hầu hết các dãy núi có độ cao khá lớn tạo thành bức tường vòng cung chắn gió Tây Nam khô nóng vào mùa hè và đón gió Đông Bắc về mùa đông.
        </p>
        <p>
        <b>Thời tiết: </b>Mát mẻ, dễ chịu với nhiệt độ trung bình khoảng 20-30°C, ít mưa.
        </p>
        <p>
        Tới Huế vào mùa xuân, bạn đừng quên chiêm ngưỡng vẻ đẹp của Đại Nội Huế, Cung An Định, Thiền Viện Trúc Lâm và các lăng tẩm. Tuy nhiên, sẽ có những cơn mưa đầu mùa vào tháng 1, do đó, nếu muốn khám phá cố đô được thuận tiện nhất thì hãy chuẩn bị thêm cho mình một chiếc ô nhé.
        </p>
        </div>
    """, unsafe_allow_html=True)
    col10, col11, col12, col13 = st.columns(4)
    with col10:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/dn-cung-an-dinh.jpg",
                 caption="Cung An Định", use_column_width=True)
    with col11:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/dn-dai-noi-hue.jpg",
                 caption="Đại Nội Huế", use_column_width=True)
    with col12:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/dn-lang-tam.png",
                 caption="Lăng tẩm", use_column_width=True)
    with col13:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/dn-thien-vien-truc-lam.png",
                 caption="Thiền viện Trúc Lâm", use_column_width=True)

    st.markdown("<div class='subtitle'>MÙA LỄ HỘI CỐ ĐÔ (Tháng 4)</div>",
                unsafe_allow_html=True)
    st.markdown("""
        <div class='text'>
        <p>
        <b>Thời tiết: </b>Mát mẻ, dễ chịu với nhiệt độ trung bình khoảng 20-30°C, ít mưa.
        </p>
        <p>Có thể nói, mảnh đất cố đô đẹp nhất chắc hẳn sẽ vào mùa Festival Huế. Đây được biết tới là một trong những lễ hội Huế có quy mô lớn nhất trong năm. Trong những ngày diễn ra lễ hội, du khách sẽ được trải nghiệm một không khí vô cùng náo nhiệt, sôi động với rất nhiều các hoạt động vui chơi, nghệ thuật giải trí đa dạng.</p>
        <p>
        Nếu bạn là người thích khám phá những văn hóa và đặc trưng nổi bật ở Huế thì đừng bỏ lỡ thời điểm này nhé!      
        </p>
        </div>
    """, unsafe_allow_html=True)
    col14, col15 = st.columns([1.35, 1.15])
    with col14:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-le-hoi-1.png",
                 caption="", use_column_width=True)
    with col15:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-le-hoi-2.png",
                 caption="", use_column_width=True)
    st.markdown("<div class='subtitle'>MÙA DU LỊCH BIỂN (Tháng 5-8)</div>",
                unsafe_allow_html=True)
    st.markdown("""
        <div class='text'>
        <p>
        <b>Thời tiết: </b>Khá nóng, nhiệt độ có thể lên tới 35-37°C. Có thể có mưa rào vào buổi chiều. 
        </p>
        <p>
        Từ tháng 5 đến tháng 8 hàng năm là thời điểm lý tưởng nhất để du lịch biển ở Huế. Vào thời gian này thời tiết Huế khá nóng bức, do đó nếu được hòa mình với những làn nước mát lạnh, không khí trong lành của những bãi biển hay sông suối ở Huế thì không còn gì tuyệt vời hơn.
        </p>
        <p>
        Ngoài ra, bạn cũng có thể tham gia chèo sup trên sông Hương, hoặc tự mình trải nghiệm cuộc sống của những người ngư dân chân chất, thưởng thức các món ăn địa phương ở đầm Chuồn.
        </p> 
        </div>
    """, unsafe_allow_html=True)
    col16, col17, col18, col19 = st.columns(4)
    with col16:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/du-lich-bien-lang-co-thuan-an.png",
                 caption="Lăng Cô - Thuận An", use_column_width=True)
    with col17:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/du-lich-bien-dam-chuon.png",
                 caption="Đầm Chuồn", use_column_width=True)
    with col18:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/du-lich-bien-cheo-sup.png",
                 caption="Chèo sup trên sông Hương", use_column_width=True)
    with col19:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/du-lich-bien-song-suoi.png",
                 caption="Sông suối", use_column_width=True)
    st.markdown("<div class='subtitle'>MÙA MƯA XỨ THƠ (Tháng 9-12)</div>",
                unsafe_allow_html=True)
    st.markdown("""
        <div class='text'>
        <p>
        <b>Thời tiết: </b>Lạnh và ẩm ướt, nhiệt độ trung bình khoảng 15-20°C.</p>
        <p>
        Mưa ở Huế được mệnh danh là “đặc sản” cố đô. Mùa mưa “xứ thơ” thường bắt đầu từ tháng 9 đến hết tháng 12 trong năm. Những cơn mưa triền miên vào mùa này đã tạo nên điểm khác biệt càng khiến cho sự trầm mặc, hoài cổ của cố đô càng hiển hiện rõ.</p>
        
        <p>Du lịch Huế mùa mưa, du khách có thể ghé chợ Đông Ba thưởng thức những món đồ nướng vỉa hè thơm ngon. Hoặc cũng có thể tới uống trà và thưởng thức nhã nhạc cung đình Huế trên những chiếc du thuyền tản mạn dòng sông Hương.
        </p>
        </div>
    """, unsafe_allow_html=True)
    col20, col21, col22, col23, col24 = st.columns([1, 1, 1, 1, 1.5])
    with col20:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-mua-xu-tho-1.png",
                 caption="", use_column_width=True)
    with col21:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-mua-xu-tho-2.png",
                 caption="", use_column_width=True)
    with col22:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-mua-xu-tho-3.png",
                 caption="", use_column_width=True)
    with col23:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/mua-mua-xu-tho-4.png",
                 caption="", use_column_width=True)
    with col24:
        st.image("C:/Users/bathi/OneDrive/Desktop/Python/Khi-Hau-Hue/dl-nha-nhac.jpg",
                 caption="", use_column_width=True)

    # Footer
    st.markdown("""
    <div class='footer'>
    © 2024 Khí hậu và du lịch Huế. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
