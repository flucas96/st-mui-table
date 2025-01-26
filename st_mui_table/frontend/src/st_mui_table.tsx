import React, { useEffect } from "react";
import { ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { Table, TableBody, TableCell, TableContainer, TablePagination, TableRow, Paper, TableHead, IconButton, Typography, TableSortLabel } from '@mui/material';
import Collapse from '@mui/material/Collapse';
import Box from '@mui/material/Box';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';



interface TableState {
    page: number;
    rowsPerPage: number;
}

function chunkArray<T>(originalArray: T[], chunkSize: number): T[][] {
  const array = [...originalArray];  // Create a copy of the original array
  const results = [];
  while (array.length) {
    results.push(array.splice(0, chunkSize));
  }
  return results;
}

const TableComponent = (props: ComponentProps) => {

  const { content, customCss, enablePagination, size, padding, showHeaders, paginationSizes, stickyHeader, paperStyle, detailColumns,detailColNum,
    detailsHeader,showIndex, maxHeight,minHeight, paginationLabel, showFirstButtonPagination, showLastButtonPagination, enable_sorting, selected_row_css   } = props.args;  // Python Args

  const [state, setState] = React.useState<TableState>({
    page: 0,
    rowsPerPage: paginationSizes[0],  // Set the default rowsPerPage to the first value in the list of options
  })

  const [sortOrder, setSortOrder] = React.useState<"asc" | "desc">("asc");
  const [orderBy, setOrderBy] = React.useState<string | null>(null);

  // State to track the selected row
  const [selectedRow, setSelectedRow] = React.useState<number | null>(null);


  const handleSortRequest = (property: string) => {
    const isAsc = orderBy === property && sortOrder === "asc";
    setSortOrder(isAsc ? "desc" : "asc");
    setOrderBy(property);
  };

  const handleCellClick = (rowIndex: number, columnName: string, cellData: any) => {
    if (props.args.return_clicked_cell) {
      const clickedCellData = {
        row: rowIndex,
        column: columnName,
        data: cellData
      };
      Streamlit.setComponentValue(clickedCellData);
    }
  };

    // Function to handle row click
    const handleRowClick = (rowIndex: number) => {
      setSelectedRow(rowIndex);
    };
  

  const sortedContent = React.useMemo(() => {
    if (enable_sorting && orderBy) { // Only sort if enable_sorting is true and orderBy is not null
      const comparator = (a: any, b: any) => {
        if (a[orderBy] < b[orderBy]) {
          return -1;
        }
        if (a[orderBy] > b[orderBy]) {
          return 1;
        }
        return 0;
      };
  
      return [...content].sort((a, b) => (sortOrder === "asc" ? comparator(a, b) : -comparator(a, b)));
    }
    return content; // If enable_sorting is false or orderBy is null, return the original content
  }, [content, orderBy, sortOrder, enable_sorting]);
  
  


  //if pagination is disabled, set rowsPerPage to -1
  useEffect(() => {
    if (!enablePagination) {
      setState((prev) => ({ ...prev, rowsPerPage: -1 }));
    }
    else {
      setState((prev) => ({ ...prev, rowsPerPage: paginationSizes[0] }));
    }
  }, [enablePagination]);

  const handleChangePage = (event: unknown, newPage: number) => {
    setState((prev) => ({ ...prev, page: newPage }));
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    event.persist();  // Remove the event from the pool
    setState((prev) => ({ ...prev, rowsPerPage: +event.target.value, page: 0 }));
  };

  const [expanded, setExpanded] = React.useState<number[]>([]);

const startRow = state.page * state.rowsPerPage;
const endRow = startRow + state.rowsPerPage;
const currentPageContent = content.slice(startRow, endRow);

const [shouldUpdateHeight, setShouldUpdateHeight] = React.useState(false);


const handleExpandClick = (i: number) => {
  const currentIndex = expanded.indexOf(i);
  const newExpanded = [...expanded];

  if (currentIndex === -1) {
    newExpanded.push(i);
  } else {
    newExpanded.splice(currentIndex, 1);
  }

  setExpanded(newExpanded);
  setShouldUpdateHeight(!shouldUpdateHeight);  // toggle shouldUpdateHeight state
};

useEffect(() => {
  if (tableRef.current) {
    const observer = new ResizeObserver(() => {
      Streamlit.setFrameHeight();
    });

    observer.observe(tableRef.current);

    return () => {
      observer.disconnect();
    };
  }
}, []);



const tableStyle = {
  maxHeight: maxHeight ? `${maxHeight}px` : undefined,
  minHeight: minHeight ? `${minHeight}px` : undefined,
  overflow: 'auto'
};const tableRef = React.useRef<HTMLDivElement>(null);


return (
  <>
    <style dangerouslySetInnerHTML={{__html: customCss}}></style>
    <style dangerouslySetInnerHTML={{__html: selected_row_css}}></style>
    <Paper sx={paperStyle}>
    <TableContainer ref={tableRef} style={tableStyle}>
      <Table stickyHeader={stickyHeader} aria-label="sticky table" size={size}>
        {showHeaders && (
          <TableHead>
            <TableRow>
              {showIndex && <TableCell></TableCell>}
              {detailColumns.length > 0 && <TableCell></TableCell>}
              {content[0] && Object.keys(content[0]).filter((header) => !detailColumns.includes(header)).map((header, i) => (
                <TableCell key={i} padding={padding} dangerouslySetInnerHTML={{__html: String(header)}}></TableCell>
              ))}
            </TableRow>
          </TableHead>
        )}
        <TableBody>
          {currentPageContent.map((row: any, rowIndex: number) => (
            <React.Fragment key={rowIndex}>
              <TableRow hover role="checkbox" tabIndex={-1} onClick={() => handleRowClick(rowIndex)}  className={rowIndex === selectedRow ? "selected-row" : ""}>
                {showIndex && <TableCell>{rowIndex + startRow}</TableCell>}
                {detailColumns.length > 0 && (
                  <TableCell>
                    <IconButton
                      onClick={(event) => {
                        event.stopPropagation();
                        handleExpandClick(rowIndex);
                      }}
                    >
                      {expanded.includes(rowIndex) ? <ExpandLessIcon /> : <ExpandMoreIcon />}
                    </IconButton>
                  </TableCell>
                )}
                {Object.entries(row).map(([columnName, cellData], columnIndex) => {
                  if (!detailColumns.includes(columnName)) {
                    return (
                      <TableCell 
                        key={`${rowIndex}-${columnIndex}`} 
                        onClick={() => handleCellClick(rowIndex + startRow, columnName, cellData)}
                        padding={padding}
                        style={{
                          wordWrap: "break-word",
                          whiteSpace: "normal",
                          overflowWrap: "break-word",
                        }}
                      >
                        <div dangerouslySetInnerHTML={{__html: String(cellData)}}></div>
                      </TableCell>
                    );
                  }
                  return null; 
                })}
              </TableRow>
              {detailColumns.length > 0 && (
                <TableRow>
                  <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                    <Collapse in={expanded.includes(rowIndex)} timeout="auto" unmountOnExit>
                      <Box margin={1}>
                        <Typography variant="h6" gutterBottom component="div" dangerouslySetInnerHTML={{__html: String(detailsHeader)}}></Typography>
                        <Table size="small" aria-label="purchases">
                          <TableBody>
                            {chunkArray(detailColumns as string[], detailColNum).map((chunk, i) => (
                              <TableRow key={i}>
                                {chunk.map((additionalColumn) => (
                                  <React.Fragment key={additionalColumn}>
                                    <TableCell dangerouslySetInnerHTML={{__html: additionalColumn}} />
                                    <TableCell dangerouslySetInnerHTML={{__html: String(row[additionalColumn])}} />
                                  </React.Fragment>
                                ))}
                              </TableRow>
                            ))}
                          </TableBody>
                        </Table>
                      </Box>
                    </Collapse>
                  </TableCell>
                </TableRow>
              )}
            </React.Fragment>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    {enablePagination && (
      <TablePagination
        rowsPerPageOptions={[...paginationSizes, { label: 'All', value: -1 }]}
        colSpan={3}
        count={content.length}
        rowsPerPage={state.rowsPerPage}
        page={state.page}
        SelectProps={{
          inputProps: { 'aria-label': 'rows per page' },
          native: true,
        }}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
        component="div"
        labelRowsPerPage = {paginationLabel}
        showFirstButton = {showFirstButtonPagination}
        showLastButton = {showLastButtonPagination}
      />
    )}
    </Paper>
  </>
);

  };
export default withStreamlitConnection(TableComponent);
