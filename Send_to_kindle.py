import os
import sys
import shutil
import zipfile
from datetime import datetime

def valid_file(each=''):
    if not (each[(each.rfind('.')+1):] in ['doc','docx','rtf','htm','html',\
                                     'txt','mobi','jpg','bmp','png','pdf']):
        shutil.move(each,'./InvalidFormatFile')
        return False
    if os.path.getsize(each) >= 40*1024*1024:
        shutil.move(each,'./TooBigFile')
        return False
    return True

def send(mtitle, to_list='yizhongpku@kindle.cn',cc_list='', a_file=''):
    if cc_list == '':
        clist =''
    else:
        clist= ' -c '+cc_list
    if a_file =='':
        att = ''
    else :
        att = ''
        for names in a_file:
            att = att + ' -a '+ names

    mbody =os.path.normpath(os.path.join(sys.path[0],'config/mail_body.txt'))
    if os.path.isfile(mbody):
        phrase = '''mail -i -s %s -r yizhongpku@163.com%s%s %s < %s '''\
              %(mtitle ,clist, att, to_list, mbody)
        print phrase
        os.system(phrase)
    shutil.move(each,'./sent')
         
if __name__=='__main__':
    lists=os.listdir(os.getcwd())
    lists.remove('InvalidFormatFile')
    lists.remove('Send_to_kindle.py')
    lists.remove('sent')
    lists.remove('TooBigFile')
    lists.remove('config')
    lists.remove('.DS_Store')
    for each in lists:
        if not valid_file(each):
            print '%s is not valid file'%each
        else:
            print 'Trying to send %s...'%each
            eachfile=os.path.join(os.getcwd(),each)
            cclist = ''
            title ="'A new kindle book to read! Send on %s.'"%datetime.strftime(datetime.today(), '%Y%m%d')
            attachment = [eachfile]
        
            if len(sys.argv)<3:
                send(title,cc_list=cclist, a_file = attachment )
            else:
                print 'Email not sent: %s'%(sys.argv[2:])