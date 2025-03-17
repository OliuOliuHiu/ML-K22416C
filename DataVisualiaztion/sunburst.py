import pandas as pd
import plotly.express as px

# 1. Đọc dữ liệu từ file Excel
file_path = "./dataset-416.xlsx"  # Đổi thành đường dẫn file của bạn
xls = pd.ExcelFile(file_path)

# 2. Đọc sheet đầu tiên
df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])

# 3. Kiểm tra và xử lý dữ liệu thiếu
df_filtered = df.dropna(subset=['Tên học phần', 'Học Kỳ', 'Loại môn học'])

# 4. Chuyển đổi dữ liệu học kỳ thành dạng chuỗi
df_filtered = df_filtered.copy()  # Tạo bản sao để tránh cảnh báo
df_filtered['Học Kỳ'] = df_filtered['Học Kỳ'].astype(int).astype(str)


# 5. Tạo biểu đồ sunburst
fig = px.sunburst(
    df_filtered,
    path=['Học Kỳ', 'Loại môn học', 'Tên học phần'],  # Cấu trúc phân cấp
    values=[1] * len(df_filtered),  # Gán trọng số bằng nhau
    title="Biểu đồ Nested Pie Chart của các môn học theo kỳ",
    color='Loại môn học',  # Màu theo loại môn học
)

# 6. Xuất biểu đồ ra file HTML
output_html = "sunburst_chart.html"
fig.write_html(output_html)

print(f"Biểu đồ đã được lưu tại {output_html}. Hãy mở file này trong trình duyệt để xem.")
