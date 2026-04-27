# #task 1
name = input ('შეიყვანეთ თვენი სახელი და გვარი:')
word = name.split()
initials = word [0][0] + '.' + word[1][0] + '.'
result = f"გამარჯობა, თქვენი ინიციალები არის {initials.upper()}"
print (result)


# #task 2
word = input ('გთხოვთ შეიყვანეთ სიტყვა:')
print (word[::-1])

#task 3
sentence = input('დაწერეთ წინადადება:')
ow_1 = input ('პირველი სიტყვა, რომელიც ჩანაცვლდეს:')
nw_1 = input ('სიტყვა, რომლითაც ჩანაცვლდეს პირველი სიტყვა')
ow_2 = input ('მეორე სიტყვა, რომელიც ჩანაცვლდეს:')
nw_2 = input ('სიტყვა, რომლითაც ჩანაცვლდეს მეორე სიტყვა')
new_sentence = sentence.replace(ow_1, nw_1)
new_sentence = new_sentence.replace(ow_2, nw_2)
print (new_sentence)
