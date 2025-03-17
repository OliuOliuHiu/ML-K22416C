import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.under_sampling import RandomUnderSampler, AllKNN
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from catboost import CatBoostClassifier
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from imblearn.combine import SMOTETomek

from Model.Statistic import Statistic


class MLModel(Statistic):
    def __init__(self,connector=None):
        super().__init__(connector)
        self.le = LabelEncoder()
    def preProcess(self):
        self.df.drop(columns = ['Column1','ID','FLAG_MOBIL'],inplace=True)
        # Labeling categorical variables
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                self.df[col] = self.le.fit_transform(self.df[col])
        return self.df

    def processResampling(self,technique,random_state):
        if technique == 'Random Undersampling':
            resampler = RandomUnderSampler(random_state=random_state)
        elif technique == 'All K-Nearest Neighbors':
            resampler = AllKNN()
        elif technique == 'Synthetic Minority Oversampling Technique (SMOTE)':
            resampler = SMOTE(random_state=random_state)
        elif technique == 'SMOTE combines Tomek':
            resampler = SMOTETomek(random_state=random_state)
        elif technique == 'Random Oversampling':
            resampler = RandomOverSampler(random_state=random_state)
        else:
            pass
        X = self.df.drop('TARGET', axis=1)
        y = self.df['TARGET']
        self.X_resampled, self.y_resampled = resampler.fit_resample(X, y)
        return self.X_resampled, self.y_resampled

    def processAlgorithm(self,algorithm,random_state,k):
        self.kf = KFold(n_splits=k, shuffle=True, random_state=random_state)
        if algorithm == 'Logistic Regression':
            model = LogisticRegression(random_state=random_state,max_iter=10000)
        elif algorithm == 'Decision Tree':
            model = DecisionTreeClassifier(random_state=random_state)
        elif algorithm == 'Random Forest':
            model = RandomForestClassifier(random_state=random_state)
        elif algorithm == 'K-Nearest Neighbors':
            model = KNeighborsClassifier()
        elif algorithm == 'Category Boosting':
            model = CatBoostClassifier(random_state=random_state, verbose=0)
        else:
            pass
        self.trained_model = self.processModel(model)
        return self.trained_model
    def processModel(self,model):
        for train_index, test_index in self.kf.split(self.X_resampled):
            X_train, X_test = self.X_resampled.iloc[train_index], self.X_resampled.iloc[test_index]
            y_train, y_test = self.y_resampled.iloc[train_index], self.y_resampled.iloc[test_index]

            # Train model
            model.fit(X_train, y_train)
        return model
    def processEvaluation(self,model):
        accuracies = []
        precisions = []
        recalls = []
        f1_scores = []
        for train_index, test_index in self.kf.split(self.X_resampled):
            X_train, X_test = self.X_resampled.iloc[train_index], self.X_resampled.iloc[test_index]
            y_train, y_test = self.y_resampled.iloc[train_index], self.y_resampled.iloc[test_index]

            # Train model
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # Calculate metrics
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, zero_division=1)
            recall = recall_score(y_test, y_pred, zero_division=1)
            f1 = f1_score(y_test, y_pred, zero_division=1)

            accuracies.append(accuracy)
            precisions.append(precision)
            recalls.append(recall)
            f1_scores.append(f1)

        mean_accuracy = round(sum(accuracies) / len(accuracies),4)
        mean_precision = round(sum(precisions) / len(precisions),4)
        mean_recall = round(sum(recalls) / len(recalls),4)
        mean_f1 = round(sum(f1_scores) / len(f1_scores),4)
        self.dfEva = pd.DataFrame({
            'Accuracy': [mean_accuracy],
            'Precision': [mean_precision],
            'Recall': [mean_recall],
            'F1-Score': [mean_f1]
        })
        return self.dfEva
    
