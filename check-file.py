import os
import glob

# Lấy đường dẫn thư mục hiện tại
current_dir = os.path.dirname(os.path.abspath(__file__))

# Duyệt qua tất cả các thư mục con trong thư mục hiện tại
for dir_name in os.listdir(current_dir):
    sub_dir = os.path.join(current_dir, dir_name)
    
    # Kiểm tra nếu là thư mục
    if os.path.isdir(sub_dir):
        # Tìm tất cả các tệp ảnh trong thư mục (chỉ tìm kiểu .png và .jpg)
        images = glob.glob(sub_dir + "/*.png") + glob.glob(sub_dir + "/*.jpg")
        
        # Nếu số lượng ảnh nhỏ hơn 2
        if len(images) < 2:
            # Đổi tên thư mục, thêm chuỗi "XxX " vào cuối
            new_dir_name = sub_dir + "XxX "
            os.rename(sub_dir, new_dir_name)
