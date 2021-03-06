import shelve


class TestSaveCookies:

    def test_cookie1(self):
        # shelve 小型数据库，对象持久化保存方法
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852947263373'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'd6cQRr8tfQjdVQBZ7iwKhAR3v1U1FJSyIxyTMmN0Rgxp2sNOXRRKv0xV5a4F9dQyp21ZMK4ifEU-6KNtGqHN_0OXz1jJT4mpYp_kxYMtgnRyCCaq7Ro4t2alfAA_tz54tvqct1m8ZOT5WBKcR0AmFfD0vbVL8dxLke5BUcPdAYMGmM5nlsOL21EKXb5LU4JoAkf9x5sneziselJM7SSQ4naBi3-en1-ADO8gOBqGw1r4WCX6xHCNfEFFSOhkWSoE7BGiyFu6cYZu2dXfgTeiiA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852947263373'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325123157255'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'KMVYlQsUP-QZ0PiGZVNJYQiXJFOVDeJzaQ8Zwp6I3mBwMDCOHRCP4Vjo1R6BYhPc'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a766949'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598194379, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': 'm8mvh7'}, {'domain': '.qq.com', 'expiry': 1598249255, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1114836802.1598081605'}, {'domain': '.qq.com', 'expiry': 1661234855, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.282616681.1598081605'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629617594, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'e903aa0eb8ba558758748f5702d7f11c6632a54a2ee5e3bc5467d712bad4a951'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629619506, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598081605,1598081621,1598083506'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'pAQQC2DGYu'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600754858, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '4048994415442863'}, {'domain': '.qq.com', 'expiry': 1598162904, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '3822710784'}]

        db = shelve.open('mydb/logincookies')
        # 定义一个cookie在数据库中
        db['cookie'] = cookies
        db.close()
