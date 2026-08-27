import streamlit as st
from database import get_connection

st.set_page_config(
    page_title="Khách hàng tiềm năng",
    page_icon="👤",
    layout="centered"
)

st.title("👤 KHÁCH HÀNG TIỀM NĂNG")
st.write("Vui lòng nhập đầy đủ thông tin khách hàng.")

with st.form("form_khach_hang"):

    # =========================
    # THÔNG TIN CÁ NHÂN
    # =========================

    st.subheader("📋 Thông tin khách hàng")

    ho_ten = st.text_input("Họ và tên *")

    so_dien_thoai = st.text_input("Số điện thoại *")

    email = st.text_input("Email")

    gioi_tinh = st.selectbox(
        "Giới tính",
        ["Nam", "Nữ"]
    )

    tuoi = st.number_input(
        "Tuổi",
        min_value=1,
        max_value=100,
        step=1
    )

    nghe_nghiep = st.text_input("Nghề nghiệp")

    khu_vuc = st.selectbox(
        "Khu vực",
        [
            "Đà Lạt",
            "Đức Trọng",
            "Lâm Hà",
            "Di Linh",
            "Bảo Lộc",
            "Lạc Dương",
            "Đơn Dương",
            "Đam Rông",
            "Khác"
        ]
    )

    # =========================
    # NHU CẦU TÀI CHÍNH
    # =========================

    st.subheader("💰 Nhu cầu tài chính")

    san_pham_quan_tam = st.selectbox(
        "Sản phẩm quan tâm",
        [
            "Vay mua ô tô",
            "Vay mua nhà",
            "Vay tiêu dùng",
            "Vay sản xuất kinh doanh",
            "Thẻ tín dụng",
            "Tiền gửi tiết kiệm",
            "Bảo hiểm",
            "Khác"
        ]
    )

    nhu_cau_tai_chinh = st.text_area(
        "Nhu cầu tài chính"
    )

    so_tien_du_kien = st.number_input(
        "Số tiền dự kiến (VNĐ)",
        min_value=0,
        step=1000000
    )

    # =========================
    # ĐÁNH GIÁ KHÁCH HÀNG
    # =========================

    st.subheader("📊 Đánh giá khách hàng")

    muc_do_tiem_nang = st.selectbox(
        "Mức độ tiềm năng",
        [
            "Cao",
            "Trung bình",
            "Thấp"
        ]
    )

    trang_thai_cham_soc = st.selectbox(
        "Trạng thái chăm sóc",
        [
            "Chưa liên hệ",
            "Đã liên hệ",
            "Đang tư vấn",
            "Đang theo dõi",
            "Đã chuyển đổi",
            "Không có nhu cầu"
        ]
    )

    ghi_chu = st.text_area(
        "Ghi chú"
    )

    # =========================
    # NÚT LƯU
    # =========================

    submit = st.form_submit_button(
        "💾 LƯU KHÁCH HÀNG"
    )


# =========================
# XỬ LÝ LƯU DATABASE
# =========================

if submit:

    if ho_ten.strip() == "":
        st.warning("⚠️ Vui lòng nhập họ và tên.")

    elif so_dien_thoai.strip() == "":
        st.warning("⚠️ Vui lòng nhập số điện thoại.")

    else:
try:

            conn = get_connection()
            cursor = conn.cursor()

            sql = """
            INSERT INTO khach_hang_tiem_nang
            (
                ho_ten,
                so_dien_thoai,
                email,
                gioi_tinh,
                tuoi,
                nghe_nghiep,
                khu_vuc,
                san_pham_quan_tam,
                nhu_cau_tai_chinh,
                so_tien_du_kien,
                muc_do_tiem_nang,
                trang_thai_cham_soc,
                ghi_chu
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
            """

            cursor.execute(
                sql,
                (
                    ho_ten,
                    so_dien_thoai,
                    email,
                    gioi_tinh,
                    tuoi,
                    nghe_nghiep,
                    khu_vuc,
                    san_pham_quan_tam,
                    nhu_cau_tai_chinh,
                    so_tien_du_kien,
                    muc_do_tiem_nang,
                    trang_thai_cham_soc,
                    ghi_chu
                )
            )

            conn.commit()

            cursor.close()
            conn.close()

            st.success("🎉 Đã lưu thông tin khách hàng thành công!")

        except Exception as e:

            st.error(f"❌ Lỗi: {e}")
