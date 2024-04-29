import pandas as pd
import datetime as dt
from datetime import timedelta

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import scipy.stats
from scipy.stats import norm
from scipy.stats import chisquare
from scipy.spatial.distance import pdist, squareform
from sklearn.preprocessing import MinMaxScaler
import datetime as dt
from datetime import timedelta


def detect_outliers(df, n, features):
    '''
    For every feature: 
    - Obtain Q1, Q3 and Interquantile range
    - Define outlier step (as in a boxplot)
    - Detect outliers if observed point is < Q1 - outlier step or point > Q3 + outlier_step
    - Check observations with more than n outliers
    '''
    outlier_indices = []                    
    '''
    Iterate over columns
    '''
    for col in features:
        q_1 = np.percentile(df[col], 25) 
        q_3 = np.percentile(df[col], 75)
        iqr = q_3 - q_1
        '''
        Define outlier step
        '''
        outlier_step = 1.5 * iqr 
        '''
        List of indices of outliers
        '''
        outlier_list_col = df[(df[col]<q_1 - outlier_step) | (df[col]>q_3 + outlier_step)].index
        '''
        Append outlier indices for col to list of outlier indices
        '''
        outlier_indices.extend(outlier_list_col)
    '''
    Select observations with k or more than k outliers
    '''
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(k for k, v in outlier_indices.items() if v >= n)
        
    return multiple_outliers


def metric_characterisation(data, var, confidence):
    '''
    Performs stats calculations to check general behaviour of the metric.
    Inputs:
    data - pandas DataFrame
    var - column in dataframe (pandas Series) containing the metric
    confidence - complement of alpha, the desired confidence (float).
    Outputs:
    - Expectation or baseline, standard deviation and confidence intervals plus what an effect size of 10% would do to the increase/decrease
    - Time series of the metric and distribution plots. 
    '''
    # metric array
    a = 1.0 * np.array(data[var])
    # sample size
    n = len(a)
    # expectation and its standard error
    m, se = np.mean(a), scipy.stats.sem(a)
    # ci
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    # quartile coefficient of dispersion
    q_1 = np.percentile(data[var], 25) 
    q_3 = np.percentile(data[var], 75)
    qcd = (q_3 - q_1)/(q_3 + q_1)
    
    # 10% increase/decrease
    ten_up = np.mean(a) * 1.1
    ten_down = np.mean(a) * 0.9
    # print (TODO: improve output formatting)
    print(f'                                          {var}             ')
    print(f'                           Baseline (average): {np.mean(a)}')
    print(f'                           Standard Deviation: {a.std()}')
    print(f'                           QCD: {qcd}')
    print(f'                           Coefficient of Variation: {a.std()/np.mean(a)}')
    print(f'                           {confidence*100}% CI Lower: {m - h}')
    print(f'                           {confidence*100}% CI Upper: {m + h}')
    print(f'                           10% increase: {ten_up}')
    print(f'                           10% decrease: {ten_down}')
    
    # figures
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4))
    data[var].plot(ax=ax1)
    # TODO: improve number of bars in distribution to be useful to all kinds of metrics
    sns.histplot(data[var], kde=True, ax=ax2)
    ax1.tick_params(axis='x', rotation=45)




def calculate_anomalies(df, alpha):
    # Calculate the anomalies
    anomaly_1 = (df['created_total'] >= 1) & (df['pending_total'] == 0).astype(int)
    anomaly_2 = (df['errors_total'] > df['completed_total']).astype(int)
    anomaly_3 = ((df['completed_total'].diff() < 0) & (df['errors_total'].diff() > 0) &
                 (df['transf_start_total'].diff() > 0)).astype(int)
    anomaly_4 = ((df['completed_total'] == 0) & (df['errors_total'].diff() > 0) &
                 (df['transf_start_total'].diff() > 0)).astype(int)
    anomaly_5 = (df['created_total'] > df['pending_total'].quantile(0.2)) 
    anomaly_6 =  ((df['completed_total'] == 0) & (df['pending_total'] != 0) & (df['errors_total'] >\
                df['pending_total'])).astype(int)

    # Combine the anomalies into a single metric
    df_with_metric = df.copy()
    df_with_metric['health_anom_1'] = (anomaly_1*2) + (anomaly_2*3) + anomaly_3 + (anomaly_4*3) + anomaly_5 + anomaly_6
    
    scaler = MinMaxScaler()
    df_with_metric['health_anom_1_normed'] = scaler.fit_transform(df_with_metric['health_anom_1'].values.reshape(-1, 1))
    
    # Smooth the metric using an exponential moving average with alpha=0.5
    df_with_metric['health_anom_exp_1'] = df_with_metric['health_anom_1'].ewm(alpha=alpha).mean()
    
    df_with_metric['health_anom_normed_exp_1'] = df_with_metric['health_anom_1_normed'].ewm(alpha=alpha).mean()
    
    return df_with_metric


def calculate_flow(df, alpha):
    # Calculate the anomalies
    a1 = (df['completed_total'] >= 1) & (df['completed_total'] <= 6).astype(int)
    a2 = (df['completed_total'] >= 7) & (df['completed_total'] <= 12).astype(int)

    # Combine the anomalies and weights into a single metric
    df_with_metric = df.copy()
    df_with_metric['health_anom_2'] = (a1) + (a2)
    
    scaler = MinMaxScaler()
    df_with_metric['health_anom_2_normed'] = scaler.fit_transform(df_with_metric['health_anom_2'].values.reshape(-1, 1))
    
    # Smooth the metric using an exponential moving average with alpha=0.5
    # low alpha means slower decay (older observations have more influence)
    # high alpha means faster decay (newer observations have more influence)
    df_with_metric['health_anom_exp_2'] = df_with_metric['health_anom_2'].ewm(alpha=alpha).mean()
    
    df_with_metric['health_anom_normed_exp_2'] = df_with_metric['health_anom_2_normed'].ewm(alpha=alpha).mean()
    
    return df_with_metric


def linear_combination(df, metric1, metric2, w1, w2):
    # Combine the two normalized metrics using a linear combination
    df['combined_metric'] = w1 * df[metric1] + w2 * df[metric2]
    df['norm_combined_metric'] = (df['combined_metric'] - df['combined_metric'].min()) / (df['combined_metric'].max() - df['combined_metric'].min())
    return df