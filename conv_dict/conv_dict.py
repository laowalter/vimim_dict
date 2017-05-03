# -*- coding:utf-8 -*-
'''
#======================================================================
#     FileName: conv_dict.py
#         Desc: 转换小鹤双拼码表到 VimIM_Dict
#       Author: Xuan Four (xuanfour@qq.com)
#         Link: http://xuanfour.github.io
#      Version: 0.0.1
#   LastChange: 2014-04-20 21:10:34
#      History:
#======================================================================
'''

import os
import logging
import logging.config
import codecs

#import common

# 数据目录
DICT_DATA_PATH = 'data'
# 源文件
DICT_SRC_FN = '导出 - 主码 -  系统词库.txt'
# 源文件编码
DICT_SRC_CODING = 'utf_16_le'
# 目的文件
DICT_TRGT_FN = 'vimim_dict.txt'
# 目的文件编码
DICT_TRGT_CODING = 'utf-8'
# 日志配置文件名
LOG_CFG_FN = 'logging.cfg'

def init():
    ''' 获得日志对象 '''
    # 当前工作目录
    workdir = os.path.normcase(os.path.dirname(__file__))
    # 得到日志配置
    cfgfn = os.path.normcase(os.path.join(workdir, LOG_CFG_FN))
    logging.config.fileConfig(cfgfn)
    logger = logging.getLogger('simple')
    logger.info('Sign In')

def _printhead(dictfile):
    ''' 打印字典头信息 '''
    dictfile.writelines('#======================================================================\n')
    dictfile.writelines('#     FileName: vimim_dict.txt\n')
    dictfile.writelines('#         Desc: 小鹤双拼输入法码表\n')
    dictfile.writelines('#               可以修改成适合自己的字典\n')
    dictfile.writelines('#       Author: Xuan Four (xuanfour@qq.com)\n')
    dictfile.writelines('#         Link: http://xuanfour.github.io\n')
    dictfile.writelines('#      Version: 0.0.1\n')
    dictfile.writelines('#   LastChange: 2014-04-22 18:55:34\n')
    dictfile.writelines('#      History:\n')
    dictfile.writelines('#======================================================================\n\n')

def _isvalid(ustr):
    ''' 是否合法的字典值 '''
    #if common.ischinese(ustr[0]) or \
       #common.isnumber(ustr[0]) or common.isletter(ustr[0]):
        #return True
    #else:
        #logger = logging.getLogger('simple')
        #logger.debug(ustr + '\n')
        #return False
    return not ustr.startswith('--')

def main():
    ''' 转换小鹤双拼码表到 VimIM_Dict '''
    # 初始化日志及获取文件路径
    init()
    logger = logging.getLogger('simple')
    # 字典项格式
    workdir = os.path.dirname(__file__)
    scrfn = os.path.join(workdir, DICT_DATA_PATH, DICT_SRC_FN)
    scrfn = os.path.normcase(scrfn)
    scrfile = codecs.open(scrfn, 'r', DICT_SRC_CODING, 'ignore')
    trgtfn = os.path.join(workdir, DICT_DATA_PATH, DICT_TRGT_FN)
    trgtfn = os.path.normcase(trgtfn)
    trgtfile = codecs.open(trgtfn, 'w', DICT_TRGT_CODING, 'ignore')
    _printhead(trgtfile)
    linebak = ''
    ensbak = ''
    fmt = '{0:<8}{1}'
    try:
        for line in scrfile.readlines():
            if not line.isspace():
                # 抛弃'#'及后面无用字符
                loc = line.find('#')
                if loc > 0:
                    line = line[:loc]
                    # 判断是否是否合法的字典值
                    if _isvalid(line):
                        codes = line.split()
                        # 如果是有效的两组字符串，就分别处理
                        if len(codes) == 2:
                            chs = codes[0].strip()
                            ens = codes[1].strip()
                            if linebak == '':
                                # 第一次有效数据，备份字典项和编码
                                ensbak = ens
                                linebak = fmt.format(ens, chs)
                            elif ens == ensbak:
                                # 重复编码
                                linebak = linebak + ' ' + chs
                            else:
                                # 写入上次有效数据，同时备份本次字典项和编码
                                trgtfile.writelines(linebak + '\n')
                                ensbak = ens
                                linebak = fmt.format(ens, chs)
                            continue
            # 删除换行，将无效数据写入日志
            line = line.replace('\r\n', '')
            line = line.replace('\n', '')
            logger.info('skip line: ' + line)

        if linebak != '':
            # 写入最后一次有效数据
            trgtfile.writelines(linebak + '\n')
    except Exception as ex:
        logger.error(line + ' ' + ex)
    finally:
        trgtfile.close()
        scrfile.close()
        logger.info('Sign Out')
        print('操作完成。')

def test():
    init()
    logger = logging.getLogger('simple')
    logger.debug('test')
    logger.info('Sign Out')

if __name__ == '__main__':
    main()
    #test()
