persian_to_english = {
    'ا': 'a',
    'آ': 'a',
    'ب': 'b',
    'پ': 'p',
    'ت': 't',
    'ث': 's',
    'ج': 'j',
    'چ': 'ch',
    'ح': 'h',
    'خ': 'kh',
    'د': 'd',
    'ذ': 'z',
    'ر': 'r',
    'ز': 'z',
    'ژ': 'zh',
    'س': 's',
    'ش': 'sh',
    'ص': 's',
    'ض': 'd',
    'ط': 't',
    'ظ': 'z',
    'ع': 'a',
    'غ': 'gh',
    'ف': 'f',
    'ق': 'q',
    'ک': 'k',
    'گ': 'g',
    'ل': 'l',
    'م': 'm',
    'ن': 'n',
    'و': 'v',
    'ه': 'h',
    'ي': 'y',
}

while True :
    Text=input("\nEnter a Persian letter (1 for leave) : ")

    if Text == "1" : 
        break
    
    ENtext=persian_to_english.get(Text)
    
    if ENtext == None:
        print("\nLetter not found in the dictionary")
        
    else:
        print(f"\n*** The English letter of {Text} is {ENtext} ***")








 
