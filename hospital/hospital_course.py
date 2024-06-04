import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('hospital_course_info.csv')

from jinja2 import Environment, FileSystemLoader

# 设置模板环境
env = Environment(loader=FileSystemLoader(searchpath=''))
template = env.get_template('hospital_template_with_css.html')

# 显示 DataFrame 的前几行
#print(df.head())
#print(df.iloc[:, 3])
# 使用列数来动态获取第四列

cateloge_name=''

for i in range(3,len(df.columns)):
    course_info={}
    course_info['Orientation']=[]
    course_info['Week1']=[]
    course_info['Month1']=[]
    course_info['Month2']=[]
    course_info['Month3']=[]
    course_info['Month12']=[]
    course_info['Task_Related']=[]

    #print(df.iloc[:, i])
    
    if df.iloc[0, i]!='NaN':
        cateloge_name=df.iloc[0, i]

    role_name=''
    role_name=df.iloc[1, i]

    for ii in range(2,len(df)):
        if df.iloc[ii, i]=='1' or df.iloc[ii, i]=='t':
            new_course = {'link':df.iloc[ii, 1], 'name':df.iloc[ii, 0]}
            #print(new_course)
            time_line = df.iloc[ii, 2]
            #print(time_line)
            course_info[time_line].append(new_course)

    html_content = ''
    html_content = template.render(cateloge_name = cateloge_name, role_name=role_name, course_info = course_info)
    with open(f"{i}-{cateloge_name}.html", 'w') as file:
        file.write(html_content)
#    print()  # 为了更清晰地分隔输出
    #break


#print(course_info)
