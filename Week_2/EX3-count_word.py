file_path = './P1_data.txt'


def count_word(path):
    # Mở file và đọc nội dung vào biến string
    with open(path) as f:
        string = f.read()

    # Chuyển đổi tất cả các ký tự trong nội dung thành chữ thường và tách thành danh sách các từ
    string = string.lower().split()

    # Đếm số lần xuất hiện của từng từ và trả về một dictionary
    return {word: string.count(word) for word in string}


# In ra kết quả đếm số lần xuất hiện của mỗi từ trong FILE_PATH
print(count_word(file_path))
