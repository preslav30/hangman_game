import random
hangman_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['a', 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'act', 'action',
             'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again',
             'against', 'age', 'agency', 'agent', 'ago', 'agree', 'agreement', 'ahead', 'air', 'all', 'allow', 'almost',
             'alone', 'along', 'already', 'also', 'although', 'always', 'American', 'among', 'amount', 'analysis',
             'and', 'animal', 'another', 'answer', 'any', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area',
             'argue', 'arm', 'around', 'arrive', 'art', 'article', 'artist', 'as', 'ask', 'assume', 'at', 'attack',
             'attention', 'attorney', 'audience', 'author', 'authority', 'available', 'avoid', 'away', 'baby', 'back',
             'bad', 'bag', 'ball', 'bank', 'bar', 'base', 'be', 'beat', 'beautiful', 'because', 'become', 'bed',
             'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond',
             'big', 'bill', 'billion', 'bit', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'box',
             'boy', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'but', 'buy', 'by', 'call',
             'camera', 'campaign', 'can', 'cancer', 'candidate', 'capital', 'car', 'card', 'care', 'career', 'carry',
             'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair',
             'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church',
             'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection',
             'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer',
             'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer', 'contain', 'continue', 'control',
             'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture',
             'cup', 'current', 'customer', 'cut', 'dark', 'data', 'daughter', 'day', 'dead', 'deal', 'death', 'debate',
             'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat', 'democratic', 'describe',
             'design', 'despite', 'detail', 'determine', 'develop', 'development', 'die', 'difference', 'different',
             'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'do',
             'doctor', 'dog', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each', 'early',
             'east', 'easy', 'eat', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either',
             'election', 'else', 'employee', 'end', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment',
             'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody',
             'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience',
             'expert', 'explain', 'eye', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'far', 'fast', 'father',
             'fear', 'federal', 'feel', 'feeling', 'few', 'field', 'fight', 'figure', 'fill', 'film', 'final',
             'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five',
             'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former',
             'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'gas',
             'general', 'generation', 'get', 'girl', 'give', 'glass', 'go', 'goal', 'good', 'government', 'great',
             'green', 'ground', 'group', 'grow', 'growth', 'guess', 'gun', 'guy', 'hair', 'half', 'hand', 'hang',
             'happen', 'happy', 'hard', 'have', 'he', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'her',
             'here', 'herself', 'high', 'him', 'himself', 'his', 'history', 'hit', 'hold', 'home', 'hope', 'hospital',
             'hot', 'hotel', 'hour', 'house', 'how', 'however', 'huge', 'human', 'hundred', 'husband', 'I', 'idea',
             'identify', 'if', 'image', 'imagine', 'impact', 'important', 'improve', 'in', 'include', 'including',
             'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead',
             'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve',
             'issue', 'it', 'item', 'its', 'itself', 'job', 'join', 'just', 'keep', 'key', 'kid', 'kill', 'kind',
             'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'law',
             'lawyer', 'lay', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'leg', 'legal', 'less', 'let',
             'letter', 'level', 'lie', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live',
             'local', 'long', 'look', 'lose', 'loss', 'lot', 'love', 'low', 'machine', 'magazine', 'main', 'maintain',
             'major', 'majority', 'make', 'man', 'manage', 'management', 'manager', 'many', 'market', 'marriage',
             'material', 'matter', 'may', 'maybe', 'me', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting',
             'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind',
             'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most',
             'mother', 'mouth', 'move', 'movement', 'movie', 'Mr', 'Mrs', 'much', 'music', 'must', 'my', 'myself',
             'name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network',
             'never', 'new', 'news', 'newspaper', 'next', 'nice', 'night', 'no', 'none', 'nor', 'north', 'not', 'note',
             'nothing', 'notice', 'now', "n't", 'number', 'occur', 'of', 'off', 'offer', 'office', 'officer',
             'official', 'often', 'oh', 'oil', 'ok', 'old', 'on', 'once', 'one', 'only', 'onto', 'open', 'operation',
             'opportunity', 'option', 'or', 'order', 'organization', 'other', 'others', 'our', 'out', 'outside', 'over',
             'own', 'owner', 'page', 'pain', 'painting', 'paper', 'parent', 'part', 'participant', 'particular',
             'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'pay', 'peace', 'people', 'per',
             'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick',
             'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'PM', 'point', 'police', 'policy',
             'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power',
             'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private',
             'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor',
             'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push',
             'put', 'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather',
             'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent',
             'recently', 'recognize', 'record', 'red', 'reduce', 'reflect', 'region', 'relate', 'relationship',
             'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research',
             'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right',
             'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'run', 'safe', 'same', 'save', 'say', 'scene',
             'school', 'science', 'scientist', 'score', 'sea', 'season', 'seat', 'second', 'section', 'security', 'see',
             'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'set', 'seven',
             'several', 'sex', 'sexual', 'shake', 'share', 'she', 'shoot', 'short', 'shot', 'should', 'shoulder',
             'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister',
             'sit', 'site', 'situation', 'six', 'size', 'skill', 'skin', 'small', 'smile', 'so', 'social', 'society',
             'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'son', 'song', 'soon', 'sort', 'sound',
             'source', 'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport',
             'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay',
             'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student',
             'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest',
             'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'task', 'tax', 'teach',
             'teacher', 'team', 'technology', 'television', 'tell', 'ten', 'tend', 'term', 'test', 'than', 'thank',
             'that', 'the', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think',
             'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout',
             'throw', 'thus', 'time', 'to', 'today', 'together', 'tonight', 'too', 'top', 'total', 'tough', 'toward',
             'town', 'trade', 'traditional', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip',
             'trouble', 'true', 'truth', 'try', 'turn', 'TV', 'two', 'type', 'under', 'understand', 'unit', 'until',
             'up', 'upon', 'us', 'use', 'usually', 'value', 'various', 'very', 'victim', 'view', 'violence', 'visit',
             'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'war', 'watch', 'water', 'way', 'we', 'weapon', 'wear',
             'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where', 'whether', 'which',
             'while', 'white', 'who', 'whole', 'whom', 'whose', 'why', 'wide', 'wife', 'will', 'win', 'wind', 'window',
             'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world', 'worry',
             'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'yes', 'yet', 'you', 'young', 'your',
             'yourself']

