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
	Allen_sticker = 0
	Viki_sticker = 0
	Allen_image = 0
	Viki_image = 0
	for line in lines:
		name = line[1]
		if name == 'Allen':
			if line[2] == '貼圖':
				Allen_sticker = Allen_sticker + 1
			elif line[2] == '圖片':
				Allen_image = Allen_image + 1
			else:
				for m in line[2:]:
					Allen_word = Allen_word + len(m)
		elif name == 'Viki':
			if line[2] == '貼圖':
				Viki_sticker = Viki_sticker + 1
			elif line[2] == '圖片':
				Viki_image = Viki_image + 1
			else:
				for m in line[2:]:
					Viki_word = Viki_word + len(m)
	print('Allen說了', Allen_word, '個字')
	print('Allen傳了', Allen_sticker, '個貼圖')
	print('Allen傳了', Allen_image, '個圖片')
	print('Viki說了', Viki_word, '個字')
	print('Viki傳了', Viki_sticker, '個貼圖')
	print('Viki傳了', Viki_image, '個圖片')
						
def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)

main()
