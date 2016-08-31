import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge


import pylab as pl
from  sklearn.cross_validation import KFold

predictors = ['age','sex','test_time','Jitter(Abs)','Jitter:RAP','Jitter:PPQ5','Jitter:DDP','Shimmer','Shimmer(dB)','Shimmer:APQ3','Shimmer:APQ5','Shimmer:APQ11','Shimmer:DDA','NHR','HNR','RPDE','DFA','PPE']
#target1 = ['motor_UPDRS']
targer1 = ['total_UPDRS']

def read_csv(filename):
    df = pd.read_csv(filename,sep = ',')
    return df



def process_svr(df):

    bestsc = -100
    bestpara = 1
    for c in pl.frange(0.5,1.5,0.1):
        clf = svm.SVR(C =c )
        scores = cross_validation.cross_val_score(clf,df[predictors],df[target1].values.ravel(),cv = 5)
        score = np.mean(scores)
        if (bestsc < score):
            bestsc = score
            bestpara = c
    return bestpara

def process_lienar(df):

    lin = LinearRegression()
    lin.fit(df[predictors],df[target1].values.ravel())

def training_predict_lin(df):

    results =[]
    #独立重复10次
    for train,test in KFold(len(df),n_folds = 10,shuffle = True):
        clf = LinearRegression()
        clf.fit(df[predictors].T[train].T,df[target1].T[train].values.ravel())

        sc = clf.score(df[predictors].T[test].T,df[target1].T[test].values.ravel())
        results.append(sc)
    return results

def training_predict_svr(df):

    results =[]
    #独立重复10次
    for train,test in KFold(len(df),n_folds = 10,shuffle = True):
        para = process_svr(df.T[train].T)
        clf = svm.SVR(C = para)
        clf.fit(df[predictors].T[train].T,df[target1].T[train].values.ravel())
        sc = clf.score(df[predictors].T[test].T,df[target1].T[test].values.ravel())
        results.append(sc)
    return results

def process_ridge(df):

    bestpara = 0
    bestsc = -1000
    for alp in pl.frange(0.5,1.5,0.1):
        clf = Ridge(alpha = alp)
        scores = cross_validation.cross_val_score(clf,df[predictors],df[target1].values.ravel(),cv = 5)
        score = np.mean(scores)
        if (bestsc < score):
            bestsc = score
            bestpara = alp
            
    return bestpara

def training_predict_ridge(df):

    results =[]
    #独立重复10次
    for train,test in KFold(len(df),n_folds = 10,shuffle = True):
        para = process_ridge(df.T[train].T)
        clf = Ridge(alpha = para)
        clf.fit(df[predictors].T[train].T,df[target1].T[train].values.ravel())

        sc = clf.score(df[predictors].T[test].T,df[target1].T[test].values.ravel())
        results.append(sc)
    return results



if __name__=='__main__':


    df = read_csv('parkinsons_updrs.data')




    print('svr:')

    ret = training_predict_svr(df)
    print(ret)
    print(np.mean(ret))

    print('\n linear_model')
    ret_linear = training_predict_lin(df)
    print(ret_linear)
    print(np.mean(ret_linear))

    print('\n ridge regression')
    ret_ridge = training_predict_ridge(df)
    print(ret_ridge)
    print(np.mean(ret_ridge))

    #x_train,x_test,y_train,y_test = cross_validation.train_test_split(data,tar1,test_size = 0.4,random_state=0)
