import os
import json
import datetime
import requests


def generate_output_string(data, dir_out):
    try:
        
        #a Korean female, age 40, with a long face and short tied hair . The photo is in slight lighter-dark-tone colors and shows an eye view of the subject in a half-body shot, standing on the floors of an airport with a blurred background.
        if "data" in data:
            data_list = data["data"]
            if len(data_list) > 0:
                current_year = datetime.datetime.now().year
                sex = data_list[0].get('sex','').split('/')[0]
                national = data_list[0].get('nationality', '');
                birthYear = data_list[0].get('dob', '').split('/')[2] or "1980";
                age = current_year - int(birthYear)
                output_string = f"a {national} {sex}, age {age} with travel-appropriate attire. The photo is in slightly brighter tone and shows an eye view of the subject in a half-body shot, standing on the floors of an airport with a blurred background. --ar 2:3 --v 5";
                # Định nghĩa URL của API POST
                url = 'http://localhost:3000/imagine'
                body = {
                    'imagine': output_string
                }
                # Gọi API POST và nhận response
                response = requests.post(url, json=body)

                # Kiểm tra và in ra response
                if response.status_code == 200:
                    uri = response.json().get('uri', None)
                    if uri:
            # Gửi yêu cầu GET để tải xuống file ảnh từ URI
                        image_response = requests.get(uri)
                        if image_response.status_code == 200:
                            # Lưu file ảnh vào thư mục "output"
                            file_name = os.path.join(dir_out, "z-download.png")
                            with open(file_name, 'wb') as file:
                                file.write(image_response.content)
                            print("File ảnh đã được tải xuống và lưu vào thư mục " + dir_out)
                        else:
                            print("Không thể tải xuống file ảnh.")
                else:
                    print("Đã có lỗi xảy ra khi gọi API.")
                return output_string
    except Exception as e:
        print(f"Lỗi trong quá trình xử lý dữ liệu: {str(e)}")
    return ""

def process_output_directory(directory):
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            detail_file_path = os.path.join(subdir_path, "detail.json")
            if os.path.isfile(detail_file_path):
                with open(detail_file_path, "r") as detail_file:
                    try:
                        detail_data = json.load(detail_file)
                        output_string = generate_output_string(detail_data, subdir_path)
                        print(output_string)
                    except Exception as e:
                        print(f"Lỗi trong quá trình xử lý file JSON: {str(e)}")
                        continue

def main():
    output_directory = "output"
    process_output_directory(output_directory)

if __name__ == "__main__":
    main()