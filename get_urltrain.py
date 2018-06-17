from station import stations
import warnings


def change_date(d1) :
    if '.' in d1 :
        d1 = d1.replace('.', '-')
    if not d1.startswith('0') :
        d1 = str(0) + d1
    if '-' in d1[-2] :
        d1 = d1[:-1] + '0' + d1[-1]
    return d1


def student_or_not(student) :
    if 'y' in student[0].lower() :
        return '0X00'
    else :
        return 'ADULT'


f1 = input('请输入开始城市：\n')
f = stations[f1]

t1 = input('请输入目的城市：\n')
t = stations[t1]

d1 = input('请输入出发时间：\n')
d = str('2018-') + change_date(d1)

student = input('是否为学生票，输入（yes/no）')

print('正在查询' + f1 + '至' + t1 + '的列车，请听听音乐......')
url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={d}&leftTicketDTO.from_station={f}&leftTicketDTO.to_station={t}&purpose_codes={student}'
url = url.format(f=f, d=d, t=t, student=student_or_not(student))
warnings.filterwarnings("ignore")