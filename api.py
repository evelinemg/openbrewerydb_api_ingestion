from pyspark.sql import SparkSession
import requests
import json
from constants import base_url, params

def makeSparkSession(name="Teste", master="local"):
    spark= SparkSession \
        .builder \
        .appName(name) \
        .config("spark.master",master) \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark


def getApi(base_url, params, response=[]):
    try:
        api_response=requests.get(base_url,params).json()
        
        if not api_response:
            return response
            
        response.extend(api_response)
        params['page']+=1
        
        return getApi(base_url,params,response)
    except Exception as e:
        raise Exception(f"Error! {e}")


def makeDfAndSparkSession():
    spark=makeSparkSession()
    response=getApi(base_url,params)
    df=spark.createDataFrame(data=response)
    return df, spark


if __name__ == '__main__':
    df,spark=makeDfAndSparkSession()
    df.show()