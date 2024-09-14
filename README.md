# IDS706_pandas_description_hw2
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/CICD.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/format.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/lint.yml/badge.svg)
![CI](https://github.com/nogibjj/IDS706_pandas_description_hw2/actions/workflows/test.yml/badge.svg)

## Requirements
* Python script using Polars for descriptive statistics
* Read a dataset (CSV or Excel)
* Generate summary statistics (mean, median, standard deviation)
* Create at least one data visualization

## Brief Introduction

### Dataset
<img src="https://seeklogo.com/images/N/nba-logo-59F0731E03-seeklogo.com.png" alt="NBA logo" width="400" />

#### [`NBA_2021.csv`](NBA_2021.csv)
This is the NBA 2021 global statistics table, which includes data for every player, such as PT (points), BL (blocks), and AT (assists).

### Python Scripts

In [`src/main.py`](src/main.py), This main.py script is used to read data from a CSV file, perform statistical analysis, and generate a data report. The script will generate three images and a PDF report. The three images are histograms showing the distribution of points, assists, and blocks for all players. Additionally, a PDF file with the report will be generated [here](NBA_2021_Report.pdf).

#### points histogram

![pts_histogram.png](pts_histogram.png)

#### assists histogram

![ast_histogram.png](ast_histogram.png)

#### blocks histogram

![blk_histogram.png](blk_histogram.png)

### Tests

There are three kinds of tests in this project.

* [test_lib.py]("src/test_lib.py"): this script is used to test functions in lib.py which contains functions shared by [`main.py`]("src/main.py") and [`python_ds_project_1.ipynb`]("python_ds_project_1.ipynb")

* [test_main.py]("src/test_main.py"): this script is used to test main if it successfully generate three figures and one PDF report.

* [test_notebook.py]("src/test_notebook.py"): this script is used to test if the output of jupyter notebook is the same as the saved output.
