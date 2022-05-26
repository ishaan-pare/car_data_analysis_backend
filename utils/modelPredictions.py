import pickle


def predict(attrP, attrH, data):
    if attrP == "Price" and attrH == "HardFeatures":
        return Price_HardFeatures(data)
    elif attrP == "Sales" and attrH == "HardFeatures":
        return Sales_HardFeatures(data)
    elif attrP == "Price" and attrH == "SoftFeatures":
        return Price_SoftFeatures(data)
    elif attrP == "Sales" and attrH == "SoftFeatures":
        return Sales_SoftFeatures(data)
    elif attrP == "HardFeatures" and attrH == "SoftFeatures":
        return HardFeatures_SoftFeatures(data)
    elif attrP == "Sales" and attrH == "Price":
        return Sales_Price(data)
    elif attrP == "SoftFeatures" and attrH == "Price":
        return SoftFeatures_Price(data)
    elif attrP == "HardFeatures" and attrH == "Price":
        return HardFeatures_Price(data)
    


def Price_HardFeatures(data): 
    try:
        with open("trained_model/price_vs_hardF" , "rb") as f:
            model = pickle.load(f)
            f.close()
    except Exception as err:
        pass
    return(model.predict([data]))

def Sales_HardFeatures(data):
    price = Price_HardFeatures(data)

    with open("trained_model/sales_vs_price", "rb") as f:
        model = pickle.load(f)
        f.close()
    price = list(price)
    return(model.predict([[price[0]]]))    

def Price_SoftFeatures(data):

    #"Power_perf_factor", "Horsepower", "__year_resale_value", "Fuel_efficiency"
    with open("trained_model/price_vs_softF", "rb") as f:
        model = pickle.load(f)
        f.close()
    return model.predict([data])[0]

def Sales_SoftFeatures(data):
    with open("trained_model/sales_vs_softF", "rb") as f:
        model = pickle.load(f)
        f.close()
    return model.predict([data])

    
def HardFeatures_SoftFeatures(data):
    with open("trained_model/hardF_vs_softF", "rb") as f:
        model = pickle.load(f)
        f.close()
    return model.predict([data])

def Sales_Price(data):
    with open("trained_model/sales_vs_price", "rb") as f:
        model = pickle.load(f)
        f.close()
    return model.predict([data])

def SoftFeatures_Price(data):
    with open("trained_model/softF_vs_price", "rb") as f:
        model = pickle.load(f)
        f.close()
    return model.predict([data])[0]

def HardFeatures_Price(data):
    softF = SoftFeatures_Price(data)
    hardF = HardFeatures_SoftFeatures(softF)

    return hardF[0]





