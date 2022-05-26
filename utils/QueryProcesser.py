import pandas as _pd
import json
def transform_query(query):
    dist = query.split(' ')

    return dist

def get_result(dist):
    if dist[0] == "popular":
        if dist[1] == "features":
            data = _pd.read_csv("cars_data_preprocessed_final.csv")

            data_p1 = _pd.get_dummies(data[["Wheelbase", "Width", "Fuel_capacity", "Engine_size", "Length", "Power_perf_factor", "Horsepower", "Fuel_efficiency", "__year_resale_value", "Price_in_thousands", "Sales_in_thousands"]])
            data_p2 = data_p1.loc[(data_p1["Sales_in_thousands"].max() == data_p1["Sales_in_thousands"])]

            result = {"result": [], "headers": ["Wheelbase", "Width", "Fuel_capacity", "Engine_size", "Length", "Power_perf_factor", "Horsepower", "Fuel_efficiency", "__year_resale_value", "Price_in_thousands", "Sales_in_thousands"]}

            
            result["result"].append(list(data_p2.iloc[0]))
            result["result"] = (result["result"][0][:])


            with open("compiled_data/features.json", "r") as f:
                ob = json.load(f)

            f.close()
            return result

        else:
            pass
        
    else:
        pass




"""
    best, max, min, popular->sales, inbudget 3,4 features

    features, $[indiv features], sales
"""