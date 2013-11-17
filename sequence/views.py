#encoding:utf-8
# Create your views here.
from sequence.models import SEQAdmin, SEQSys, SEQMerchant, SEQEmploy
def get_unique_code(pre):
    '''
    @todo :add redis to sync
    '''
    if pre == 'A':
    	c = SEQAdmin 
    elif pre == 'S':
    	c = SEQSys
    elif pre == 'M':
    	c = SEQMerchant
    elif pre == 'E':
    	c = SEQEmploy
    else:
    	raise

    seq_obj = c.objects.create() 
    seq_id = seq_obj.id

    digest = ('%s'% seq_id).zfill(5)

    seq_obj.digest = digest
    seq_str = '%s%s'%(pre, digest)
    seq_obj.seq = seq_str
    seq_obj.save()

    return seq_str





