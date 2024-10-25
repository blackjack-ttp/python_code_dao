"""
Thống kê từ vựng: Viết một chương trình để đếm tần suất xuất hiện của mỗi từ trong một văn bản và trả về 
một danh sách các từ cùng với số lần xuất hiện của chúng, được sắp xếp theo thứ tự giảm dần.
"""

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

text = input("Nhập một văn bản: ")
print("Tần suất xuất hiện của các từ:", word_frequency(text))
