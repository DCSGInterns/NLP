def split_line(line):
    cols = line.split('\t')
    return cols

from stat_parser import tokenizer

main_array = []
sub_array = []
with open("C:/Users/kruthika_ved/Documents/GitHub/NLP/Code/slang_word.txt") as stop_file:
    for line in stop_file:
        print line
        if "!@#" in line:
            main_array.append(sub_array)
            sub_array = []
        else:
            parts = split_line(line)
            part = tokenizer.word_tokenizer(parts[1].rstrip('\n'))            
            sub_array.append((parts[0],part))

print main_array

file = open("slag_word.py","w")
file.write(str(main_array))
file.close()

            
