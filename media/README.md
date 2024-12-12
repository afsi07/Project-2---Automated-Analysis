# Data Analysis Report - media

## Dataset Overview
The dataset contains 2652 rows and 8 columns. Columns include:

- *date*: object
- *language*: object
- *type*: object
- *title*: object
- *by*: object
- *overall*: int64
- *quality*: int64
- *repeatability*: int64

## Summary Statistics
|               |   count |   unique | top               |   freq |      mean |        std |   min |   25% |   50% |   75% |   max |
|:--------------|--------:|---------:|:------------------|-------:|----------:|-----------:|------:|------:|------:|------:|------:|
| date          |    2553 |     2055 | 21-May-06         |      8 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| language      |    2652 |       11 | English           |   1306 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| type          |    2652 |        8 | movie             |   2211 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| title         |    2652 |     2312 | Kanda Naal Mudhal |      9 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| by            |    2390 |     1528 | Kiefer Sutherland |     48 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| overall       |    2652 |      nan | nan               |    nan |   3.04751 |   0.76218  |     1 |     3 |     3 |     3 |     5 |
| quality       |    2652 |      nan | nan               |    nan |   3.20928 |   0.796743 |     1 |     3 |     3 |     4 |     5 |
| repeatability |    2652 |      nan | nan               |    nan |   1.49472 |   0.598289 |     1 |     1 |     1 |     2 |     3 |
## Missing Values
|               |   0 |
|:--------------|----:|
| date          |  99 |
| language      |   0 |
| type          |   0 |
| title         |   0 |
| by            | 262 |
| overall       |   0 |
| quality       |   0 |
| repeatability |   0 |
## Correlation Matrix
The correlation matrix of the dataset is visualized below:
![Correlation Matrix](media\correlation_matrix.png)

## Missing Values
A bar plot visualizing the number of missing values by column:
![Missing Values Bar Plot](media\missing_values_barplot.png)

## Outliers
The number of outliers detected in the dataset (Z-score > 3) per column is as follows:
|               |   0 |
|:--------------|----:|
| overall       |   0 |
| quality       |   0 |
| repeatability |   0 |