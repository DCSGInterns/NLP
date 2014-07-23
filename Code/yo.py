st = ['300', '316lt', '316sx', '320lt', '320lx', '320n', '320n-plus', '320sli', '320sx', '325n', '325nc', '325sli', '333d', '333s/l', '3ix', '3v', '3xxsxcr', '433p', '5100', '8-16(switch)', 'a', 'about', 'above', 'access', 'adapter', 'administrator', 'aero', 'after', 'again', 'against', 'alienware', 'all', 'am', 'an', 'and', 'and', 'any', 'appassure', 'are', 'as', 'assistant', 'at', 'automation', 'ax100dp', 'ax100i', 'ax100sp', 'ax4-5', 'backup', 'bay', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'blaster', 'bluetooth', 'both', 'broadband', 'broadcom', 'brocade', 'but', 'by', 'camera', u'can', 'catalyst', 'catridge', 'chassis', 'chromebook', 'cisco', 'client', 'cloud', 'cluster', 'commvault', 'configuration', 'connect', 'control', 'controller', 'could', 'customer', 'cx200', 'cx300', 'cx4', 'cx400', 'cx500', 'cx600', 'dae', 'dae2p', 'dae4p', 'das', 'data', 'database', 'delivery', 'dell', 'dellware', 'deployment', 'diagnostic', 'diagnostics', 'did', 'dimension', 'disk', 'dj', 'do', 'does', 'doing', u'don', 'down', 'dp', 'drac', 'ds-16b', 'ds-16m', 'ds-32m', 'ds-8b', 'during', 'dx', 'e-flat', 'e-legacy', 'e-monitor', 'e-port', 'e-support', 'e-view', 'each', 'emulex', 'enterprise', 'eqaullogic', 'ethernet', 'expansion', 'external', 'fabric', 'fc2', 'fc4', 'fc4500', 'fc4700', 'fc4700-2', 'fc5300', 'fc64-1063', 'fc8', 'few', 'flex', 'for', 'for', 'force10', 'from', 'further', 'guide', 'had', 'has', 'hat', 'have', 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'hub', 'hybrid', 'i', "i'd", "i'll", "i'm", "i've", 'idrac6', 'if', 'ilc', 'in', 'infrastructure', 'inspiron', 'installation', 'integration', 'intel', 'into', 'ip4700', 'is', 'it', 'it', "it's", 'its', 'itself', 'jukebox', u'just', 'kace', 'keyboard', 'kits', 'kmms', 'kvm', 'kvms', 'laptop', 'lasso', 'latitude', 'lcd', "let's", 'license', 'liebert', 'lifecycle', 'logic', 'lp7000e', 'lp982', 'management', 'manager', 'mds', 'me', 'media', 'mellanox', 'microsoft', 'mini', 'mini3', 'mobile', 'monitor', 'more', 'most', 'my', 'myself', 'networking', 'netxtreme', 'nl20', 'nl25', 'no', 'nor', 'not', 'notebook', u'now', 'nx', 'nx20', 'nx4', 'oemr', 'of', 'off', 'office', 'on', 'once', 'online', 'only', 'open', 'openmanager', 'optiplex', 'or', 'oracle', 'order', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'pack', 'pc', 'pentium', 'performance', 'platespin', 'playstation', 'plug-in', 'point', 'port', 'powerapp', 'powerconnect', 'poweredge', 'powervault', 'precision', 'printer', 'pro', 'proc', 'projector', 'prosupport', 'protection', 'q', 'quality', 'quest', 'rack', 'raid', 'recovery', 'red', 'remote', 'replicator', 'repository', 'router', 'rt', u's', 'sa', 'same', 'san', 'server', 'service', 'services', 'she', "she'd", "she'll", "she's", 'should', 'simpana', 'smartpc', 'smartstep', 'so', 'software', 'some', 'sonicwall', 'sound', 'soundbar', 'speaker', 'sql', 'station', 'streak', 'studio', 'such', 'support', 'surface', 'suse', 'sw3800/ds16b2', 'switch', 'sx', 'syncup', 'system', u't', 'tablet', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'toad', 'too', 'tool', 'toolkit', 'tools', 'touchpad', 'tuner', 'tv', 'under', 'until', 'up', 'update', 'upgrade', 'ups', 'usb', 'users', 'utility', 'v386', 'venue', 'very', 'vita', 'vizioncore', 'vmware', 'vostro', 'was', 'we', "we'd", "we'll", "we're", "we've", 'web', 'were', 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", u'will', 'windows', 'wireless', 'with', "won't", 'would', 'wyse', 'xbox', 'xps', 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
st.sort()

ts = st

import string

def b(tag):
	global ts 

	sub = []
	ts.sort()

	for word in ts:
		
		if word[0] == tag:
			break
		else:
			sub.append(word)
			ts = [x for x in ts if x != word]

	#print sub
	return sub

def a():
	main = []
	li = list(string.ascii_lowercase)
	for alpha in li:
		main.append(b(alpha))
	return main

print a()


