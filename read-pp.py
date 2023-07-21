import os
import shutil
import requests
import re

arrApiKey = [
    'JJTrO0WrN000P3ayBQSn2KMCq0x8O70H',
    'V05sRGPm0SpFc4BYBN0eItaqhU03T0fi',
    '2yZkh6HxWCJ0V3aQPv0xbrZ11UAYpb0f',
    'JFqiFUyzVIetZMH8iIVnK3lpYHLxwgNi',
    '1gUyVAdXDNlbdtKG0dAHff4kulApIrZl',
    'S4EEXDDNJTK4EKKjrrwIpp7l1XRxCoZQ',
    'G9g0eN8UUnnMCk0ND2YtXxyY4KC7xwC8',
    'WpvBzMOzxPqn7ysuqnHVk9Gt9VyDvzaj',
    'a2Y4Ydi8A4x4AwGqMgRcrYsPg4I41Le4',
    'FCpPsRCGRtcygPCProblWK253RvR40z0',
    'MKxZXxFEo7LlCM8uKiCNbgl00pYRFaIM',
    'pcbkoq9eGaiCJrvCMJ0fV03ftso0XwaO',
    'lN1pKOV70QH1RJSsM22l5RN8NMgc58jS',
    '0C1rZEcMtNWEABx7I58QElOVsKN802vF',
    'Uwiq6qtGqPJDBJzsW0R6zh7rK1f78qv4',
    '0wHJ3Is76FfiU7pkGu3H5yDWWh7GmxCo',
    'Mw66cpiz4FyX6HatRNHEhU7iBVijnNSA',
    '0dnj62PQMYA8T5avCArmHfEcfcz9HUBh',
    '84HYpK3tEvHoEVnh4yLOqBo9OzN0LV5N',
    '2pgM0A3o6oDppY3uGRe0V9oE2hXZeOBP',
    '2D7rdEQplrNF1hOoLUlpB2qGXdjELZqS',
    'CZaIuttzxSIQrUXqy1ZZP82EQIhC8tbZ',
    'M9WUZJieJFpGTaozx2CTMJaIV6glHlki',
    '1fRv1Ja8PCY5N461Y5eB3sMpVsULBDd0',
    'PIq8VSdohuHlhBtdkeHFX2cJk5xULPLK',
    'kUz6yPwo4aAzJP7yonpPOj7UmMUQh9UX',
    '5OrRLHIp6oS2F4c5y5GkKJFfcoyzW53F',
    'tqYR6g9QZ1zRZlZvE62gP5yzdkjT2QQi',
    'UZf0Z644gS9R2OQr2QiNUkLbOzS1DAkx',
    'HW9vSBqD0Me8MHNf1q3TTXOdObxQAtij',
    'Gzhpo4MgdGLL0IqfSj8m8gyCALu6UChK',
    'k0ICFH19x0y5jzuTqnviCbsor8WjQKei',
    'oUilSi0dNfrOgGaDk8hJJgTvjmCiQQLg',
    '1Pgt4QjtXlw9DPC4tnPUSKuUnvwTeIET',
    'LaO4NpxYo832p8WZaIUKb80qbyICTCbp',
    'LGCYI8IV4UHctldPVF2BgbiyxJZKuVkD',
    'uGGqRe5cNbVeeWfm9pMvn0yw9Juw7xvN',
    'XBTMt2WqjuXsygMIvjSecR64I53GB691',
    'YuFYI7RKyFIziSmq4zk9o9VICEGiHerw',
    'LGq5W0QR2KUHlUV3Hg8uSQUOlCMot3Ea',
    '9E0D6HxK9KZ0nDEIshsU6N85pNoll328',
    '0IYI1w8wye8NjanrczJNXMxVIblYqTAe',
    'acxMCW3HGmGSlumEPQxvxhSfzsanDe5T',
    '2XOnFg3JGVTn20s2geeqfUx1svrh8mBX',
    'pqqT2rBzPqgcNwWr7Jp5n9B0G6iuXaK4',
    'Caa8W1W91qtU9xtP8cLGuqB9g9zXYfX1',
    'tybtTrQdgTLDFc9YtH8VVPp48b45xOwy',
    'LRy1X2fZ3ZII3yT3MVN5D09IL6gyQPja',
    'TIs4JKaUcmfROG3XoqSg2hIRRJgq3TK3',
    'DCaaYYG9c8oDvjiORg9yuF1l4zobulbx',
    'h9myMGEhIQKx7JVw7scIWYS1KjT7lsuw',
    'U2838trPLVPXC78u7lYVfL1Z8utDeHWD',
    'FZBoEQJ5ruIwy5ZyOBysgFnBy3iewuG5',
    'MsIm8mRWmgVtvoPSgV43h2P01K9YwBiX',
    'aMJFyRDZD0KBErctgx0SwExAwMw6eKDu',
    'XpNBDtsd3c1byAATwLtlmt133w0lNvLh',
    'wo7zK8gKP2jZcrWQ2z9kVLIawhvfa0gw',
    'C1fiSPcyylB5mvjQslgbFu3IMv69rHhg',
    '2fGcHK2Oa2NE4CJMA2cmR1QizmxC8KI0',
    'y94WP9rcMg2RRMcYcXtq0JRBxZLq9DEL',
    'oViRXqDW1k6q10RZDYaCVMpuaVyMrfhW',
    '2i779PrkuPO808WzPCePjtfM9ixlgv1V',
    '43Yrnsv96VNoEhry1cBbNBpSCw6ANFa8',
    '3IyH6pjmKd0x2RTGY1MiousmedzLY67q',
    'syCO9OFCFQmrGtQZjXyrCvAWRRT9coZC',
    'S9VTWY6HJ8eUtFdDan8nPJA1lTQg1U0p',
    'VekGl8GaORXrb8hEyeMXW43AIqxkv2Ir',
    'znrBrW11dS0pRKwIzKGVODO03PVzpBgF',
    'mktdPXGdXsBLGbEk3eTAKFEDfCBIbFLK',
    'GRmB2INSCDlWkeY25wBsGmoQFnk2ND1p',
    'YncxDn7eRJrpfBS3GpzNdufwXRDtJWTS',
    '8G5tNSEbpd3YdFfKPMpUDYdYZ3moNPGO',
    'dax6VFs38RwW6FeXTdItKTB7YR2pMqjN',
    'fZMlR0LbT13lQs6cAepfN9BT1XsM9JW9',
    '0toVKDekbmjJas2CoCROs8uL0OsibRUl',
    'ssQhdH29BqM1qfDBoF68ZHL6TmmT8nVR',
    'IeZ45TKox7jXKfJhqqVm2LJi5BWoyGlF',
    'DiaTALBLv087ZVYJ7PG1KrBrfMyCUuar',
    'JQCt6BVBME9U0Scj5CsFVeJb7uz3IMiy',
    '2sKLWhilFJAytdt88ZcOBfxHgW8s8SXY',
    'p2dRr8NaNt8vTvpTHHnRyFXfPvETKPsq',
    'ODtPfQE8d471BUCfqWH9dcN1wrv5m7tT',
    '9pclM0b4IXRULKytIIP9GUTyEduKWwHZ',
    'EuKzNwDvXOoydr3kzaedfSaTnwv5PzZD',
    '3iCeAZavl79AZGZTNTeZegwJ2Lhg2pyq',
    'u9MqV5hHpeVKxGs2Ye8alh22m1nZZWgj',
    'bobUKxX6x5nNnoCowuyI6O9lIUPB31Cb',
    'jo2NK7sq7LSukqX2YgyBK1iTNnqv0J9Q',
    'YoNaySOGrxZ7uJQ2O2fGBY9XM66hsnQU',
    'Aiu4oCbk1xsPYXm6geEUH36n0QBLdDlp',
    'PkWnqq5tvfbaTLSLmoDhfmntNZ7g69Zf',
    'WlgJwqzj76yWlNSVPIGOAhEWJPEnrNIj',
    'AKyyDnlSmkO5H2Wi1Wp2tAF95rjwhPLa',
    'UHAcpOzvF6MRjcRyeZf3IoeSY6k6ZUVK',
    'bAYOCucCUVRkQoL1GzwCuHHRSvQGuONy',
    '7Qcsg6x7OGrMAQl3mIld3p3uqF1Eb4jT',
    'WY0rv21GZWvYlauOdXdsyLeXhvG2Peqi',
    '738rXeBMadLgfiMMeQmRlX82I0KJSJKk',
    'NwjHr6ghMoJgoRZYA8zcgyrJjMHlPbz5',
    'acoUYz3hlqC6XKzBhOJbmU36Vw00sKJn'
]

  
def process_images_in_directory():
    index = 62
    directory = "1876-bk"
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if is_image(file_path):
            new_filename = str(index) + os.path.splitext(filename)[1]  # Đổi tên file thành số thứ tự
            new_file_path = os.path.join(directory, new_filename)
            shutil.copy2(file_path, new_file_path)  # Ghi đè lên file đã tồn tại (nếu có)
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