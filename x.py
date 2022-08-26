
# start = "{({["
# end = "]})}"

# start_count = 0
# end_count = 0

# for i in a:
# 	if i in start:
# 		start_count = start_count + 1

# 	elif i in end:
# 		end_count = end_count + 1



org = "{[]({[<]})}>"

dic = {
	"{": "}",
	"[": "]",
	"(": ")",
	"<": ">"
}

dummy = org

for i, x in enumerate(org):
	if x in dic.keys():
		dummy = dummy.replace(x, '', 1)
		v = dic[x]
		
		if v in dummy:
			dummy = dummy.replace(v, '', 1)

		print(dummy)

	elif x in dic.values():
		dummy = dummy.replace(x, '', 1)
		# print("String imbalanced")
		# exit()
		print(dummy)


print(dummy)

# if len(dummy):
# 	print("String imbalanced")
# else:
# 	print("String balanced")