from tokenizer import PennTreebankTokenizer
t = PennTreebankTokenizer()
s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo o'''
print t.tokenize(s)
