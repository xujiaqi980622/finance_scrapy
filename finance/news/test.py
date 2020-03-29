import re

# str="央视网 | 2020年03月29日 10:06"
# pat='(.*?[^|])'
# # m = re.match(pat,str)
# # print(m.group())
# print(str.split("|")[0])
# string ="新京报 记者：张秀兰 编辑：岳清秀"
# print(re.split(r'\s',string)[0])


str = "时间：2020年02月25日 08:55:49 中财网"
# reg='(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2})'
# reg2 = str.replace("年", "-").replace("月", "-").replace("日", " ").replace("/", "-").strip()
# t = re.sub("\s+", " ", str)
# print(t)
regex_str=".*(\d{4}[年/-]\d{1,2}([月/-]|[月/-]$|$)\d{1,2}([日/-]|[日/-]$|$) \d{1,2}:\d{1,2}:\d{1,2})"
match_obj = re.match(regex_str,str)
if match_obj:
    print(match_obj.group(1))
source = re.findall('.([^ ])$',str)[0]
print(source)
