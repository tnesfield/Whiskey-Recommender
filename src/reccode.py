from surprise import SVD, Reader, Dataset
import pandas as pd
import numpy as np


def whiskey_rec(w1,w2,w3,w4,w5,user_type,user_budget):
    
    whis_df = pd.read_csv('whiskeys4.csv')

    userid = whis_df['Drinker ID'].max()+1

    user_type = user_type.title()

    rating_list = [{'Drinker ID': userid, 'Bottle': 'Lagavulin 16 Year Old', 'Rating': w1},
                   {'Drinker ID': userid, 'Bottle': 'Glenlivet 18 Year Old', 'Rating': w2},
                   {'Drinker ID': userid, 'Bottle': 'Jamerson 18 Year Old', 'Rating': w3},
                   {'Drinker ID': userid, 'Bottle': 'Hakushu 12 Year Old', 'Rating': w4},
                   {'Drinker ID': userid, 'Bottle': 'Makers Mark Cask Strength', 'Rating': w5}]
    
    new_whis_df = whis_df.append(rating_list,ignore_index=True)
    new_whis_df = new_whis_df[new_whis_df['USD'] <= float(user_budget)]
    new_whis_df = new_whis_df[new_whis_df['Type'] == user_type]
        


        # loaded_model = pickle.load(open(filename, 'rb'))
    
        # #load in new df
        # data = Dataset.load_from_df(new_whis_df[['Drinker ID', 'Bottle ID', 'Rating']], reader)
        

    #create model
    reader = Reader(rating_scale=(1, 100))
    algo = SVD(n_factors = 30, n_epochs = 25)

    #load in new df
    data = Dataset.load_from_df(new_whis_df[['Drinker ID', 'Bottle ID', 'Rating']], reader)

    #fit the model
    algo.fit(data.build_full_trainset())

    # get predictions 
    pred = []
    for w in new_whis_df['Bottle ID'].unique():
        pred.append(algo.predict(new_whis_df['Drinker ID'].max(),w))

    #put predictions into a sorted dataframe    
    df = pd.DataFrame(pred, columns=['Drinker ID', 'Bottle ID', 'rui', 'Rating', 'details'])
    sorteddf = df.sort_values('Rating', ascending = False)
    sorteddf.reset_index(inplace=True)

    result = []
    for i in range(5) : 
        recommendation = []
        bottle = int(sorteddf.loc[i, "Bottle ID"]) 
        bottle_info = new_whis_df.loc[new_whis_df['Bottle ID'] == bottle].iloc[0]
        recommendation.extend((bottle_info['Bottle'],bottle_info['USD'],bottle_info['url']))
        result.append(recommendation)

    results_df = pd.DataFrame(result,columns=['Flight Recommendations','Price USD','URL'])
    results_df.index = np.arange(1, len(results_df) + 1)
    
    return   results_df.to_html(justify='center',render_links=True)  
