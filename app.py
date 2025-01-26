import streamlit  as st
from st_mui_table import st_mui_table
from typing import Dict

import numpy as np
import pandas as pd

import datetime 
import random
from datetime import datetime, timedelta



st.set_page_config(layout="wide")

#Generate random data
# Set a seed so the random values are the same each time you run the code
np.random.seed(24)

# Generate a list of random dates
date_today = datetime.now()
days = pd.date_range(date_today, date_today + timedelta(19), freq='D').strftime('%m/%d/%Y').tolist()

# Generate a list of product names
products = ['Product ' + str(i) for i in range(1, 6)]

# Generate a DataFrame
df = pd.DataFrame({
    'Date': days,
    'Product': [random.choice(products) for _ in range(20)],
    'Units Sold': [random.randint(1, 100) for _ in range(20)],
    'Unit Price': [round(random.uniform(10.5, 100.5), 2) for _ in range(20)]
})


# Calculate the Total Sales and add as a new column
df['Total Sales'] = df['Units Sold'] * df['Unit Price']
df["Total Sales"] =  df["Total Sales"].round(2)
st.title('Streamlit Mui Table Component Demo')
st.divider()
st.title('Basic Usage')



#gernate random dataframe


col_left, col_right = st.columns((1,1))

with col_left:

    st_mui_table(df,key="Table1")

with col_right:
    st.code("""
    st_mui_table(df,key="table2")
    """, language="python")

    st.markdown("<b>Input Dataframe", unsafe_allow_html=True)
    st.dataframe(df)


st.divider()

st.title('HTML Styling in Cells')

st.write("You can use HTML to style the cells")

col_left, col_right = st.columns((1,1))

df2 = df.copy()
df2['Total Sales'] = df2['Total Sales'].apply(lambda x: f"<b>{x}</b>")

with col_left:
    st_mui_table(df2,key="table2")

with col_right:
    st.code("""
    df2 = df.copy()
    df2['Total Sales'] = df2['Total Sales'].apply(lambda x: f"<b>{x}</b>")
    st_mui_table(df2,key="table2")
    """, language="python")

    st.markdown("<b>Input Dataframe", unsafe_allow_html=True)
    st.dataframe(df2)


st.divider()

st.title('Pagination - Size - Padding - Header')

st.write("You can enable pagination, change the size of the cells, change the padding of the cells and hide the header")
col_left, col_right = st.columns((1,1))

with col_right:

    pagination = st.checkbox("**Enable Pagination**", value=True)
    col1, col2 = st.columns((1,1))
    with col1:
        skipfirst = st.checkbox("**Skip to first Page Button**", value=True)
    with col2:
        skiplast = st.checkbox("**Skip to last Page Button**", value=True)
    pagination_label = st.text_input("**Pagination Label**", value="Rows per page",disabled= not pagination)
    minHeight = st.number_input("**Min Height**", value=200)
    maxHeight = st.number_input("**Max Height**", value=400)



    size = st.selectbox("**Size**", ["small", "medium"], index=1)
    padding = st.selectbox("**Padding**", ["normal", "checkbox", "none"], index=0)
    showHeaders = st.checkbox("**Show Headers**", value=True)
    stickyHeader = st.checkbox("**Sticky Header**", value=True)

    st.code(f"""
    st_mui_table(df2,key="table3", enablePagination={pagination}, size={size}, padding={padding}, showHeaders={showHeaders}, stickyHeader={stickyHeader}, maxHeight={maxHeight},
                 minHeight={minHeight}, paginationLabel={pagination_label}, showLastButtonPagination={skiplast}, showFirstButtonPagination={skipfirst})
    """, language="python")

with col_left:
    st_mui_table(df2,key="table3", enablePagination=pagination, size=size, padding=padding, showHeaders=showHeaders, stickyHeader=stickyHeader,maxHeight=maxHeight,minHeight=minHeight,
                 paginationLabel=pagination_label, showLastButtonPagination=skiplast, showFirstButtonPagination=skipfirst)

st.divider()

st.title('Details')

st.write("You can add a details section to each row. You can specify the number of columns to show in the details and the header of the details section")

col_left, col_right = st.columns((1,1))

with col_right:
    
        detailColumns = st.multiselect("**Detail Columns**", df.columns, default=["Date", "Product"])
        detailColNum = st.slider("**Number of Detail Columns**", min_value=0, max_value=len(detailColumns), value=1)
        detailsHeader = st.text_input("**Details Header**", value="<b>Details</b>")
        st.code("""
        for col in detailColumns:
            df.rename(columns = {col:f"<b>{col}</b>"}, inplace = True)
        detailColumns = [f"<b>{col}</b>" for col in detailColumns]
        st_mui_table(df2,key="table4", detailColumns={detailColumns}, detailColNum={detailColNum}, detailsHeader={detailsHeader})
        """, language="python")

with col_left:
    for col in detailColumns:
        df2.rename(columns = {col:f"<b>{col}</b>"}, inplace = True)
    detailColumns = [f"<b>{col}</b>" for col in detailColumns]


    st_mui_table(df2,key="table4", detailColumns=detailColumns, detailColNum=detailColNum, detailsHeader=detailsHeader)

st.divider()

st.title('Custom CSS')

st.write("You can add custom CSS to the table")

col_left, col_right = st.columns((1,1))

with col_right:
        
            customCss = st.text_area("**Custom CSS**", value="""
            .MuiTableCell-root {
                border: 2px solid green;
            }
            """)

            paperCSS  = { "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid red'}

            st.code("""
            paperCSS  = { "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid red'}
            st_mui_table(df2,key="table5", customCss={customCss}, paperStyle=paperCSS)
            """, language="python")

with col_left:
    st_mui_table(df2,key="table5", customCss=customCss, paperStyle=paperCSS)


st.divider()

st.title('Displaying Images & Sorting')

st.write("You can display images in the table")

col_left, col_right = st.columns((1,1))

with col_right:
    st.write("You can enable sorting by columns:")
    sorting = st.checkbox("**Enable Sorting**", value=False)
    df2["Product Image"] = """<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/220px-Kittyply_edit1.jpg" height="100px" alt="Cat!" />"""

    st.write("We can add images by adding a column with the HTML code for the image:")
    st.code("""df2["Product Image"] = "<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Kittyply_edit1.jpg/220px-Kittyply_edit1.jpg" height="100px" alt="Cat!" />""")

with col_left:
    st_mui_table(df2,key="table6", detailColumns=detailColumns, detailColNum=detailColNum, detailsHeader=detailsHeader, enable_sorting=sorting)


st.divider()

st.title('Enable Selecting')


col_left, col_right = st.columns((1,1))



with col_left:
    return_value = st_mui_table(df2,key="table7", detailColumns=detailColumns, detailColNum=detailColNum, detailsHeader=detailsHeader, enable_sorting=sorting, return_clicked_cell=True)

    st.write("You can get the value of the clicked cell:")
    st.write(return_value)


