#encoding:utf-8
# Create your views here.
from utils.sequtil import generator_member_code
def get_unique_code(pre):
	random_code = generator_member_code()
	counter = 0
	while counter<5:
		counter = counter + 1

		obj, created = Sequence.objects().get_or_create(seq=pre+random_code)
		if created:
			break

	if not created:
		raise
