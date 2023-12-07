import os
import zipfile

# Tạo thư mục output nếu chưa tồn tại
if not os.path.exists('output'):
    os.makedirs('output')

# Tạo thư mục output_zip nếu chưa tồn tại
output_zip_dir = 'output_zip'
if not os.path.exists(output_zip_dir):
    os.makedirs(output_zip_dir)

zip_counter = 1

# Duyệt qua tất cả thư mục trong thư mục 'output'
for root, dirs, files in os.walk('output'):
    # Kiểm tra trong thư mục có đủ > 4 ảnh không
    if len(files) > 4:
        # Tạo file zip
        zip_path = os.path.join(output_zip_dir, f'{zip_counter}.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in files:
                # Nếu file là file ảnh
                if file.endswith('.jpg') or file.endswith('.png'):
                    # Thêm file ảnh vào file zip
                    img_path = os.path.join(root, file)
                    zipf.write(img_path, arcname=file)
        
        zip_counter += 1
