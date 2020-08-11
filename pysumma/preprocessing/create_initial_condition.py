from osgeo import gdal
import pandas as pd
import os
import numpy as np

class InitialCondition(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def tif_to_dataframe(self, path):
        raster = gdal.Open(path)
        rasterArray = raster.ReadAsArray()
        df = pd.DataFrame(rasterArray)
        return df

    def tif_to_dataframe_one_col(self, path, col_name):
        raster = gdal.Open(path)
        rasterArray = raster.ReadAsArray()
        df = pd.DataFrame(rasterArray)
        one_col = pd.concat([pd.DataFrame(df.loc[:,[i]].values, columns=[col_name]) for i in range(len(df.columns))], ignore_index=True)
        return one_col

    def delete_number(self, df, number):
        df.replace(number, np.nan, inplace=True)
        df_new = df.dropna().astype('int64')
        return df_new

    def merge_mukey_soil_depth(self, df, soil_depth_df):
        mukey_depth = df.merge(soil_depth_df, on='MUKEY')
        return mukey_depth