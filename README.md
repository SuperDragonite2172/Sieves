# Sieves
Prime sieves in various languages as programming practice

## Stats of the Sieves
Number of Passes (Average over 10 runs of 10 seconds)
-
|Limit      |SievePyV0|SievePyV1   |
|-----------|---------|------------|
|10         |875,055.4|   3,203,360|
|100        |  8,626.7|   883,921.4|
|1000       |       77|     83735.6|
|10000      |       1*|      7094.9|
|100000     |        -|       658.4|
|**1000000**|    **-**|    **54.2**|
|10000000   |        -|        4.9*|
|100000000  |        -|         -|

Passes per second (Average over 10 runs)
-
|Limit      |SievePyV0   |SievePyV1    |
|-----------|------------|-------------|
|10         |87,505.47634|314,935.95157|
|100        |   862.62024| 88,392.08608|
|1000       |     7.65741|   8373.52483|
|10000      |     0.07426|    709.41650|
|100000     |           -|     65.77512|
|**1000000**|       **-**|  **5.37658**|
|10000000   |           -|      0.43602|
|100000000  |           -|            -|

\*Time taken to finish the last pass was greater than 10 seconds

\-Not patient enough to test