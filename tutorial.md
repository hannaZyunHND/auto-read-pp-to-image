# Chuẩn bị: 
1. Cài đặt môi trường python 3.12
2. Nodejs 18.18.0
3. Blue Stack 5
4. Các app đã crack, viết riêng đặt trong thư mục `Require App`

# Cấu hình lần đầu Blue Stack
1. Cài đặt cấu hình điện thoại Samsung Galaxy S22 Ultra
2. Màn hình xoay dọc, độ phân giải 900 x 1600
3. Cài đặt phần mềm Reface.apk đính kèm trong code, đặt ở grid cột 3, hàng 1'
4. cài đặt phần mềm delete-image.apk đính kèm trong code, đặt ở grid cột 1, hàng 2
5. Khởi chạy phần mềm DeleteImage, ấn nút button 1 lần để cấp quyền
6. Khởi chạy phần mềm Reface như bình thường, chạy một lần đầu tiên bằng tay để cấp quyền. Ở phần Choose from device, chọn `Hiển thị bộ nhớ trong` để đọc được các file trong thư mục `Picture`. Cấp quyền ở lần chạy đầu tiên.
7. Tại phần mềm Reface, ở màn hình chính, chọn dấu Setting ở góc cao bên phải màn hình, chọn Earse data để xóa trắng dữ liệu (nhưng không làm mất phân quyền)
8. Cài đặt marco `marco-clear-final` trong code đính kèm

# Cấu hình chạy tạo ảnh từ passport 
1. Chuẩn bị hình ảnh Passport. Lưu ý hình ảnh phải đảm bảo không bị che mặt và không được có đồng thời 2 khuôn mặt; hình passport thể hiện rõ chuỗi mrz.
2. Đặt tất cả ảnh passport với đuôi ảnh jpg vào thư mục `passport` trong code
3. Chạy file runNode.bat để kết nối đến API của Midjourney
4. Chạy file runPython.bat để tự động sinh nguyên liệu chạy deepfake.
5. Quá trình này tùy thuộc vào khối lượng dữ liệu, tốc độ mạng, tốc độ chạy của API... Cứ cắm máy chạy thôi
6. Sau khi quá trình tạo ảnh hoàn thành, kiểm tra thư mục output_zip xem có các file nén bao gồm ảnh passport gốc và 4 ảnh do AI sinh ra

# Khởi chạy với BlueStack
1. Trên màn hình gốc, chọn `Ứng dụng hệ thống/Trình quản lý thư mục`
2. Chọn chức năng `Import from Window`
3. Nhập tất cả cac file nén ở phần trên vào máy ảo
4. Xóa toàn bộ các phần mềm đang chạy, sau đó tiến hành chạy marco `marco-clear-final` đã setup trước đó
5. Phần mềm sẽ tự động chạy đi chạy lại liên tục nhiều lần để đảm báo tính ổn định, không bị tràn RAM. Khi Bluestack đang chạy, có thể ẩn đi nhưng KHÔNG được tác động gì lên màn hình (nếu cần sử dụng máy tính). Trung bình 4p sẽ deepfake được 1 người.

# Xuất dữ liệu đã xong
1. Trên màn hình gốc, chọn `Ứng dụng hệ thống/Trình quản lý thư mục`
2. Chọn thư mục `Explore/output_zip`. Tất cả kết quả được lưu tại đây, với tên được đặt theo thời gian `năm_tháng_ngày_giờ_phút_giây` hoàn thành.
3. Ấn giữ vào 1 item bất kỳ, khi hiển thị dấu chọn thì ấn `Chọn tất cả`
4. Chọn phần `Export to Window` ở góc dưới bên trái. Chọn thư mục lưu trữ trên window. 
5. Các file output_zip trong máy ảo có thể xóa đi được
6. Các file output sẽ có thêm thử mục `Reface` bên trong và số lượng ảnh có thể chỉnh sửa được dao động từ 1->4 ảnh từ các ảnh do Midjourney sinh ra cho mỗi người
