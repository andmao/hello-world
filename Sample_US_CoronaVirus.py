import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('/Users/andmao/Desktop/PyTest/US.xlsx',sheet_name='1')
df

fig = go.Figure(data=go.Choropleth(
                                    locations = df['code'],# 设置位置，各州的编号（缩写）
                                    z = df['conNum'].astype(float),# 设置填充色数据
                                    locationmode = 'USA-states',# 设置国家名称
                                    colorscale = 'Reds',# 图例颜色
                                    colorbar_title = '人数'# 图例标题
))

fig.update_layout(title_text='美国累计确认人数',# 地图标题
                    geo_scope='usa',# 设置地图的范围为美国
                    )

#导出地图为html文件
fig.write_html("/Users/andmao/Desktop/PyTest/US.html")