choice = input("\nType 1 for Easy, 2 for Medium, 3 for Hard or 4 for Expert. Type 5 to stop the game.\n")
if choice == "5":
    print("GOOD GAME BRO!")
    quit()
easy_list = []
medium_list = []
hard_list = []
expert_list = []

for word in word_list:
    if 3 <= len(word) <= 4:
        easy_list.append(word)
    elif len(word) == 5:
        medium_list.append(word)
    elif len(word) == 6:
        hard_list.append(word)
    elif len(word) > 6:
        expert_list.append(word)

while choice != "5":
    if choice == "5":
        print("GOOD GAME BRO!")
        break
    elif choice == "1":
        random_word_chosen_by_computer = random.choice(easy_list)
    elif choice == "2":
        random_word_chosen_by_computer = random.choice(medium_list)
    elif choice == "3":
        random_word_chosen_by_computer = random.choice(hard_list)
    elif choice == "4":
        random_word_chosen_by_computer = random.choice(expert_list)
    else:
        print("Invalid input!")
    random_computer_chosen_word_list = list(random_word_chosen_by_computer) # turn word into list so we can iterate over it and replace characters at certain indices
    incomplete_word = list(random_word_chosen_by_computer[0] + "_" * (len(random_word_chosen_by_computer) - 2) + random_word_chosen_by_computer[-1])
    print("Your word is: " + random_word_chosen_by_computer[0] + "_" * (len(random_word_chosen_by_computer) - 2) + random_word_chosen_by_computer[-1])
    print(hangman_stages[-1])
    successful_guesses = 0
    wrong_guesses = 6
    current_hangman_stage = -1      # we need this in order to know which hangman stage to print
    guess = input("You have 6 guesses. Guess a letter or type 5 to stop the game: ")  # works until here
    if guess == "5":
        print("\nBYE!")
        break
    guessed_letters_list = []
    while successful_guesses < len(random_word_chosen_by_computer) - 2:
        if guess not in guessed_letters_list:
            if guess in random_computer_chosen_word_list:
                if random_computer_chosen_word_list.count(guess) == 1 and (guess == random_computer_chosen_word_list[0] or guess == random_computer_chosen_word_list[-1]):
                    print("This is either the first or the last letter. Does not occur a second time.")
                elif random_computer_chosen_word_list.count(guess) > 1 and (guess == random_computer_chosen_word_list[0] or guess == random_computer_chosen_word_list[-1]):
                    for i in range(1, len(random_computer_chosen_word_list) - 1):
                        if random_computer_chosen_word_list[i] == guess:
                            incomplete_word[i] = guess
                            successful_guesses += 1
                            guessed_letters_list.append(guess)
                            if successful_guesses == len(random_word_chosen_by_computer) - 2:
                                print("".join(incomplete_word))
                                print("\nYOU WIN!")
                                break
                            else:
                                print("\nYou found one! Here's what's left of the word:")
                                print("".join(incomplete_word))
                                print("\n\nGuesses made so far: " + " ".join(guessed_letters_list))
                else:
                    for x in range(1, len(random_computer_chosen_word_list) - 1):
                        if random_computer_chosen_word_list[x] == guess:
                            incomplete_word[x] = guess
                            successful_guesses += 1
                            guessed_letters_list.append(guess)
                            if successful_guesses == len(random_word_chosen_by_computer) - 2:
                                print("".join(incomplete_word))
                                print("\nYOU WIN!")
                                break
                            else:
                                print("\n\nYou found one! Here's what's left of the word:")
                                print("".join(incomplete_word))
                                print("\n\nGuesses made so far: " + " ".join(guessed_letters_list))
            elif guess not in random_computer_chosen_word_list:
                wrong_guesses -= 1
                guessed_letters_list.append(guess)
                if wrong_guesses == 0:
                    print(hangman_stages[0])
                    print("\nYOU LOSE.")
                    print("The word is: " + random_word_chosen_by_computer)
                    break
                else:
                    current_hangman_stage -= 1
                    print(f"\nWrong guess. {wrong_guesses} wrong guesses left.")
                    print(hangman_stages[current_hangman_stage])
                    print("\n\nGuesses made so far: " + " ".join(guessed_letters_list))
                    print("".join(incomplete_word))
        elif guess in guessed_letters_list:
            print("\nYou've already guessed that letter!")

        if successful_guesses == len(random_word_chosen_by_computer) - 2:
            break
        guess = input("\nGuess another letter or type 5 to stop the game. ")
        if guess == "5":
            break
    if guess == "5":
        print("\nBYE!")
        break
    choice = input("\nType 1 for Easy, 2 for Medium, 3 for Hard or 4 for Expert. Type 5 to stop the game.\n")
    if choice == "5":
        print("BYE!")
        quit()







