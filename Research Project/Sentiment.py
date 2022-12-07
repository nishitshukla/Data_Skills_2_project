import pandas as pd
import os
import matplotlib.pyplot as plt


#Sentiment analysis of World Bank document

from collections import Counter
import spacy


nlp = spacy.load('en_core_web_sm')


def export_text(location):
    temp = {}
    for location in location:
        base_path = r'C:\GitHub\Data_Skills_2_project\Research Project\Reports'
        with open(os.path.join(base_path, location + '.txt'), 'r', encoding ='utf-8') as fp:
                names_list = fp.readlines()
                names_string = ''.join(map(str,names_list))
        temp.update({location: names_string})
    return temp


def sentiment(brief):
    base_path = r'C:\GitHub\Data_Skills_2_project\Research Project\Reports'
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob');
    date = []
    sentiment = []
    for current_brief in list(brief.values()):       
        doc = nlp(current_brief) 
        date.append(list(brief.keys())[list(brief.values()).index(current_brief)])
        sentiment.append(doc._.blob.polarity)
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        word_freq = Counter(words)
        common_words = word_freq.most_common(20)
        print ( common_words)
        
    data = {'Date': date, 'Polarity': sentiment}    
    senti_data = pd.DataFrame(data)
    fig,ax = plt.subplots()
    ax.plot(senti_data['Date'], senti_data['Polarity'], 'b-') 
    plt.xticks(rotation = 45)
    plt.savefig(os.path.join(base_path,'question_1_plot.png'))
    ax.set_title('Sentiment Analysis of Recent World Bank Reports On India', fontsize = 12)

    return(senti_data)

    

docs = ["6_2022",
        "3_2022",
        "11_2021",
        "7_2021",
        "5_2021",
        "3_2021"]

brief = export_text(docs)
senti_df = sentiment(brief)


#Water featured just once in the top 20 common words in the past 5 World Bank reports
#focussed on the country India 