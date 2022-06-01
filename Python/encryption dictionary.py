class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text=text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        word_count=0
        values=[]
        max_count=0
        for i in range(26):
            to_decrypt=(self.apply_shift(i)).split(' ')
            for j in to_decrypt:
                if is_word(self.valid_words,j):
                    word_count+=1
            values.append(word_count)
####################################################################################################3
unencrypted=Message
unencrypted.message_text='Hello Friends'
unencrypted.build_shift_dict(5)
unencrypted.apply_shift(5)
