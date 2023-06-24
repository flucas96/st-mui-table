import streamlit  as st
from st_mui_table import st_mui_table
from typing import Dict

import numpy as np
import pandas as pd

import datetime 

st.set_page_config(layout="wide")



# Create a sample DataFrame
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
df.iloc[0, 2] = "<b>bold</b>"

df.rename(columns={'A': '<b>date</b>'}, inplace=True)

st.title('Streamlit MUI Table Example')

st.header('Original DataFrame')
st.dataframe(df)

st.header('MUI Table')
customCss = """
    .MuiTableContainer-root {
        border: 1px solid red;
    }
"""
st_mui_table(df, enablePagination=True,  paginationSizes = [5,10,25], additionalColumns=["E","B"])

st.write("test")