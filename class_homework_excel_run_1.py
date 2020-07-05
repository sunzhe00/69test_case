# -*- coding:utf-8 -*-
# @time   :2020/6/30  11:23
# @Author :sunzhe
# @Email  :15967579213@163.com
# @File   :run.py
#读取文件
from class_recharge.class_homework_R_W_excel_1 import read_data
from class_recharge.http_Request_case_1 import http_request
from class_recharge.class_homework_R_W_excel_1 import write_data
Token = None  #全局变量设置为None
user_id = None
def case_run(file_name,sheet_name,column_num_1,column_num_2):
    global Token   #函数外的Token和函数内的Token是同一个值
    global user_id
    all_case = read_data(file_name,sheet_name)
    ip = 'http://120.78.128.25:8766'
    for data_case in all_case:
        response = http_request(ip + data_case[4], eval(data_case[5]),Token,data_case[3])
        if 'login' in data_case[4]:  #判断是不是login用例，如果是提取出来Token和id
            Token = 'Bearer '+response['data']['token_info']['token']
            user_id = response['data']['id']
        print(response)
#写入测试用例
        write_data(file_name,sheet_name,data_case[0]+1,column_num_1,str(response))
        actual = {'code': response['code'], 'msg': response['msg']}
        if eval(data_case[6]) == actual:
            write_data(file_name, sheet_name, data_case[0]+1,column_num_2,'PASS')
        else:
            write_data(file_name, sheet_name, data_case[0]+1,column_num_2,'FAIL')
# #执行充值
case_run('login_test_1_1.xlsx','recharge',8,9)
# #执行注册
# case_run('login_test_1_1.xlsx','register',8,9)
