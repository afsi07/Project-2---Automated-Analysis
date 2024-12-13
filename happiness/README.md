# Dataset Analysis

## Summary Statistics

|       |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
| count | 2228       |    2228       |           2228       |      2228        |                         2228       |                    2228        |  2228        |                 2228        |       2228        |      2228         |
| mean  | 2014.75    |       5.51673 |              9.42476 |         0.814925 |                           63.6223  |                       0.753292 |    -0.006656 |                    0.753851 |          0.65415  |         0.27073   |
| std   |    5.05565 |       1.07991 |              1.11405 |         0.111636 |                            6.28811 |                       0.131256 |     0.150479 |                    0.163192 |          0.102103 |         0.0816989 |
| min   | 2005       |       2.56    |              6.607   |         0.45     |                           43.96    |                       0.342    |    -0.34     |                    0.206    |          0.344    |         0.083     |
| 25%   | 2011       |       4.694   |              8.55875 |         0.751    |                           59.9     |                       0.668    |    -0.113    |                    0.703    |          0.575    |         0.21      |
| 50%   | 2015       |       5.481   |              9.516   |         0.837    |                           65.045   |                       0.769    |    -0.018    |                    0.7925   |          0.663    |         0.262     |
| 75%   | 2019       |       6.32125 |             10.3803  |         0.904    |                           68.3812  |                       0.85625  |     0.085    |                    0.865    |          0.736    |         0.323     |
| max   | 2023       |       8.019   |             11.676   |         0.985    |                           74.6     |                       0.985    |     0.474    |                    0.983    |          0.884    |         0.532     |


## Missing Values

|                                  |   0 |
|:---------------------------------|----:|
| Country name                     |   0 |
| year                             |   0 |
| Life Ladder                      |   0 |
| Log GDP per capita               |  28 |
| Social support                   |  13 |
| Healthy life expectancy at birth |  63 |
| Freedom to make life choices     |  36 |
| Generosity                       |  81 |
| Perceptions of corruption        | 125 |
| Positive affect                  |  24 |
| Negative affect                  |  16 |


## Correlation Matrix

|                                  |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:---------------------------------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
| year                             |  1         |     0.0414252 |            0.0690816 |       -0.0576127 |                          0.14479   |                       0.225251 |    0.0214748 |                   -0.074632 |         0.0106182 |         0.210467  |
| Life Ladder                      |  0.0414252 |     1         |            0.774487  |        0.704591  |                          0.720781  |                       0.513171 |    0.209112  |                   -0.43648  |         0.491588  |        -0.307532  |
| Log GDP per capita               |  0.0690816 |     0.774487  |            1         |        0.679238  |                          0.827032  |                       0.335495 |    0.0127042 |                   -0.337751 |         0.217547  |        -0.237718  |
| Social support                   | -0.0576127 |     0.704591  |            0.679238  |        1         |                          0.594342  |                       0.370288 |    0.0790819 |                   -0.225122 |         0.388698  |        -0.426929  |
| Healthy life expectancy at birth |  0.14479   |     0.720781  |            0.827032  |        0.594342  |                          1         |                       0.331835 |    0.0360008 |                   -0.287388 |         0.198472  |        -0.117886  |
| Freedom to make life choices     |  0.225251  |     0.513171  |            0.335495  |        0.370288  |                          0.331835  |                       1        |    0.340981  |                   -0.454094 |         0.552196  |        -0.227725  |
| Generosity                       |  0.0214748 |     0.209112  |            0.0127042 |        0.0790819 |                          0.0360008 |                       0.340981 |    1         |                   -0.292188 |         0.302215  |        -0.0754834 |
| Perceptions of corruption        | -0.074632  |    -0.43648   |           -0.337751  |       -0.225122  |                         -0.287388  |                      -0.454094 |   -0.292188  |                    1        |        -0.27825   |         0.240799  |
| Positive affect                  |  0.0106182 |     0.491588  |            0.217547  |        0.388698  |                          0.198472  |                       0.552196 |    0.302215  |                   -0.27825  |         1         |        -0.28052   |
| Negative affect                  |  0.210467  |    -0.307532  |           -0.237718  |       -0.426929  |                         -0.117886  |                      -0.227725 |   -0.0754834 |                    0.240799 |        -0.28052   |         1         |


## Key Insights

- **year:** Mean = 2014.75, Std Dev = 5.06, Skewness = -0.06, Kurtosis = -1.09
- **Life Ladder:** Mean = 5.52, Std Dev = 1.08, Skewness = -0.01, Kurtosis = -0.72
- **Log GDP per capita:** Mean = 9.42, Std Dev = 1.11, Skewness = -0.35, Kurtosis = -0.77
- **Social support:** Mean = 0.81, Std Dev = 0.11, Skewness = -0.90, Kurtosis = 0.18
- **Healthy life expectancy at birth:** Mean = 63.62, Std Dev = 6.29, Skewness = -0.72, Kurtosis = -0.23
- **Freedom to make life choices:** Mean = 0.75, Std Dev = 0.13, Skewness = -0.60, Kurtosis = -0.19
- **Generosity:** Mean = -0.01, Std Dev = 0.15, Skewness = 0.51, Kurtosis = -0.06
- **Perceptions of corruption:** Mean = 0.75, Std Dev = 0.16, Skewness = -1.37, Kurtosis = 1.55
- **Positive affect:** Mean = 0.65, Std Dev = 0.10, Skewness = -0.32, Kurtosis = -0.61
- **Negative affect:** Mean = 0.27, Std Dev = 0.08, Skewness = 0.48, Kurtosis = -0.12


## Visualizations

Refer to the generated PNG files for detailed visualizations, including distribution histograms and correlation heatmaps.