#encoding:utf-8

import datetime
import random
s10 = [str(i) for i in range(0, 10)]
az = [chr(i) for i in range(97, 123)]
AZ = [chr(i) for i in range(65, 91)]
random_choice_list = az + AZ + s10

def _generator_s_date(x):
    '''
    x is len of str_date
    x is in [0:20]
    '''
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, '%Y%m%d%H%M%S')[:x]

def _generator_s_random(random_choice_list, x):
    '''
    x is len of str_random
    x is in [0:len(random_choice_list)]
    '''
    r_l = random.sample(random_choice_list, x)
    return ''.join(r_l)
    
def generator_member_code():
    alpher = _generator_s_random(AZ, 2)
    digest = _generator_s_random(s10, 4)

    return alpher+digest