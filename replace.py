'''
5. Aditi has used a text editing software to type some text. After saving
the article as WORDS.TXT, she realised that she has wrongly typed alphabet
J in place of alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the
corrected version of entire content of the file WORDS.TXT with all the
alphabets "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.
Example:
If Aditi has stored the following content in the file WORDS.TXT:
WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE
The function JTOI() should display the following content:
WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH THIS TO BE A SENTENCE'''

line = ''
file = open('word.txt','r')
data = file.readlines()
for i in data:
	# strip = i.strip()
	# print(strip)
	s = i.replace("J","I")
	# line+= s+ '\n'
	print(s)		


