import json
import csv
'''
def conv(a):
	a = a.lower()
	translator = str.maketrans('', '', '0123456789')
	a = a.translate(translator)
	return a
'''
def foo(q):
	word = q["entry"]["form"]
	q["contents"][0]["title"]
	i = 0 if q["contents"][0]["title"] == "訳語" else 1
	return word + "\t" + q["contents"][i]["text"].replace('\r', '\\r').replace('\n', '\\n').replace('\t', '\\t')


def main():
	a = open("兮日辞典.json" , "r") 
	b = json.load(a)
	d = [foo(q) for q in b["words"]]
	with open("兮日辞典.tsv", "w") as f:
		for line in d:
			f.write(line + "\n")
	


if __name__ == '__main__':
    main()
