import random
from words import words_list
def get_words():
    word=random.choice(words_list)
    return word.upper()
def play(word):
    word_completion='_'*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6
    print('Hey! Let\'s\' see how well you know African countries')
    print('Get Started,show vickie something')
    print(display_hanggirl(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries>0:
        guess=input('come on! guess a letter or word: ').upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter',guess)
            elif guess not in word:
                print(guess,'is not in the word.')
                tries-=1
                guessed_letters.append(guess)
            else:
                print('Great! You impressed Vickie', guess,'is in the word')
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion=''.join(word_as_list)
                if '_' not in word_completion:
                    guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guessed in guessed_words:
                print('You already guessed the word',guess)
            elif guess != word:
                print(guess,'Ops!this is not in word.')
                tries-=1
                guessed_word.append(guess)
            else:
                guessed=True
                word_completion=word
        else:
            print('You dissapointed vickie')
        print(display_hanggirl(tries))
        print(word_completion)
        print('\n')
    if guessed:
        print('Congrats! You impressed vickie. You won!')
    else:
        print('Sorry ,You ran outta tries. The country was'+word+'.Let us get it next time')
         
def display_hanggirl(tries):
    stages=['''

               --------
               |       |
               |       0 
               |      \\|/
               |       |
               |       /\\
               -
             ''',
             '''
                --------
                |       |
                |       0
                |      \\|/
                |       | 
                |       /
                -
             ''',
             '''
                --------
                |       |
                |       0
                |      \\|/  
                |       |
                | 
                -
             ''',
             '''
                --------
                |       |
                |       0
                |      \\|
                |       |
                |
                -
             ''',
             '''
                 --------
                 |       |
                 |       0
                 |       |
                 |       |
                 |
                 -
              ''',
              '''
                 --------
                 |       |
                 |       0
                 |      
                 |
                 |
                 -
              '''        
      ]
    return stages[tries-1]
def main():
    word=get_words()
    play(word)
while input('Play Again?(yes/No) ').upper()=='Yes':
    word=get_word()
    play(word)
if __name__=='__main__':
    main()
