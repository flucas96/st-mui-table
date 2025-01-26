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

def st_mui_table(df, enablePagination:bool=True, customCss:str="", paginationSizes:list = [5,10,25], size:str="medium", padding:str="normal", showHeaders:bool=True,
                 key:str="mui_table", stickyHeader:bool=True, paperStyle:dict={ "width": '100%',  "overflow": 'hidden',"paddingBottom": '1px', "border": '2px solid rgba(224, 224, 224, 1)'}, 
                 detailColumns:list=[], detailColNum:int=1, detailsHeader:str="Details",showIndex: bool=False, maxHeight: int=None, minHeight: int=None,paginationLabel:str="Rows per page",
                 showLastButtonPagination:bool=True, showFirstButtonPagination:bool=True,enable_sorting:bool = False, return_clicked_cell:bool = False, default_value = None, selected_row_css = """.selected-row {background-color: #b3d4fc !important;}"""):
    """
    Parameters
    ----------
    df : pandas DataFrame
    enablePagination: bool
    paginationLabel: str - The Label that will be displayed left to the pagination feature.
    showFirstButtonPagination: bool - Whether to show the first page button in the pagination feature.
    showLastButtonPagination: bool - Whether to show the last page button in the pagination feature.
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
    maxHeight: int, maximum height of the table - if exceeded, a scrollbar will appear - if None no maxHeight will be applied.
    minHeight: int, minimum height of the table - if None no minHeight will be applied.

    return_clicked_cell: bool, whether to return the clicked cell
    default_value: str, default value of the returned clicked cell
    selected_row_css: str, css style of the selected row
    """

    df_copy = df.copy()
    df_copy.fillna("", inplace=True)  # Replace NaN with empty string



    content = df_copy.to_dict('records')  # Convert DataFrame to list of dicts
    #Convert all columns to string

    return_value = _component_func(content=content, enablePagination=enablePagination, 
                                      size=size, padding=padding, showHeaders=showHeaders,
                                      key=key, customCss=customCss, paginationSizes=paginationSizes, stickyHeader=stickyHeader, paperStyle=paperStyle,
                                      detailColumns=detailColumns,detailColNum=detailColNum,detailsHeader=detailsHeader,showIndex=showIndex,maxHeight = maxHeight,
                                      minHeight = minHeight,paginationLabel=paginationLabel, showLastButtonPagination=showLastButtonPagination, showFirstButtonPagination=showFirstButtonPagination,
                                        enable_sorting=enable_sorting, return_clicked_cell=return_clicked_cell, default_value=default_value, selected_row_css = selected_row_css)

    if return_clicked_cell:
        return return_value                   
