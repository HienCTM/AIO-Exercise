from collections import deque


def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []

    if k == 1:
        return num_list

    deque_index = deque()
    max_values = []

    for i in range(len(num_list)):
        # Loại bỏ các chỉ số nằm ngoài cửa sổ trượt hiện tại
        if deque_index and deque_index[0] < i - k + 1:
            deque_index.popleft()

        # Loại bỏ các chỉ số mà giá trị tương ứng nhỏ hơn num_list[i]
        while deque_index and num_list[deque_index[-1]] < num_list[i]:
            deque_index.pop()

        # Thêm chỉ số hiện tại vào deque
        deque_index.append(i)

        # Cửa sổ trượt bắt đầu từ chỉ số k-1
        if i >= k - 1:
            max_values.append(num_list[deque_index[0]])

    return max_values


# Sử dụng ví dụ:
num_list = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(num_list, k))  # Output: [3, 3, 5, 5, 6, 7]
