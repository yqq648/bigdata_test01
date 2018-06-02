# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:14:50 2018
{
“地址”:"北京海淀区xxxx",
“手机号码”:"15010159566",
"寄信人":"chance"
}
@author: yq
"""
msg = {"地址":"北京海淀区xxxx",
 "手机号码":"15010159566",
 "寄信人":'chance'}

print(msg["地址"])
print(msg['手机号码'])
print(msg['寄信人'])
#题目，写一个字典类型，表示一个人的基本信息
#姓名，身高，性别，年龄
"""
dict(key:value,key,value,.........)
"""
xzhq={'name':'薛之谦',
      'songs':['特别辣','演员','暧昧','认真的雪'],
      '昵称':'xiao薛',
      '认识过女朋友':[2,1,3,8,-1]}
songs=xzhq['songs']
print(songs)
print("歌曲总数:"+str(len(songs)))#len()求列表长度的函数
print(max(xzhq['认识过女朋友']))#max求列表中最大的数
#天气 ,未来5天天气温度list, 未来5天的情况list,今天星期几
#用字典写出天气信息，并且查询最高温度是？

    





















