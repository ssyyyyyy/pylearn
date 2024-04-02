import pandas as pd

# 读取Excel文件


data = pd.read_excel('data1.xlsx', sheet_name='Sheet1')
print(data.columns)

# 处理数据，示例中假设你想将'Column1'和'Column2'相加，并将结果保存到'NewColumn'
data['NewColumn'] = data[sheet'A'] + data[sheet'B']

# 进行其他数据处理操作，可以根据你的需求进行操作

# 将处理后的数据保存回Excel文件，保存的列为'Column1'、'Column2'和'NewColumn'
data[['Column1', 'Column2', 'NewColumn']].to_excel('output.xlsx', index=False)
