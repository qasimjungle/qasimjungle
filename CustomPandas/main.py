
# This program is practice of the pandas module
import pandas as pd
import matplotlib.pyplot as plt

from CustomPandas.common.utils import ask_to_exit_or_continue, take_user_input
from CustomPandas.modules.Correlation import finding_correlation
from CustomPandas.modules.GraphPlotting import graph_plotting_file_csv_data, graph_plotting_file_json_data, file_column_graph, file_column_graph_scatter, file_column_histogram, file_column_pie_chart
from CustomPandas.modules.CSVdataModifying import reading_csv_file, Removing_File_Row, filling_empty_row, mean_mode_median, remove_duplicate_row, add_something_empty_cell
from CustomPandas.modules.JsonPythonDictionary import read_jason_file, python_dictionary_json, access_rows_from_start, access_rows_from_end, file_information
from CustomPandas.modules.LoadingCsvFile import loading_file, maximum_row_file, change_row_file
from CustomPandas.modules.PandaSeries import pandas_series_mode, access_item
from CustomPandas.modules.DataFrame import access_row, dataframe_demo

USER_INPUT_STRING = [
    "\033[95m Select valid Input",
    '\033[0;31m \tA.Enter the for pandas series',
    '\033[0;32m \tB.Dataframe Demo respectively:',
    '\033[0;31m \tC.Load a File',
    '\033[0;34m \tD.Read a json file and demo of python dictionary reading like json',
    '\033[0;35m \tE. REMOVING EMPTY CELL,DELETING  DUPLICATE,REMOVING WORG DATA,mean median mode',
    '\033[0;31m \tF.correlation of pandas file with .csv extension',
    '\033[0;32m \tG.Plot Graph of the data of the file',
]
message = "Just Enter the Option Alphabet of the Above Operation"


SYSTEM_MODES = {
    'a': pandas_series_mode,
    'b': dataframe_demo,
    'c': loading_file,
    'd': read_jason_file,
    'e': reading_csv_file,
    'f': finding_correlation,
    'g': graph_plotting_file_csv_data
}

if __name__ == "__main__":

    keep_running = True

    while keep_running:
        user_input = take_user_input(
            "\n".join(USER_INPUT_STRING),
            strict_validation=True,
            validation_rules=SYSTEM_MODES.keys()
        )

        SYSTEM_MODES[user_input]()
        keep_running = ask_to_exit_or_continue()

