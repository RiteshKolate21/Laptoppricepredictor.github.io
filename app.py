from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle as pkl


app = Flask(__name__)

dataset = pd.read_csv("Finald.csv")


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/lap-prediction")
def lapprediction():    
    dataset = pd.read_csv("Finald.csv")
    companies = sorted(dataset["Company"].unique())
    TypeName = sorted(dataset["TypeName"].unique())
    Rams = sorted(dataset["Ram"].unique())
    Weight = sorted(dataset["Weight"].unique())
    Price = sorted(dataset["Price"].unique())
    Ips = sorted(dataset["Ips"].unique())
    ppi = sorted(dataset["ppi"].unique())
    Cpu_brand = sorted(dataset["Cpu_brand"].unique())
    HDD = sorted(dataset["HDD"].unique())
    SSD = sorted(dataset["SSD"].unique())
    Gpu_brand = sorted(dataset["Gpu_brand"].unique())
    os = sorted(dataset["os"].unique())
   


    return render_template("lapprediction.html", companies = companies, TypeName = TypeName,
                           Rams=Rams,Weight=Weight,Price=Price,Ips=Ips,ppi=ppi,Cpu_brand=Cpu_brand,
                          HDD=HDD,SSD=SSD,Gpu_brand=Gpu_brand,os=os)


@app.route("/lap-price-prediction-result")
def lappricepredictionresult():
    Company = request.args.get("Company")
    TypeName = request.args.get("TypeName")
    Ram = int(request.args.get("Ram"))

    Weight = float(request.args.get("Weight"))
    Touchscreen = int(request.args.get("Touchscreen"))
    Ips = int(request.args.get("Ips"))
    ppi = float(request.args.get("ppi"))
    Cpu_brand = request.args.get("Cpu_brand")
    HDD = int(request.args.get("HDD"))
    SSD = int(request.args.get("SSD"))
    Gpu_brand = request.args.get("Gpu_brand")
    os = request.args.get("os")

    model = pkl.load(open('FinalPickle.pkl','rb'))
    
    myinput = pd.DataFrame(data=[[Company,TypeName,Ram,Weight,Touchscreen,Ips,ppi,Cpu_brand,HDD,SSD,Gpu_brand,os]],columns=['Company','TypeName','Ram','Weight','Touchscreen','Ips','ppi','Cpu_brand','HDD','SSD','Gpu_brand','os'])
    print(myinput)
    result = model.predict(myinput)

    return render_template("lappricepredictionresult.html",Company=Company,TypeName=TypeName,Ram=Ram,Weight=Weight,Touchscreen=Touchscreen,Ips=Ips,ppi=ppi,Cpu_brand=Cpu_brand,HDD=HDD,SSD=SSD,Gpu_brand=Gpu_brand,os=os,result = int(result[0][0]))

if __name__=="__main__":
    app.run(debug=True)