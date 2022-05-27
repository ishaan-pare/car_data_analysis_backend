from dis import dis
from email import header
from unittest import result
import pandas as _pd
import json


# first word of query
keywords = {
    "popular": 0,
    "max": 1,
    "min": 2,
}
# after noun
specifier = {
    "having": 0,
    "under": 1,
    "between": 2
}
# after keyword
nouns = {
    "wheelbase": 0,
    "width": 1,
    "fuelcapacity": 2,
    "enginesize": 3,
    "length": 4,
    "powerperffactor": 5,
    "horsepower": 6,
    "fuelefficiency": 7,
    "yearresalevalue": 8,
    "price": 9,
    "sales": 10,
    "features": 11,
}
# only for length of query = 2


# predifiend features in dataset
features = ["Wheelbase", "Width", "Fuel_capacity", "Engine_size", "Length", "Power_perf_factor",
            "Horsepower", "Fuel_efficiency", "__year_resale_value", "Price_in_thousands", "Sales_in_thousands"]


# 0          1       2      0     1
#popuar wheelbase having max horsepower -> connector
#max wheelbase under 10 to 12
#min
def processor(query):
    dist = query.split(" ")
    
    df = _pd.read_csv("cars_data_preprocessed_final.csv")

    ans = get_result(df, dist)
    

    result = {"result": [], "headers": []}
    result["headers"] = list(ans.columns)
    result["result"] = list(ans.iloc[0])

    return result

def get_result(df, query):
    if len(query) == 2:
        if query[0] == "popular":
            fullC = df.loc[(df["Sales_in_thousands"].max() == df["Sales_in_thousands"])]
            if query[1]!="features":
                required_col = _pd.get_dummies(fullC[[features[nouns["sales"]],features[nouns[query[1]]]]])
            else:
                required_col = _pd.get_dummies(fullC[features])
            return required_col
        elif query[0] == "max":
            fullC = df.loc[(df[features[nouns[query[1]]]].max() == df[features[nouns[query[1]]]])]
            if query[1]!="features":
                required_col = _pd.get_dummies(fullC[[features[nouns[query[1]]]]])
            else:
                required_col = _pd.get_dummies(fullC[features])
            return required_col
    
    else:
        if query[2] == "having":
            pass
        elif query[2] == "under":
            pass
        elif query[2] == "between":
            obj = df.loc[(df[features[nouns[query[5]]]]).between(float(query[3]),float(query[4]))]
            

            if query[0] == "popular":
                a = obj.loc[(obj["Sales_in_thousands"].max() == obj["Sales_in_thousands"])]
            else:
                a = obj.loc[(obj[features[nouns[query[1]]]].max() == obj[features[nouns[query[1]]]])]
            
            if query[1] == "features":
                return _pd.get_dummies(a[features])

            return _pd.get_dummies(a[[features[nouns["sales"]],features[nouns[query[1]]]]])

