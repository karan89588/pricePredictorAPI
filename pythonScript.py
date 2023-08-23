from sklearn.ensemble import RandomForestRegressor

import pickle


'''

option.args[0]=state;
option.args[1]=season;
option.args[2]=name;
option.args[3]=availability;
option.args[4]=demand;


predictor data

name
season
state
availability
demand

'''

def predictPrice(name,season,state,availabilty,demand):
    filename='price_predictor_veg.pickle'
    regr=pickle.load(open(filename,'rb'))

    predictorData=[[int(name),int(season),int(state),int(availabilty),int(demand)]]
    data=regr.predict(predictorData)[0]
    return data

if __name__=='__main__':
    print(predictPrice(0,2,0,2,1))
