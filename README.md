# CORNELLSASLAB
SAS output to EXCEL converter for Cornell/MIT Language and acquisition lab


Instructions:

This python code can be used to convert SAS outputs from the lang and ac lab into data tables for regression and factorial summaries. SAS formst varies by run, therefore you may have to do a little editing before the code works.

For example, a working data chunk for this program would look something like this:


                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    1         2     1   8          1      1     -0.4167    0.1251   1544    -3.33    0.0009
    1         2     1   8          1      2     -0.2917    0.1251   1544    -2.33    0.0199
    1         2     2   7          2      3     -0.4375    0.1363   1544    -3.21    0.0014
    1         2     2   8          1      1     -0.4583    0.1251   1544    -3.66    0.0003
                                        The SAS System         15:01 Sunday, August 4, 2019 139

                                     The GLIMMIX Procedure

                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    1         2     2   8          1      2     -0.3333    0.1251   1544    -2.66    0.0078
    1         2     2   8          1      3     -0.5625    0.1251   1544    -4.50    <.0001
    1         2     2   8          2      1     -0.5833    0.1363   1544    -4.28    <.0001
    1         2     3   7          2      3     -0.4167    0.1363   1544    -3.06    0.0023
    1         2     3   8          1      1     -0.4375    0.1251   1544    -3.50    0.0005
    1         2     3   8          1      2     -0.3125    0.1251   1544    -2.50    0.0126
    1         2     3   8          1      3     -0.5417    0.1251   1544    -4.33    <.0001
                                        The SAS System         15:01 Sunday, August 4, 2019 140

                                     The GLIMMIX Procedure

                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    1         2     3   8          2      1     -0.5625    0.1363   1544    -4.13    <.0001
    1         2     3   8          2      2     -0.5208    0.1363   1544    -3.82    0.0001
    1         2     3   8          2      3     -0.4583    0.1363   1544    -3.36    0.0008
    2         1     1   2          1      2    6.66E-16   0.07654   1544     0.00    1.0000
    2         1     1   2          1      3    -0.08333   0.07654   1544    -1.09    0.2764
    2         1     1   8          2      1     -0.4583    0.1251   1544    -3.66    0.0003
    2         1     1   8          2      2     -0.4167    0.1251   1544    -3.33    0.0009
    2         1     1   8          2      3     -0.3542    0.1251   1544    -2.83    0.0047
                                        The SAS System         15:01 Sunday, August 4, 2019 141


As you can see, every chunk starts with the same title, and ends with a date and page number in the bottom right corner. All of the chunks have the same format and same number of columns. If the format of the pasted chunks is wrong, the code likely won't work.


NOTE: when pasting the file path to your excel document, make sure excel is not running on your computer, or else there will be an error.
