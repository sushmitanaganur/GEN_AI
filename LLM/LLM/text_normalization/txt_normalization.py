class TextNormalization:
    def __init__(self,data):
        self.data=data
    def start(self):
        print('''
               1)coverting string to lowercase
               2)Removing punctuations
               3)removing Spl chars
               4)Handling Emojis
               5)Removing Extra Spaces
               6)Contractions(Expanding the words )
               7)correcting the words
             ''')
        
    def strings_lowercase(self):
        self.data=self.data.lower()
        return self.data
    def removing_punctuations(self):
        import string
        chars=self.data
        punctuations=string.punctuation
        for char in punctuations:
            chars=chars.replace(char,'')
        self.data=chars
        return self.data
    def removing_spc_chars(self,data):
        chars=self.data
        for char in chars:
             if  not char .isalnum() or  not ord(char)==32:
              chars=chars.replace(char,'')
        self.data=chars
        return self.data
    def handling_emojis(self):
        import emoji
        self.data = emoji.replace_emoji(self.data, " ")
        return self.data
    def removing_extra_spaces(self):
        import re
        self.data = re.sub(r"\s+"," ",self.data).strip()
        return self.data
    
    def contractions(self):
        self.contractions_dict={
            "can't":"cannot",
            "won't":"will not",
            "i'm":"i am",
            "it's":"it is",
            "don't":"do not",
            "isn't":"is not",
            "you're":"you are",
            "they're":"they are"
        }
        words=self.data.split()
        result=[]

        for word in words:
            result.append(self.contractions_dict.get(word,word))
        self.data=" ".join(result)
        return self.data
    
    def correcting_words(self):
        from textblob import TextBlob

        self.data=str(TextBlob(self.data).correct())
        return self.data
    
obj =TextNormalization(" i'm 😊❤️  the wods for txt!!! normalization")
obj.start()
print("Original data: ",obj.data)
print("Lowercase: ",obj.strings_lowercase())
print("Punctuation removed :",obj.removing_punctuations())
print("spl charats: ",obj.removing_spc_chars())
print("Emojis removed:",obj.handling_emojis())
print("Extra space removed:",obj.removing_extra_spaces())
print("Contractions Expand:",obj.contractions())
print("Corrected Text:",obj.correcting_words())