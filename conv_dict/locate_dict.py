# -*- coding: utf-8 -*-
'''
#======================================================================
#     FileName: locate_dict.py
#         Desc: 定位字典中字母位置
#       Author: Xuan Four (xuanfour@qq.com)
#         Link: http://xuanfour.github.io
#      Version: 0.0.1
#   LastChange: 2014-04-22 21:59:18
#      History:
#======================================================================
'''

import os
import logging
import codecs

import conv_dict as cvd


def main():
    ''' 定位字典中字母位置 '''
    # 初始化日志及获取文件路径
    cvd.init()
    logger = logging.getLogger('simple')
    # 字典项格式
    workdir = os.path.dirname(__file__)
    trgtfn = os.path.join(workdir, cvd.DICT_DATA_PATH, cvd.DICT_TRGT_FN)
    trgtfn = os.path.normcase(trgtfn)
    trgtfile = codecs.open(trgtfn, 'r', cvd.DICT_TRGT_CODING, 'ignore')
    start = 97
    lineno = 1
    rec = ''
    try:
        for line in trgtfile.readlines():
            if ord(line[0]) == start:
                rec = rec + str(lineno) + ', '
                start = start + 1
            lineno = lineno + 1
    except Exception as ex:
        logger.error(line + ' ' + ex)
    finally:
        trgtfile.close()
        logger.info('rec: ' + rec)
        logger.info('Sign Out')
        print('操作完成。')


if __name__ == '__main__':
    main()
