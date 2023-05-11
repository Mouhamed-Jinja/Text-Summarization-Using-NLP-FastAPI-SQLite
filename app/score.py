import nltk
import math
summary = ''''Ad sales boost Time Earner profit Quarterly profits of media giant TimeWarner jumped 76 % $ 1.13bn ( £600m ) three months December,
$ 639m year-earlier.The firm , one biggest investors Google , benefited sales high-speed internet connections higher avert sales. 
However , company said AOL 's underlying profit exceptional items rose 8 % back stronger internet advertising revenues .TimeWarner also
estate 2000 2003 results following probe of Securities Exchange Commission ( SEC ) , close concluding.Time Earner 's fourth quarter profits
slightly better analysis' expectations .TimeWarner said fourth quarter sales rose 2 % $ 11.in $ 10.in .full-year , TimeWarner posted profit $ 3.36bn,
27 % 2003 performance, revenues grew 6.4 % $ 42.09bn .profits buoyed one-off gains offset profit dip Earner Gros , less users AOL.Time Earner
said Friday owns 8 % search-engine Google .intends adjust way accounts deal German music publisher Bertelsmann 's purchase stake AOL Europe,
reported advertising revenue.'''

a_summary = ''''TimeWarner said fourth quarter sales rose 2% to $11.1bn from $10.9bn.For the full-year, TimeWarner posted a profit of $3.36bn,
 up 27% from its 2003 performance, while revenues grew 6.4% to $42.09bn.Quarterly profits at US media giant TimeWarner jumped 76%
 to $1.13bn (£600m) for the three months to December, from $639m year-earlier.However, the company said AOL's underlying profit before
 exceptional items rose 8% on the back of stronger internet advertising revenues.Its profits were buoyed by one-off gains which offset 
a profit dip at Warner Bros, and less users for AOL.For 2005, TimeWarner is projecting operating earnings growth of around 5%, and also 
expects higher revenue and wider profit margins.It lost 464,000 subscribers in the fourth quarter profits were lower than in the preceding
 three quarters.Time Warner's fourth quarter profits were slightly better than analysts' expectations.'''
hypothesis = summary
reference = a_summary
BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
print(f"BLEUscore : %{math.ceil(BLEUscore *100)}")