import os
from PIL import Image

# Duyệt qua tất cả thư mục
for root, dirs, files in os.walk('./output'):
    for file in files:
        # Nếu tên file là 'z_download.png'
        if file == 'z-download.png':
            # Đường dẫn đầy đủ đến file ảnh
            img_path = os.path.join(root, file)
            
            # Đọc file ảnh
            img = Image.open(img_path)

            # Lấy kích thước của ảnh
            width, height = img.size

            # Cắt ảnh thành 4 phần
            img1 = img.crop((0, 0, width // 2, height // 2))
            img2 = img.crop((width // 2, 0, width, height // 2))
            img3 = img.crop((0, height // 2, width // 2, height))
            img4 = img.crop((width // 2, height // 2, width, height))

            # Lưu 4 bức ảnh đã cắt
            img1.save(os.path.join(root, 'z_1.jpg'))
            img2.save(os.path.join(root, 'z_2.jpg'))
            img3.save(os.path.join(root, 'z_3.jpg'))
            img4.save(os.path.join(root, 'z_4.jpg'))

            # Xóa file ảnh 'z_download.png'
            os.remove(img_path)
