import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('hospital_course_info.csv')

# 显示 DataFrame 的前几行
print(df.tail(5))
#from jinja2 import Environment, FileSystemLoader

# 设置模板环境
#env = Environment(loader=FileSystemLoader(searchpath=''))
#template = env.get_template('template.html')
# 输出列名和列数
print("列数:", len(df.columns))

#print(df.iloc[0:3, 0])
# 遍历每一列，并打印出列名和数据
#for i in range(0,len(df.columns)):
#    print(df.iloc[1, i])
#    html_content = ''
#    html_content = template.render(name=df.iloc[0, i], link=df.iloc[1, i])
#    with open(f"{df.iloc[0, i]}.html", 'w') as file:
#        file.write(html_content)
#    print()  # 为了更清晰地分隔输出
#    break
