
###以下を変更###
# file_name = ''
# file_name = 'mecab_bonbonshokora'
# file_name = 'Juman_bonbonshokora'
file_name = 'Janome_bonbonshokora'
ma_type = 2
# text = ''

#ファイル読み込み
file_path = 'bonbonshokora.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

#===ma_type===
# 0 : Mecab
# 1 : Juman
# 2 : Janome

# 3 : Juman_customed
#import等
import time
import MeCab

from pyknp import Juman
jumanpp = Juman(command='/usr/local/bin/jumanpp', option='--dir /usr/local/share/jumanpp')
from janome.tokenizer import Tokenizer

###処理部分###
if ma_type == 0: 
    #MeCab
    mecabrc_path = "/etc/mecabrc"
    tagger = MeCab.Tagger(f"-r {mecabrc_path}")
    start = time.time()
    parsed = tagger.parse(text)
    end = time.time()
elif ma_type == 1: 
    #Juman
    start = time.time()
    result = jumanpp.analysis(text)
    end = time.time()
    parsed = []
    for mrph in result.mrph_list():
        parsed.append("{:<10}原形:{:<10} 品詞:{:<10} 品詞細分類:{:<15} 活用型:{:<10} 活用形:{:<10} 意味情報:{:<20} 代表表記:{}".format(
            mrph.midasi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
    parsed = "\n".join(parsed)
elif ma_type == 2: 
    #Janome
    t = Tokenizer()
    start = time.time()
    result = t.tokenize(text)
    end = time.time()
    parsed = []
    for token in result:
        parsed.append(str(token))
    parsed = "\n".join(parsed)
elif ma_type == 3:
    start_1 = time.time()
    result = jumanpp.analysis(text_1)
    end_1 = time.time()
    parsed_1 = []
    for mrph in result.mrph_list():
        parsed_1.append("{:<10}原形:{:<10} 品詞:{:<10} 品詞細分類:{:<15} 活用型:{:<10} 活用形:{:<10} 意味情報:{:<20} 代表表記:{}".format(
            mrph.midasi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
    parsed_1 = "\n".join(parsed_1)
    
    start_2 = time.time()
    result = jumanpp.analysis(text_2)
    end_2 = time.time()
    parsed_2 = []
    for mrph in result.mrph_list():
        parsed_2.append("{:<10}原形:{:<10} 品詞:{:<10} 品詞細分類:{:<15} 活用型:{:<10} 活用形:{:<10} 意味情報:{:<20} 代表表記:{}".format(
            mrph.midasi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))
    parsed_2 = "\n".join(parsed_2)

elapsed_time = end - start
# elapsed_time = end_2 - start_2 + end_1 - start_1

with open(file_name + '.txt', 'w', encoding='utf-8') as file:
    file.write("#Tool__name: ")
    if ma_type == 0:
        file.write("MeCab")
    elif ma_type == 1 or ma_type == 3:
        file.write("Juman")
    elif ma_type == 2:
        file.write("Janome")
    file.write('\n')
    #file.write("#Checked_text: " + text + '\n')
    file.write("Checked_text: bonbonshokora.txt" + '\n')
    file.write("#execute_time: " + str(elapsed_time) + ' [sec]' + '\n\n')
    if ma_type == 3:
        file.write(parsed_1)
        file.write(parsed_2)
    else:
        file.write(parsed)

# 結果を表示
#print(parsed)
