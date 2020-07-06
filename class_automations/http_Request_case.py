# -*- coding:utf-8 -*-
# @time   :2020/6/30  13:42
# @Author :sunzhe
# @Email  :15967579213@163.com
# @File   :http_request_case.py

import requests
mobile_phone_user = '15055555328'
mobile_phone_admin = "15055555238"
pwd_user = "52525200"
pwd_admin = "sunzhe00"
reg_url = "http://120.78.128.25:8766/futureloan/member/register"
reg_data_user = {"mobile_phone": mobile_phone_user, "pwd": pwd_user}
reg_data_admin = {"mobile_phone": mobile_phone_admin, "pwd": pwd_admin, "type": "0", "reg_name": "管理员用户lemon"}
log_url = "http://120.78.128.25:8766/futureloan/member/login"
log_data_user = {"mobile_phone": mobile_phone_user, "pwd": pwd_user}
log_data_admin = {"mobile_phone": mobile_phone_admin, "pwd": pwd_admin}
def http_request(url, data, token_user=None, method='post'):  # 因为我的形参一定要放在默认参数的前面
    header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json',
                    'Authorization':token_user}
    if method == 'get':  # 判断是不是get请求，如果是get请求，就返回result
        response = requests.get(url, params=data, headers=header)
        result = response.json()
    elif method == 'post':  # 判断是不是post请求，如果是post请求，就返回result
        response = requests.post(url, json=data, headers=header)
        result = response.json()
    elif method == 'patch':  # 判断是不是potch请求，如果是patch请求，就返回result
        response = requests.patch(url, json=data, headers=header)
        result = response.json()
    return result  # 返回result
if __name__ == '__main__':
    http_request(reg_url, reg_data_user)
    print(http_request(reg_url, reg_data_user))  # 打印调用函数--执行的是注册的普通用户
    print(http_request(reg_url, reg_data_admin))  # 打印调用函数--执行的是注册的管理员用户
    print(http_request(log_url, log_data_user))  # 打印调用函数--执行的是登录的普通用户
    print(http_request(log_url, log_data_admin))  # 打印调用函数--执行的是登录的管理员用户
    token_user = http_request(log_url, log_data_user)['data']['token_info']['token']  # 取user的token
    user_id = http_request(log_url, log_data_user)['data']['id']  # 取user的id
    token_admin = http_request(log_url, log_data_admin)['data']['token_info']['token']  # 取admin的token
    user_header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json',
                       'Authorization': 'Bearer ' + token_user}  # 取user的请求头
    admin_header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + token_admin}  # 取admin的请求头
    recharge_url = "http://120.78.128.25:8766/futureloan/member/recharge"  # 充值的数据
    recharge_data = {'member_id': user_id, 'amount': 50000}
    print(http_request(recharge_url, recharge_data,'Bearer ' + token_user))  # 调用函数--普通会员进行执行充值
    withdraw_url = "http://120.78.128.25:8766/futureloan/member/withdraw"  # 提现的数据
    withdraw_data = {'member_id': user_id, 'amount': 5000}
    print(http_request(withdraw_url, withdraw_data,'Bearer ' + token_user))
    add_url = "http://120.78.128.25:8766/futureloan/loan/add"  # add加标
    add_data = {"member_id": user_id, "title": "购买全栈测试课程_1",
                    "amount": 10000.00, "loan_rate": 1, "loan_term": 1, "loan_date_type": 1, "bidding_days": 1}
    print(http_request(add_url, add_data,'Bearer ' + token_user ))
    loan_id = http_request(add_url, add_data, 'Bearer ' + token_user)['data']['id']  # 加标以后，我要提取标id
        # audit_url = "http://120.78.128.25:8766/futureloan/loan/audit"  # 审核的数据
        # audit_data = {"loan_id": loan_id, "approved_or_not": "true"}
        # print(http_request(audit_url, audit_data, admin_header, 'patch'))  # 打印 审核信息
    # invest_url = "http://120.78.128.25:8766/futureloan/member/invest"  # 投资的数据
    # invest_data = {"member_id": user_id, "loan_id": loan_id, "amount": "100"}
    # print(http_request(invest_url, invest_data, 'Bearer ' + token_user))
    name_update_url = "http://120.78.128.25:8766/futureloan/member/update"  # 用户更新昵称数据
    name_update_data = {"member_id": user_id, "reg_name": "潇洒哥"}
    print(http_request(name_update_url, name_update_data, 'Bearer ' + token_user, 'patch'))  # 打印昵称修改
    user_info_url = 'http://120.78.128.25:8766/futureloan/member/' + str(user_id) + '/info'  # 咱们用拼接
    print(http_request(user_info_url, None, 'Bearer ' + token_user, 'get'))
    loans_list_url = "http://120.78.128.25:8766/futureloan/loans"  # 标项目列表
    header_2 = {"X-Lemonban-Media-Type": "lemonban.v2"}
    print(http_request(loans_list_url, None,None,'get'))
