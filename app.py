import streamlit as st

st.set_page_config(
    page_title="Quản lý khách hàng tiềm năng",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 QUẢN LÝ KHÁCH HÀNG TIỀM NĂNG")

st.write("Vui lòng điền đầy đủ thông tin khách hàng dưới đây.")

with st.form("form_khach_hang"):

    ho_ten = st.text_input("Họ và tên")

    gioi_tinh = st.radio(
        "Giới tính",
        ["Nam", "Nữ"]
    )

    so_dien_thoai = st.text_input("Số điện thoại")

    email = st.text_input("Email")

    tuoi = st.number_input(
        "Tuổi",
        min_value=18,
        max_value=100,
        step=1
    )

    nghe_nghiep = st.text_input("Nghề nghiệp")

    khu_vuc = st.text_input("Khu vực")

    san_pham_quan_tam = st.selectbox(
        "Sản phẩm khách hàng quan tâm",
        [
            "Vay mua nhà",
            "Vay mua ô tô",
            "Vay tiêu dùng",
            "Thẻ tín dụng",
            "Tiền gửi tiết kiệm",
            "Tài khoản thanh toán",
            "Khác"
        ]
    )

    nhu_cau_tai_chinh = st.text_input(
        "Nhu cầu tài chính"
    )

    so_tien_du_kien = st.number_input(
        "Số tiền dự kiến",
        min_value=0,
        step=1000000
    )

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
            "Đã chuyển đổi",
            "Không có nhu cầu"
        ]
    )

    ghi_chu = st.text_area("Ghi chú")

    submit = st.form_submit_button("Lưu khách hàng")


if submit:

    if ho_ten == "" or so_dien_thoai == "":
        st.error("Vui lòng nhập Họ tên và Số điện thoại!")

    else:
        st.success("✅ Lưu thông tin khách hàng thành công!")

        st.write("### 📋 Thông tin khách hàng vừa nhập")

        st.write("**Họ tên:**", ho_ten)
        st.write("**Giới tính:**", gioi_tinh)
        st.write("**Số điện thoại:**", so_dien_thoai)
        st.write("**Email:**", email)
        st.write("**Tuổi:**", tuoi)
        st.write("**Nghề nghiệp:**", nghe_nghiep)
        st.write("**Khu vực:**", khu_vuc)
        st.write("**Sản phẩm quan tâm:**", san_pham_quan_tam)
        st.write("**Nhu cầu tài chính:**", nhu_cau_tai_chinh)
        st.write("**Số tiền dự kiến:**", so_tien_du_kien)
        st.write("**Mức độ tiềm năng:**", muc_do_tiem_nang)
        st.write("**Trạng thái chăm sóc:**", trang_thai_cham_soc)
        st.write("**Ghi chú:**", ghi_chu)
