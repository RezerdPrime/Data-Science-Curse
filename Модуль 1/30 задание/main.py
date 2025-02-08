import pandas as pd
import pickle

from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector
from sklearn.svm import SVC

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import LogisticRegression


def filter_data(df):
    columns_to_drop = [
        'id', 'url', 'region', 'region_url', 'price',
        'manufacturer', 'image_url', 'description',
        'posting_date', 'lat', 'long'
    ]
    return df.drop(columns_to_drop, axis=1)


def remove_outliers(df):
    q25 = df['year'].quantile(0.25)
    q75 = df['year'].quantile(0.75)
    iqr = q75 - q25
    bound = (q25 - 1.5 * iqr, q75 + 1.5 * iqr)
    
    df.loc[df['year'] < bound[0], 'year'] = round(bound[0])
    df.loc[df['year'] > bound[1], 'year'] = round(bound[1])
    
    return df


def add_features(df):
    df['short_model'] = df['model'].apply(lambda x: x.lower().split(' ')[0] if pd.notnull(x) else x)
    df['age_category'] = df['year'].apply(lambda x: 'new' if x > 2013 else ('old' if x < 2006 else 'average'))
    return df


def main():

    df = pd.read_csv('homework.csv')

    preprocessor = Pipeline(steps=[
        ('filter', FunctionTransformer(filter_data)),
        ('remove_outliers', FunctionTransformer(remove_outliers)),
        ('add_features', FunctionTransformer(add_features))
    ])

    df = preprocessor.fit_transform(df)

    numerical = df.select_dtypes(include=['int64', 'float64']).columns
    categorical = df.select_dtypes(include=['object']).columns

    for feat in categorical:
        df[feat].fillna(df[feat].mode()[0], inplace=True)

    for feat in numerical:
        df[feat].fillna(df[feat].median(), inplace=True)

    x = df.drop(['price_category'], axis=1)
    y = df['price_category']

    numerical_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    preprocessing = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, make_column_selector(dtype_include=['int64', 'float64'])),
            ('cat', categorical_transformer, make_column_selector(dtype_include=object))
    ])

    models = {
        'Logistic Regression': Pipeline(steps=[
            ('preprocessor', preprocessing),
            ('classifier', LogisticRegression(solver='liblinear'))
        ]),
        'Random Forest': Pipeline(steps=[
            ('preprocessor', preprocessing),
            ('classifier', RandomForestClassifier())
        ]),
        'Support Vector Classifier': Pipeline(steps=[
            ('preprocessor', preprocessing),
            ('classifier', SVC())
        ])
    }

    best_score = 0
    best_model = None

    for name, model in models.items():
        score = cross_val_score(model, x, y, cv=4, scoring='accuracy').mean()
        print(f'Model: {name}, Accuracy: {score:.4f}')
        
        if score > best_score:
            best_score = score
            best_model = model

    best_model.fit(x, y)
    with open('bestmodel.pkl', 'wb') as file:
        pickle.dump(best_model, file)

    print(f'Model saved')


if __name__ == '__main__':
    main()
