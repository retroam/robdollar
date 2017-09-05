# -*- coding: utf-8 -*-

"""Main module."""
import pandas as pd
from sklearn.linear_model import LinearRegression, RandomizedLasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import Imputer
import numpy as np
from sklearn.pipeline import Pipeline
import logging

# TODO
# Add MAPE instead of RMSE


# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FeatureSelect(object):
    """
    Base class for feature selection
    """
    def __init__(self, path, target):
        self.path = path
        self.target = target
        self.df = pd.DataFrame()
        self.selected_features = []
        self.quality_report = []
        self.model = ""
        self.R2 = None
        self.mse = None

    def load_csv(self, sep='|'):
        """Function to load csv into python data fromae

        Args:
            path(str): path to csv file.
            sep (str): seperator.

        Returns:
            df: DataFrame of csv file.

        """

        self.df = pd.read_csv(self.path, header=None, sep=sep)

        return self.df

    def data_check(self):
        """Function for creating a data quality report of data.

        Args:
            df (object): DataFrame.

        Returns:
            quality_check: Quality report.

        """
        df = self.df
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
        self.quality_report = (data_types.join(present_data_counts).join(missing_data_counts).
                               join(unique_value_counts).join(minimum_values).
                               join(maximum_values))
        return self.quality_report

    def feature_selection(self):
        """Function for executing feature selection.

        Args:
            path (str): Path to csv file.
            target (str): Name of target column.

        Returns:
            selected_features: The selected features.
        """

        X = self.df
        y = X[self.target]
        X = X.drop(self.target, axis=1)

        self.model = Pipeline([("imputer", Imputer(missing_values='NaN',
                                                   strategy="mean",
                                                   axis=1)),
                               ('feature', RandomizedLasso()),
                               ("model", LinearRegression())])

        try:

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                            random_state=0)
            self.model.fit(X_train, y_train)
            self.R2 = self.model.score(X_test, y_test)
            ypred = self.model.predict(X_test)
            self.mse = mean_squared_error(y_test, ypred)
            logger.info("R^2 (Linear Regression + feature selection): {0}".format(self.R2))
            logger.info("mse (Linear Regression + feature selection): {0}".format(self.mse))

            features = self.model.named_steps['feature']

            self.selected_features = X.columns[features.transform(np.arange(len(X.columns)))].values.tolist()[0]
        except ValueError:
            self.selected_features = []
            logger.error("Issue with data...too small?")

        return self.selected_features
