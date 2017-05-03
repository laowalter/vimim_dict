# -*- coding: utf-8 -*-
'''
#======================================================================
#     FileName: common.py
#         Desc: 公用模块
#       Author: Xuan Four (xuanfour@qq.com)
#         Link: http://xuanfour.github.io
#      Version: 0.0.1
#   LastChange: 2014-04-20 21:31:52
#      History:
#======================================================================
'''


def ischinese(uchar):
    '''
    判断一个unicode是否是汉字
    一般用4E00－9FA5已经可以，如果要更广，
    则用2E80－A4CF  ||   F900-FAFF　||　FE30-FE4F
    '''
    return (uchar >= '\u4e00' and uchar <= '\u9fa5') or \
        (uchar >= '\u2e80' and uchar <= '\ua4cf') or \
        (uchar >= '\uf900' and uchar <= '\ufaff') or \
        (uchar >= '\ufe30' and uchar <= '\ufe4f')


def isnumber(uchar):
    """判断一个unicode是否是数字"""
    return uchar >= '\u0030' and uchar <= '\u0039'


def isletter(uchar):
    """判断一个unicode是否是英文字母"""
    return (uchar >= '\u0041' and uchar <= '\u005a') or \
           (uchar >= '\u0061' and uchar <= '\u007a')


if __name__ == '__main__':
    print('begin common ...')
    print('end common')
