# -*- coding: UTF-8 -*-
from datetime import datetime
import jdatetime

date_format = '%d/%m/%Y'
month_list = ['01 - Jan',
              '02 - Feb',
              '03 - Mar',
              '04 - Apr',
              '05 - May',
              '06 - Jun',
              '07 - Jul',
              '08 - Aug',
              '09 - Sep',
              '10 - Oct',
              '11 - Nov',
              '12 - Dec']

farsi_weekdays = [
                  'دوشنبه',
                  'سه‌شنبه',
                  'چهارشنبه',
                  'پنج‌شنبه',
                  'جمعه',
                  'شنبه',
                  'یکشنبه',
                  ]

farsi_numbers = ['۰',
                 '۱',
                 '۲',
                 '۳',
                 '۴',
                 '۵',
                 '۶',
                 '۷',
                 '۸',
                 '۹',]

farsi_monthnames = ['ژانویه',
                    'فوریه',
                    'مارس',
                    'آوریل',
                    'می',
                    'ژوئن',
                    'جولای',
                    'آگوست',
                    'سپتامبر',
                    'اکتبر',
                    'نوامبر',
                    'دسامبر',
                    ]

jalali_monthnames = ['فروردین',
                     'اردیبهشت',
                     'خرداد',
                     'تیر',
                     'مرداد',
                     'شهریور',
                     'مهر',
                     'آبان',
                     'آذر',
                     'دی',
                     'بهمن',
                     'اسفند'
                     ]

def get_farsi_number(n):
    farsin = ''
    while n > 0:
        farsin = farsi_numbers[n%10] + farsin
        n=int(n/10)
    return farsin

def get_farsi_date(s):
    da = datetime.strptime(s,date_format)
    fyear = get_farsi_number(da.year)
    fmonth = farsi_monthnames[da.month-1]
    fweekday = farsi_weekdays[da.weekday()]
    fday = get_farsi_number(da.day)
    #ftoday = '{} {} {} {}'.format(fweekday, fday, fmonth, fyear)
    ftoday = fweekday
    return ftoday

def get_jalali_date(s):
    da = datetime.strptime(s,date_format)
    j  = jdatetime.date.fromgregorian(day=da.day,month=da.month,year=da.year)
    jyear = get_farsi_number(j.year)
    jmonth = jalali_monthnames[j.month-1]
    jday = get_farsi_number(j.day)
    jtoday = '{} {} {}'.format(jday, jmonth, jyear)
    return jtoday

today = datetime.today().strftime(date_format)

headline = '{} {}'.format(get_farsi_date(today),get_jalali_date(today))
print(headline)
