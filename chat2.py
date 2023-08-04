# 對話紀錄改寫2


#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			s = line.strip().split(' ')
			lines.append(s)
		return lines

#資料處理
def convert(lines):
	Allen_word = 0
	Viki_word = 0
	for line in lines:
		name = line[1]
		if name == 'Allen':
			for m in line[2:]:
				Allen_word = Allen_word + len(m)
		elif name == 'Viki':
			for m in line[2:]:
				Viki_word = Viki_word + len(m)
	print('Allen說了', Allen_word, '個字')
	print('Viki說了', Viki_word, '個字')
						











def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)

main()
