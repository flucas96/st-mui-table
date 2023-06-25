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
df.iloc[0, 2] = "<b>2022-05-06, vollkommen zufrieden </b><br> Der Abschluss der Versicherung lief sehr gut, allerdings habe ich noch keine Erfahrung mit der Schadensregulierung. Auch die Beiträge sind sehr günstig."
df.iloc[0, 3] = "<b>2022-05-06, vollkommen zufrieden </b><br> Der Abschluss der Versicherung lief sehr gut, allerdings habe ich noch keine Erfahrung mit der Schadensregulierung. Auch die Beiträge sind sehr günstig."

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

col_size = st.slider("Column Size", 0.1, 12.5, 0.1)
col1, col2 = st.columns((col_size,1))

with col1:
    st_mui_table(df, enablePagination=True,  paginationSizes = [5,10,25], detailColumns=["E","B","D"], detailColNum=2,minRowHeight=1000)

st.write("test")