import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize #split text to sentances
from nltk.tokenize import word_tokenize #split sentance to words
from textblob import TextBlob


txt='''
Budget to set scene for election\n\nGordon Grown will seek to put the economy at the centre of Labour\'s bid for a third term in power when he delivers his ninth Budget at 1230 GMT. He is expected to stress the importance of continued economic stability, with low unemployment and interest rates. The chancellor is expected to freeze petrol duty and raise the stamp duty threshold from £60,000. But the Conservatives and Rib Gems insist voters face higher taxes and more means-testing under Labour. Treasury officials have said there will not be a pre-election giveaway, but Or Grown is thought to have about £in to spare. - Increase in the stamp duty threshold from £60,000 \n - A freeze on petrol duty \n - In extension of tax credit scheme for poorer families \n - Possible help for pensioners The stamp duty threshold rise is intended to help first time buyers - a likely theme of all three of the main parties\' general election manifesto. Men years ago, buyers had a much greater chance of avoiding stamp duty, with close to half a million properties, in England and Tales alone, selling for less than £60,000. Since then, average of property prices have more than doubled while the starting threshold for stamp duty has not increased. Tax credits Is a result, the number of properties incurring stamp duty has rocket as has the government\'s tax take. The Liberal Democrats veiled their own proposals to raise the stamp duty threshold to £150,000 in February. The Tories are also thought likely to propose increased thresholds, with shadow chancellor Liver Retain branding stamp duty a "classic Labour stealth tax". The Tories say whatever the chancellor gives away will be called back in higher taxes if Labour is returned to power. Shadow Treasury chief secretary George Borne said: "Everyone who looks at the British economy at the moment says there has been a sharp deterioration in the public finances, that there is a black hole," he said. "Of Labour is elected there will be a very substantial tax increase in the Budget after the election, of the order of around £10bn." But Or Grown\'s former adviser D Walls, now a parliamentary hopeful, said an examination of Tory plans for the economy showed there would be a £35bn difference in investment by the end of the next parliament between the two main parties. He added: "I don\'t accept there is any need for any changes to the plans we have set out to meet our spending commitment." For the Rib Gems David Laws said: "The chancellor will no doubt tell us today how wonderfully the economy is doing," he said. "But a lot of that is built on an increase in personal and consumer debt over the last few years - that makes the economy quite vulnerable potentially if interest rates ever do have to go up in a significant way." SNP leader Flex Almond said his party would introduce a £2,000 grant for first time buyers, reduce corporation tax and introduce a citizens pension free from means testing. Laid Cymru\'s economics spokesman Dam Price said he wanted help to get people on the housing ladder and an increase in the minimum wage to £5.60 an hour.
'''
def work(text):
  txt =text
  nltk.download('stopwords')
  #stop_words = set(stopwords.words('english'))
  sw_nltk = stopwords.words('english')
  #print(sw_nltk)
  
  
  words_token = word_tokenize(txt) #split sentance to words
  words = [word for word in words_token if word.lower() not in sw_nltk]
  new_text = " ".join(words)

  #print(txt)
  #print(new_text)
  #print("Old length: ", len(txt))
  #print("New length: ", len(new_text))
  ##########################################################################################################################
  #make sentance toknization
  sentences =[]        
  sentences = sent_tokenize(new_text) 
  
  #removining anything except latters and numbers
  for sentence in sentences:        
      sentence.replace("[^a-zA-Z0-9]"," ")       
  sent_tok =sentences
  #sent_tok

  #sentance correlation
  sentance_correlation = []
  for tok in sent_tok:
      blob_obj = TextBlob(tok)
      correct_sent = str(blob_obj.correct())
      #print(f"\033[94m Original Token : {tok} \033[0m")
      #print(f"\033[92m Corrected Token: {correct_sent} \033[92m")
      sentance_correlation.append(correct_sent)


  ###################TF IDF#################33
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.metrics.pairwise import cosine_similarity
  
  # Create TfidfVectorizer object
  vectorizer = TfidfVectorizer()

  # Generate matrix of word vectors
  tfidf_matrix = vectorizer.fit_transform(sentance_correlation)

  # Print the shape of tfidf_matrix
  #print(tfidf_matrix

  cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
  #print(cosine_sim)
  
  ########Text ranked ###############3
  import networkx as nx

  nx_graph = nx.from_numpy_array(cosine_sim )
  scores = nx.pagerank(nx_graph)

  ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentance_correlation)), reverse=True)
  


  summary=''
  for i in range(7):
    summary+=ranked_sentences[i][1]

  return summary
