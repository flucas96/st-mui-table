import React, { useEffect } from "react";
import { ComponentProps, Streamlit, withStreamlitConnection } from "streamlit-component-lib";
import { Table, TableBody, TableCell, TableContainer, TablePagination, TableRow, Paper, TableHead, IconButton, Typography } from '@mui/material';
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
    detailsHeader,showIndex  } = props.args;  // Python Args
  const [state, setState] = React.useState<TableState>({
    page: 0,
    rowsPerPage: paginationSizes[0],  // Set the default rowsPerPage to the first value in the list of options
  })

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

const tableRef = React.useRef<HTMLDivElement>(null);
return (
  <>
    <style dangerouslySetInnerHTML={{__html: customCss}}></style>
    <Paper sx={paperStyle}>
      <TableContainer ref={tableRef}>
        <Table stickyHeader={stickyHeader} aria-label="sticky table" size={size}>
          {showHeaders && (
            <TableHead>
              <TableRow>
                {showIndex && <TableCell>{/* This cell is for the index */}</TableCell>}
                {/* Add a new table cell for the expand button */}
                {detailColumns.length > 0 && <TableCell></TableCell>}
                {content[0] && Object.keys(content[0]).filter((header) => !detailColumns.includes(header)).map((header, i) => (
                  <TableCell key={i} padding={padding} dangerouslySetInnerHTML={{__html: String(header)}}></TableCell>
                ))}
              </TableRow>
            </TableHead>
          )}
          <TableBody>
            {currentPageContent.map((row: {[key: string]: any}, rowIndex: number) => {
              const isExpanded = expanded.includes(rowIndex);
              return (
                <React.Fragment key={rowIndex}>
                  <TableRow hover role="checkbox" tabIndex={-1}>
                    {showIndex && <TableCell>{rowIndex}</TableCell>}
                    {detailColumns.length > 0 && (
                      <TableCell>
                        <IconButton
                          onClick={(event) => {
                            event.stopPropagation(); // Prevent the row click event from firing
                            handleExpandClick(rowIndex);
                          }}
                        >
                          {isExpanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
                        </IconButton>
                      </TableCell>
                    )}
                    {Object.entries(row).map(([key, value], i) => {
                      if (!detailColumns.includes(key)) {
                        return (
                          <TableCell 
                            key={`${rowIndex}-${i}`} 
                            padding={padding} 
                            dangerouslySetInnerHTML={{__html: String(value)}}
                            style={{
                              wordWrap: "break-word",
                              whiteSpace: "normal",
                              overflowWrap: "break-word",
                            }}
                          />
                        );
                      }
                      return null;  // Return null when we don't want to render anything
                    })}
                  </TableRow>
                  {detailColumns.length > 0 && (
                    <TableRow>
                      <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                        <Collapse in={isExpanded} timeout="auto" unmountOnExit>
                          <Box margin={1}>
                          <Typography variant="h6" gutterBottom component="div" dangerouslySetInnerHTML={{__html: String(detailsHeader)}}></Typography>
                            <Table size="small" aria-label="purchases">
                            <TableBody>
                            {chunkArray(detailColumns as string[], detailColNum).map((chunk: string[], i) => (
                              <TableRow key={i}>
                                {chunk.map((additionalColumn: string) => (
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
              );
            })}
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
        />
      )}
    </Paper>
  </>
);

  };
export default withStreamlitConnection(TableComponent);
