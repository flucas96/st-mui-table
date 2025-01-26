# Streamlit MUI Table

The **Streamlit MUI Table** component brings the Material UI Table to Streamlit applications. It allows for displaying tables with features such as pagination, expandable rows, and customizable styles. A key feature is the ability to render HTML within the table cells, providing flexibility for displaying styled content. The component also supports row selection.

---

## Installation

Install the component using pip:

```bash
pip install st_mui_table
```

---

## Usage

To use the `st_mui_table` component, import it into your Streamlit script and call it like any other Streamlit function:

```python
from st_mui_table import st_mui_table

# Example usage
st_mui_table(
    df,
    enablePagination=True,
    customCss="",
    paginationSizes=[5, 10, 25],
    size="medium",
    padding="normal",
    showHeaders=True,
    key="mui_table",
    stickyHeader=True,
    paperStyle={
        "width": '100%',
        "overflow": 'hidden',
        "paddingBottom": '1px',
        "border": '2px solid rgba(224, 224, 224, 1)'
    },
    detailColumns=[],
    detailColNum=1,
    detailsHeader="Details",
    showIndex=False
)
```

---

## Features

### Render HTML in Table Cells
The table supports rendering HTML directly within cells. For example, if a cell contains `<b>bold</b>`, the text will be rendered as bold. This feature provides significant flexibility but requires caution if users can influence table content.

### Expandable Rows
You can define specific columns (`detailColumns`) that are hidden from the main table but displayed in an expandable section when a row is expanded. The layout of this section is configurable using `detailColNum`.

### Row Selection
The table supports row selection, allowing users to interact with specific rows.

---

## Parameters

- **`df`**: The DataFrame to display in the table.
- **`enablePagination`** (bool): Enables pagination. Default: `True`.
- **`paginationLabel`** (str): Label for pagination. Default: "Rows per page".
- **`showFirstButtonPagination`** (bool): Show the "first page" button in pagination. Default: `True`.
- **`showLastButtonPagination`** (bool): Show the "last page" button in pagination. Default: `True`.
- **`customCss`** (str): Custom CSS for styling the table. Example: `.MuiTableCell-root {color:red;}`. Default: `""`.
- **`paginationSizes`** (list): Defines the number of rows per page options. Default: `[5, 10, 25]`.
- **`size`** (str): Table cell size. Options: `"small"`, `"medium"`. Default: `"medium"`.
- **`padding`** (str): Table cell padding. Options: `"normal"`, `"checkbox"`, `"none"`. Default: `"normal"`.
- **`minHeight`** (int): Minimum height of the table. Default: `None`.
- **`maxHeight`** (int): Maximum height of the table. Default: `None`.
- **`showHeaders`** (bool): Show column headers. Default: `True`.
- **`key`** (str): Unique key for the table instance. Default: `"mui_table"`.
- **`stickyHeader`** (bool): Make the table header sticky. Default: `True`.
- **`paperStyle`** (dict): Custom styles for the table container. Default: `{ "width": '100%', "overflow": 'hidden', "paddingBottom": '1px', "border": '2px solid rgba(224, 224, 224, 1)' }`.
- **`detailColumns`** (list): Columns to display in the expandable row section. Default: `[]`.
- **`detailColNum`** (int): Number of columns in the expandable section. Options: `1`, `2`, `3`. Default: `1`.
- **`detailsHeader`** (str): Header text for the expandable section. Default: `"Details"`.
- **`showIndex`** (bool): Show the DataFrame index as a separate column. Default: `False`.
- **`enable_sorting`** (bool): Enable sorting on table columns. Default: `False`.
- **`return_clicked_cell`** (bool): Return data about the clicked cell (row, column, and content). Default: `False`.

---

## Example: Expandable Rows

```python
from st_mui_table import st_mui_table
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Details": ["<b>Alice's details</b>", "<b>Bob's details</b>", "<b>Charlie's details</b>"]
}
df = pd.DataFrame(data)

# Define detailColumns
st_mui_table(
    df,
    detailColumns=["Details"],
    detailColNum=1,
    detailsHeader="User Details",
    enablePagination=True,
    showIndex=True
)
```

---

## Notes

- **HTML Rendering**: Ensure proper validation of any HTML content in the DataFrame to avoid unexpected behavior or vulnerabilities.
- **Pagination**: The first value in `paginationSizes` defines the default rows per page.

This component simplifies table creation in Streamlit, enabling rich features and customization with minimal effort.