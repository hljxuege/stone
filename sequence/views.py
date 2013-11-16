#encoding:utf-8
# Create your views here.

def alpha_add1(alpha):
	'''
	A~Z :65~91
	'''

	len_alpha = len(alpha)
	if len_alpha == 1:
		h, l = 64, ord(alpha)
	else:
		h, l = ord(alpha[0]), ord(alpha[1])

	l = l + 1
	if l > 91:
		l = 65
	    h = h + 1

	if h < 65:
		alpha_1 = chr(l)
	else:
		alpha_1 = chr(h)+chr(l)

	return alpha_1 	

def digest_add1(digest):

	return ('%s'%(int(digest)+1)).zfill(4)

def get_unique_code(pre):
	last_pre = Sequence.objects().get(pre=pre)
	seq = pre + alpha + digest
	len_seq = len(seq)
	r = 7 - len_seq
	if r > 0:
		seq = seq + '0'*r

	obj, created = Sequence.objects().get_or_create(alpha=alpha, digest=digest, seq=seq)
		

	if not created:
		raise
