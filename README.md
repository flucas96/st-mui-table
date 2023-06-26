# 

# Streamlit MUI Table

This is a Streamlit custom component that brings Material UI Table component to your Streamlit apps. It allows to show a simple table in the MUI style. There are some parameters that can be used to customize the table. However, by no means this component is a full implementation of the MUI Table component. It is just a simple table that can be used to show data in a nice way. The most advanced features is that "detailColumns" can be defined that are shown when a row gest "expanded". 

Check out the [live demo](https://st-mui-table.streamlit.app/)!

## Installation

To install st_mui_table, you can use pip:

````
pip install st_mui_table
````

## Usage

To use the sst_mui_table component, you just need to import it in your Streamlit script and call it like any other Streamlit function:

```` python
from st_mui_table import st_mui_table
````
```` python
st_mui_table(
    df,
    enablePagination=True,
    customCss="",
    paginationSizes = [5,10,25],
    size="medium",
    padding="normal",
    showHeaders=True,
    key="mui_table",
    stickyHeader=True,
    paperStyle={ "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid rgba(224, 224, 224, 1)'},
    detailColumns=[],
    detailColNum=1,
    detailsHeader="Details",
    showIndex=False
    
)
````

## Note worthy
All HTML content will be correctly interpreted and rendered! Meaning if there is something like `<b>bold</b>` in the dataframe, it will be rendered as bold text. 
Keep that in mind if users can directly influence the content of the table.

## Parameters

- **df**: The dataframe to be shown in the table.
- **enablePagination**: If True, pagination is enabled. Default: True
- **customCss**: Custom CSS to be applied to the table. Can just be a string like  `.MuiTableCell-root {color:red;}`  Default: "". The text will be rendered in `<style>` tags above the component.
- **paginationSizes**: List of integers that define the number of rows per page. Default: [5,10,25] - The first number defined the amount of rows that will be displayed when the table first renders
- **size**: Size of the table. Can be "small", "medium" or "large". Default: "medium"
- **padding**: Padding of the table. Can be "normal", "checkbox" or "none". Default: "normal"
- **showHeaders**: If True, the headers of the table are shown. Default: True
- **key**: Key of the component. Default: "mui_table"
- **stickyHeader**: If True, the header of the table is sticky. Default: True
- **paperStyle**: Dictionary with the style of paper on which the table is on. Default: { "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid rgba(224, 224, 224, 1)'}
- **detailColumns**: List of columns that will be shown when a row is expanded. Default: [] - All Column in this list will not be displayed in the "normal" table anymore.
- **detailColNum**: Structure of the columns in the details seciont. If 1 all details will be shown beneath each other. If 2, the details will be shown in two columns. If the 3 details will be shown in three columns. Default: 1...
- **detailsHeader**: Header of the details section. Default: "Details"
- **showIndex**: If True, the index of the dataframe should be shown. Default: False