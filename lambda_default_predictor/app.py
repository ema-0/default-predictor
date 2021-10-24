import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model
import json


def handler(event, context):
    model_folder_path = './trained_model/'

    with open(model_folder_path + 'categories.txt', 'rb') as fp:
        categories = pickle.load(fp)

    with open(model_folder_path + 'numerics_columns.txt', 'rb') as fp:
        numerics_columns = pickle.load(fp)

    model = load_model(model_folder_path + 'model.h5')
    if 'body' in event.keys():
        event = json.loads(event['body'])

    df = pd.DataFrame(pd.Series(event)).T
    df = df.fillna(-1)
    if 'body' not in event.keys():
        df = df.replace(to_replace={'nan': -1, 'True': True, 'False': False})

    df_numerics = df[numerics_columns]
    n_rows = df.shape[0]

    one_hot_list = []
    for key, value in categories.items():
        indexes = df[key].apply(lambda x: value.index(x))
        one_hot = np.zeros((n_rows, len(value)))
        one_hot[range(n_rows), indexes] = 1
        one_hot_list.append(one_hot)

    X_pred = np.concatenate([df_numerics] + one_hot_list, axis=1).astype('float32')
    y_pred = model.predict(X_pred)

    pr = str(y_pred[0, 0])

    return {
        'statusCode': 200,
        'body': pr
    }


