# py日志切割
import datetime
import os


def cut_log():
    date = datetime.datetime.now().date() - datetime.timedelta(days=1)
    date = date.strftime('%Y-%m-%d')
    os.system('cp /data/log/nginx/access.log /data/log/nginx/access.log.%s' % date)
    os.system('echo '' > /data/log/nginx/access.log')

    os.system('cp /data/log/nginx/error.log /data/log/nginx/error.log.%s' % date)  # 按天把日志归档
    os.system('echo '' > /data/log/nginx/error.log')  # 将原来的文件清空


def rm_old_log():
    start = datetime.datetime.now().date() - datetime.timedelta(days=15)
    start = start.strftime('%Y-%m-%d')
    os.system('rm /data/log/nginx/access.log.%s' % start)
    os.system('rm /data/log/nginx/error.log.%s' % start)


# 使用Linux的cron每天调用这个py即可
if __name__ == "__main__":
    cut_log()
    rm_old_log()
