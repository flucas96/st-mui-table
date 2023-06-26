import streamlit.components.v1 as components
import os

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_mui_table",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_mui_table", path=build_dir)

def st_mui_table(df, enablePagination=True, customCss="", paginationSizes = [5,10,25], size="medium", padding="normal", showHeaders=True, key="mui_table", stickyHeader=True,
                 paperStyle={ "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid rgba(224, 224, 224, 1)'}, detailColumns=[], detailColNum=1,
                 detailsHeader="Details",showIndex=False):
    """
    Parameters
    ----------
    df : pandas DataFrame
    enablePagination: bool
    customCss : str
    size: str, size of the table cells, can be "small", "medium"
    padding: str, padding of the table cells, can be "normal", "checkbox", "none"
    showHeaders: bool, whether to show column headers
    key : str
    stickyHeader: bool, whether to make the header sticky
    paperStyle: dict, style of the table
    detailColumns: list, list of columns to show in the details
    detailColNum: int, number of columns to show in the details
    detailsHeader: str, header of the details
    showIndex: bool, whether to show the index column

    """
    df_copy = df.copy()
    df_copy.fillna("", inplace=True)  # Replace NaN with empty string



    content = df_copy.to_dict('records')  # Convert DataFrame to list of dicts
    #Convert all columns to string

    component_value = _component_func(content=content, enablePagination=enablePagination, 
                                      size=size, padding=padding, showHeaders=showHeaders,
                                      key=key, customCss=customCss, paginationSizes=paginationSizes, stickyHeader=stickyHeader, paperStyle=paperStyle,
                                      detailColumns=detailColumns,detailColNum=detailColNum,detailsHeader=detailsHeader,showIndex=showIndex)
