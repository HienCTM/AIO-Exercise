def count_chars(string):
    # Khởi tạo dictionary rỗng để lưu kết quả
    char_count = {}

    # Duyệt qua từng ký tự trong chuỗi
    for char in string:
        # Bỏ qua khoảng trắng
        if char == ' ':
            continue

        # Chuyển ký tự về chữ thường để không phân biệt chữ hoa chữ thường
        char = char.lower()

        # Nếu ký tự đã có trong dictionary, tăng giá trị đếm lên 1
        if char in char_count:
            char_count[char] += 1
        # Nếu ký tự chưa có trong dictionary, khởi tạo giá trị đếm là 1
        else:
            char_count[char] = 1

    return char_count


# Ví dụ sử dụng:
string1 = 'Happiness'
# Output: {'h': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
print(count_chars(string1))

string2 = 'smiles'
print(count_chars(string2))  # Output: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
