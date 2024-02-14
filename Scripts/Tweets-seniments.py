
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("Scripts\\Externals\\Positive_wordss.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("Scripts\\Externals\\Negative_wordss.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(str):
    for i in str:
        if i in punctuation_chars:
            str = str.replace(i,"")
    return str    

def get_pos(sent): #sent
    sent = strip_punctuation(sent)
    counter = 0
    sent = sent.split()
    for word in sent:
        if word.lower() in positive_words:
            counter += 1
    return counter

def get_neg(sent): #sent
    sent = strip_punctuation(sent)
    sent = sent.split()
    counter = 0
    for word in sent:
        if word.lower() in negative_words:
            counter += 1
    return counter          

# Python Project 
fname = open("Scripts\Externals\project_twitter_data.txt", "r")
allTweets = fname.readlines()
allTweets = allTweets[1:]
res_data = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n"


for lin in allTweets: #line per a tweet ["tweet, retweet, replies"]
    lin = lin.replace("\n", "")
    lin = lin.split(",") #['tweet_text', 'retweet_count', 'reply_count\n']
    res_data += lin[1] + ", " + lin[2] +", "+ str(get_pos(lin[0])) +", "+ str(get_neg(lin[0])) +", "+ str(get_pos(lin[0]) - get_neg(lin[0])) +"\n"

lastFile = open("resulting_data.csv","w")
lastFile.write(res_data)
lastFile.close()    