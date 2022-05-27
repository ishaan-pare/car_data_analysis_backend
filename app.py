from flask import Flask, request
from flask_cors import CORS, cross_origin
from utils.QueryProcesser import processor
from utils.modelPredictions import predict
import pandas as pd
import json


"""
    Flask application 
    initiallised and added cors layer
"""
app = Flask(__name__)
cors = CORS(app)


#for relationship between features

#Route for getting correlation coefficient data
@app.route("/corr_coeffs", methods=["get"])
@cross_origin()
def get_corr_coeffs():
    with open("compiled_data/corr_coeffs.json") as f:
        obj_file = json.load(f)
        f.close()
        return obj_file


#most dependent features column
@app.route("/m_attr", methods=["get"])
@cross_origin()
def get_m_attr():
    with open("compiled_data/m_attr.json", "r") as f:
        obj = json.load(f)
        f.close()
    return obj


#----------end of relationship routes-----------#

#for query processing
@app.route("/query")
@cross_origin()
def query_manager():
    query_str = request.args.get("q")
    result = processor(query_str)

    return result


#for visualizer data
@app.route("/get_visuals_data", methods=["get"])
@cross_origin()
def get_visual_data():
    with open("compiled_data/features_data.json") as f:
        obj = json.load(f)
        f.close()
    return obj


#for model predictions
@app.route("/predict", methods=["get"])
@cross_origin()
def get_results():
    print(request.args.get("q"))
    query = request.args.get("q")
    dis = query.split(" ")
    haves = dis[0].split(",")
    toPredict = dis[1]

    data = haves[1:]
    known = haves[0]
    data = [float(o) for o in data]
   
    res = predict(toPredict, known, data)
    result = [i for i in data]
    
    print(type(res))
    print(res)

    # if type(res) == "<class 'numpy.ndarray'>":
    #     res = list(res)
    #     res[0] = list(res[0])

    result.extend(res)



    softFeatures = ["Power_perf_factor", "Horsepower", "__year_resale_value", "Fuel_efficiency"]
    hardFeatures = ["Wheelbase","Fuel_capacity","Width", "Engine_size", "Length"]
 
    if known == "SoftFeatures":
        label = softFeatures
    elif known == "HardFeatures":
        label = hardFeatures
    elif known == "Sales":
        label = ["Sales"]
    else:
        label = ["Price"]

    if toPredict == "SoftFeatures":
        label.extend(softFeatures)
    elif toPredict == "HardFeatures":
        label.extend(hardFeatures)
    elif toPredict == "Sales":
        label.extend(["Sales"])
    else:
        label.extend(["Price"])
    

    result = list(result)
    label = list(label)
    print(result)
    return {"result": result, "headers": label}


@app.route("/carsegments", methods=["get"])
@cross_origin()
def getPieData():
    with open("compiled_data/segments.json", "r") as f:
        obj = json.load(f)
        f.close()
        return obj

if __name__ == "__main__":
    app.run()