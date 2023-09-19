def contains_consecutive_substring(s):
    char_count = {}
    
    # 遍历输入字符串中的每个字符
    for char in s:
        # 如果字典中没有这个字符，添加它并设置计数为1
        if char not in char_count:
            char_count[char] = 1
        else:
            # 如果字符已经在字典中，增加计数
            char_count[char] += 1
            
        # 检查是否有两个或更多相同的字符
        if char_count[char] >= 2:
            return True
    
    # 如果没有找到两个或更多相同的字符，返回False
    return False

# 使用示例
str=input("string:")
print(contains_consecutive_substring(str))

