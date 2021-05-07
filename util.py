import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__model1 = None


def get_estimated_price(location, total_sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model1.predict([x])[0], 2)


def get_location_names():
    return __locations


def load_saved_artifacts() -> object:
    print("Loading saved artifacts")
    global __data_columns
    global __locations
    global __model1

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model1
    if __model1 is None:
        with open("./artifacts/Datascience.pickle", 'rb') as f:
         __model1 = pickle.load(f)

    print("Loading the artifacts is done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
