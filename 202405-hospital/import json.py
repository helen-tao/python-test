import json

# 读取JSON数据
with open('test.json', 'r', encoding='utf-8') as file:
    hospital_data = json.load(file)

# 创建一个模板字符串
template = """
Dear {name},

Your email address {email} has been registered successfully.

Best regards,
Your Team
"""

# 填充模板
output = template.format(**hospital_data)

# 写入新文件
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(output)
