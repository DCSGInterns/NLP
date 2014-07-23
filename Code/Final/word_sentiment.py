dell_list = ['office', '333d', 'hybrid', 'laptop', 'deployment', '325sli', '433p', '3v', 'manager', 'kits', 'keyboard', 'cx400', '3xxsxcr', '320n-plus', '325nc', 'upgrade', 'monitor', 'tablet', 'tv', 'raid', 'lp982', '316sx', 'latitude', 'xbox', 'hat', 'jukebox', 'dae', 'dj', 'appassure', 'assistant', '320sli', 'kmms', 'dell', 'fc5300', 'touchpad', 'lcd', 'quest', 'dx', 'das', 'dp', 'e-monitor', 'intel', 'kace', 'proc', '3ix', 'venue', 'bay', 'fc4700', '325n', 'usb', 'tuner', 'ups', 'inspiron', 'playstation', 'cisco', 'commvault', 'chromebook', 'fc4700-2', 'e-support', 'bluetooth', 'cx500', 'connect', 'mds', 'vizioncore', 'ax100dp', 'vita', 'vmware', 'powerapp', 'dae4p', 'repository', 'for', 'alienware', 'broadband', 'open', 'precision', 'integration', 'ax100sp', 'ax100i', 'disk', '300', 'ax4-5', 'poweredge', 'ds-32m', 'lasso', 'order', 'red', 'infrastructure', 'chassis', 'sw3800/ds16b2', 'blaster', 'expansion', 'diagnostic', 'management', 'studio', 'web', 'configuration', 'ds-8b', 'powerconnect', 'installation', 'ilc', 'license', 'plug-in', 'adapter', 'rack', 'nl25', 'protection', 'nl20', 'logic', 'router', 'backup', 'e-flat', 'software', '320lx', 'control', 'fc4500', 'point', 'pentium', 'syncup', 'sql', '320lt', 'emulex', 'services', 'projector', 'streak', 'suse', 'mellanox', 'tools', '320sx', 'cloud', 'idrac6', 'smartstep', '316lt', 'networking', 'fabric', 'service', 'smartpc', 'liebert', 'dae2p', 'support', 'broadcom', 'system', 'kvms', 'pc', 'camera', 'xps', '320n', 'openmanager', 'fc64-1063', 'cx4', 'netxtreme', 'hub', 'cx600', 'tool', 'aero', 'platespin', 'ip4700', 'it', 'delivery', 'controller', 'v386', 'catalyst', '5100', '8-16(switch)', 'customer', 'optiplex', 'wyse', 'access', 'cx200', 'windows', 'powervault', 'soundbar', 'server', 'guide', 'pack', 'and', 'mini', 'fc2', 'fc4', 'san', 'flex', 'fc8', 'pro', 'toolkit', 'surface', 'e-legacy', 'cluster', '333s/l', 'nx20', 'vostro', 'prosupport', 'station', 'quality', 'utility', 'nx4', 'e-view', 'recovery', 'media', 'enterprise', 'port', 'simpana', 'sound', 'speaker', 'online', 'performance', 'dellware', 'rt', 'administrator', 'printer', 'replicator', 'users', 'force10', 'toad', 'oemr', 'kvm', 'e-port', 'automation', 'notebook', 'ds-16m', 'catridge', 'drac', 'ethernet', 'eqaullogic', 'brocade', 'ds-16b', 'data', 'lifecycle', 'wireless', 'nx', 'remote', 'cx300', 'database', 'mobile', 'lp7000e', 'update', 'sx', 'microsoft', 'q', 'sonicwall', 'switch', 'client', 'diagnostics', 'oracle', 'mini3', 'sa', 'dimension', 'external']
stopset = set(['all', "she'll", u'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', u'now', "he's", "when's", "we've", 'had', 'should', "he'd", 'to', 'only', "there's", 'those', 'under', 'ours', 'has', 'ought', 'do', 'them', 'his', "they'll", 'very', "who's", "they'd", "you've", 'they', 'not', 'during', 'yourself', 'him', 'nor', "we'll", 'did', "they've", 'this', 'she', 'each', "won't", 'where', "i'll", "why's", 'because', "you'd", 'doing', 'some', 'are', 'further', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', u't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'would', 'of', 'could', 'against', u's', "i'd", "i'm", 'or', 'own', 'into', 'whom', 'down', 'your', "you're", 'from', "how's", 'her', 'their', "it's", 'there', 'been', 'why', 'few', 'too', 'themselves', 'was', 'until', 'more', 'himself', "where's", "i've", 'with', "what's", 'but', u'don', 'herself', 'than', "here's", 'he', 'me', "they're", 'myself', 'these', 'up', u'will', 'below', u'can', 'theirs', 'my', "we'd", 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'that', 'when', 'same', 'how', 'other', 'which', 'you', 'our', 'after', "let's", 'most', 'such', "he'll", 'a', 'off', 'i', "she'd", 'yours', "you'll", 'so', "we're", "she's", 'the', "that's", 'having', 'once'])

from SWNReader import *


import re

regexp_clause = "[.:;!?]"

def get_text_lexicon(current_word,previous_word_inc_val):
    s = get_scores('SentiWordNet.txt',current_word)
    t = previous_word_inc_val
    if t != 0:
        s = t*s
    if current_word.isupper():
        s = s*2   
    return s 



def get_inc_value(word):
    f = open('Incremetors.txt')
    for line in f:
        cols = split_line(line)
        if word == cols[0]:
            #print word
            #Sprint cols[1]
            return float(cols[1])
        else:
            return 0



def negation(chunked):

    regexp_not = "(?:^(?:never|no|nothing|nowhere|noone|none|not|havent|hasnt|hadnt|cant|couldnt|shouldnt|wont|wouldnt|dont|doesnt|didnt|isnt|arent|aint)$)|n't"
    

    neg_sent = []
    prev_word = None
    flag = 1;
    prev_inc_val = 0
    text_count = 0

    for current_word in chunked:
        current_word_small = current_word.lower()

        global stopset
        global dell_list

        if current_word_small not in stopset and current_word_small not in dell_list:   
            t = flag;
            if t==0:
                t = -1 
            t = t * get_text_lexicon(current_word, prev_inc_val)
            if t != 0:
                text_count += 1
        else:
            t = 0
        neg_sent.append((current_word , t))
        if re.search(regexp_not, current_word): 
            flag = (flag + 1) % 2;
        prev_word = current_word
        prev_inc_val = get_inc_value(prev_word)  
    
    #print neg_sent
    return [neg_sent, text_count] 

