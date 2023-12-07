import os
import shutil
import requests
import re

arrApiKey = [
    'SK03EIjA39xx2dqRn0gYKmAjFAp6lfrY',
    'G0Ejq02dETQUOF8elPYIUhRw4uAE8GI1',
    '32v9U5VjYxsCS0rNfMvdngAJwP3HEPO0',
    'ADe4Yf2FMlwMvsZXSzAJ2oXiL7VaDDRS',
    'mfZHSH99BzJJXK5RgPOV0DwDr9xz4q5i',
    'o9ggdaeRIXWInCc63ZV4f74IXVY7iHoX',
    'iFa3OR9Ifzw5PrJFSBDENKEZUTluBEgq',
    'VuujdD28rsr87V4PAQcPnJ9ldZtiNxJJ',
    'xUcZrIzZVRqPgJAuKOnEslzbPNBxc78B',
    'pBG7KwDrYjag2lgJ3GFw82TUE9Wudd2o',
    'ZeyxKqJA1FhLSEsBZk0nSPIXG8ujsgy7',
    'UWPcR2s7KhV224fdUdoQ0VH92MRBB5Yn',
    'ayhftGy9rHsKULwyk6ZTjkV4EJYFekCM',
    '9jnwsCOzOSbv70sD0VpRzP8W0avQsItz',
    '4tpbUKoPuz2RNJmwWYZmzxzG7Tm4HRDx',
    'byBUlPTkD4VfgYGzq6Y6bMiqqVo3FlGo',
    'FsRjECzriLJHfkjD5KqQCquYFkE11gfo',
    'fVfj3KdphLeF2Ten3sPkUZiI0ak3wAJy',
    'vCIkrNvDDL83DBT45HMZm2LiE7S5kexQ',
    'YSEWONWlMCazU5rXfWzn3vD1w7qgrYnM',
    'qpW997JjRcy58waI4BaVfX7eJUMHoLqC',
    'u1t7vMHPEV7wXvPF3Or1Hqi0KcTlCFHx',
    '9rSRjohFedSshDX5MdEhJebB921Kr1zb',
    'hK497nGs3F47sSe9YttaNgCehuqtmp6A',
    'py2YXx9E2DJg3hc20rla0c99hGeyOsdf',
    'KB8blmSWU2s2pxAJCQYaan9IOf8XuB3n',
    'qhcJeu5poM5OjtLu6VCf6BLUldmwOMyL',
    'lYWn8Ebi44OA1S76QUT2vF9ArA1qD2bo',
    'Yug8VIWtPlWFASpsnBIabPKpMgr3dG1v',
    'TjiJwDQHF4pK7LSl7DHoO4Lo0dTfPcKQ',
    'txvv1bJapxxsexzcmhXiUQVuglp7KFB3',
    'c7r0I88dGRFc6MOG8SWMIr5OWf5M6Fbk',
    'O6Rch0LRhOj4595aL5XN94tbC6oL5KC8',
    'NTRbqGPRCf9Kbb1mr3bMOg4e2OYsbnZ3',
    'STJ3XnszxIKpDvSzpvgLi4FazMJQ8buH',
    '4cfbRV8EjfaZWyUpbcT10M1jp1Bld2GC',
    'JcJsJxiCgQkc6R53glCcUYCtmvEXV1Dv',
    '3C8yDLou6wwV9up9WZM1cg7SNqKKBCoG',
    'tDzz3oPUXzfri4MGDhH4Gyx20Ck6GMPE',
    'oPp70kbLUov9vhXR5A8PjwBG9zuDqSWY',
    '4RTm0R2mPjLM5DUATksUJ4oA7LjrPcnm',
    'ZJtKBFpTTAdvZqPJMeuNS8SYsCMYc2aS',
    'FDnUQYU3spMtkPwA9BS24EmCuhjm9Q89',
    'ef62MF0cd94SO6ccjuhlS1YgsS4BHc1c',
    'ufOPFB4MThlONPQXCuSTZGogW9n2PqSn',
    'pvH7ylQsOvHmTZFnokLDmMx5ur1l1J7H',
    'NDL3cg08nGfYTmppfOyrLOeHQdtFiALV',
    'kSkAYxazDuZilJGJR0eCMc9FlYvV82vo',
    'QUwNdELDUdkLup7E8ZPz6L0HLLRhyvDJ',
    'e52ON4kebhSQIsxjOpZWkP5p8li31RRQ',
    '1X1krQdIZ3UpeZtKqIGIg8xHZsKqwpzI',
    'KRBST0oELujqTj7Oj0wIEL0CFZhk3Tk8',
    'CNLRzWWb8b3efbeDmFMk0UpGWbhYrBsF'
]

  
def process_images_in_directory():
    index = 62
    directory = "passport"
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if is_image(file_path):
            new_filename = str(index) + os.path.splitext(filename)[1]  # Đổi tên file thành số thứ tự
            new_file_path = os.path.join(directory, new_filename)
            # shutil.copy2(file_path, new_file_path)  # Ghi đè lên file đã tồn tại (nếu có)
            try:
                callAPIToGetResult(new_file_path, arrApiKey)
            except Exception as e:
                print(f"Lỗi xảy ra khi gọi API: {str(e)}")
            
            index += 1

def is_image(file_path):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
    file_extension = os.path.splitext(file_path)[1].lower()
    return file_extension in image_extensions

def callAPIToGetResult(image_path, api_keys):
    if not api_keys:
        print("Không có api-key khả dụng.")
        return
    
    url = 'https://api.fpt.ai/vision/passport/vnm'

    files = {'image': open(image_path, 'rb').read()}
    headers = {
        'api-key': api_keys[0]
    }
    print("Run with api key: " + api_keys[0]);
    response = requests.post(url, files=files, headers=headers)
    
    if response.status_code == 200:
        # Tạo thư mục con trong thư mục "output" với tên là tên file ảnh
        image_name = os.path.basename(image_path)
        output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                                        re.sub(r'[^\w\-_. ]', '', os.path.splitext(image_name)[0]))
        os.makedirs(output_directory, exist_ok=True)

        # Copy ảnh gốc vào thư mục con
        shutil.copy(image_path, os.path.join(output_directory, image_name))

        # Tạo file detail.json và ghi nội dung response.text vào file
        detail_file_path = os.path.join(output_directory, "detail.json")
        with open(detail_file_path, "w") as detail_file:
            detail_file.write(response.text)

        print("Ghi thành công dữ liệu vào thư mục output.")

    elif response.status_code == 400:
        print("Gọi API không thành công. Lỗi 400 - Bad Request.")
        return

    else:
        print("Gọi API không thành công. Thử lại với api-key khác.")
        api_keys.pop(0)  # Xóa vị trí đầu tiên trong api_keys
        if len(api_keys) > 1:
            
            callAPIToGetResult(image_path, api_keys)
        else:
            print("Không còn api-key khả dụng.")
    
process_images_in_directory();