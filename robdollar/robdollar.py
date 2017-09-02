# -*- coding: utf-8 -*-

"""Main module."""
import pandas as pd
from sklearn.linear_model import LinearRegression, RandomizedLasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import Imputer
import numpy as np
from sklearn.pipeline import Pipeline


def load_df(path, sep='|'):
    df = pd.read_csv(path, header=None, sep=sep)

    return df


def data_check(df):
    data_types = pd.DataFrame(df.dtypes, columns=['dtype'])
    missing_data_counts = pd.DataFrame(df.isnull().sum(), columns=['missing'])
    present_data_counts = pd.DataFrame(df.count(), columns=['count'])
    unique_value_counts = pd.DataFrame(columns=['unique'])
    for v in list(df.columns.values):
        unique_value_counts.loc[v] = [df[v].nunique()]
    minimum_values = pd.DataFrame(columns=['min'])
    for v in list(df.columns.values):
        minimum_values.loc[v] = [df[v].min()]
    maximum_values = pd.DataFrame(columns=['max'])
    for v in list(df.columns.values):
        maximum_values.loc[v] = [df[v].max()]
    quality_report = (data_types.join(present_data_counts).join(missing_data_counts).
                      join(unique_value_counts).join(minimum_values).
                      join(maximum_values))
    return quality_report


def feature_selection(path, target):
    X = load_df(path)
    y = X[target]
    X = X.drop(target, axis=1)

    model = Pipeline([("imputer", Imputer(missing_values='NaN',
                                          strategy="mean",
                                          axis=1)),
                      ('feature', RandomizedLasso()),
                      ("model", LinearRegression())])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=0)
    model.fit(X_train, y_train)
    R2 = model.score(X_test, y_test)
    ypred = model.predict(X_test)
    mse = mean_squared_error(y_test, ypred)
    print "R^2 (Linear Regression + feature selection): ", R2
    print "mse (Linear Regression + feature selection): ", mse

    features = model.named_steps['feature']

    selected_features = X.columns[features.transform(np.arange(len(X.columns)))].values.tolist()[0]

    return selected_features
