# CORNELLSASLAB
SAS output to EXCEL converter for Cornell/MIT Language and acquisition lab


Instructions:

This python code can be used to convert SAS outputs from the lang and ac lab into data tables for regression and factorial summaries. SAS formst varies by run, therefore you may have to do a little editing before the code works.

For example, a working data chunk for this program would look something like this:


                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
                                        The SAS System         15:01 Sunday, August 4, 2019 139

                                     The GLIMMIX Procedure

                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
                                        The SAS System         15:01 Sunday, August 4, 2019 140

                                     The GLIMMIX Procedure

                      Differences of CHILDAGE*TASK*TR Least Squares Means
 
                                                         Standard
    CHILDAGE  TASK  TR  _CHILDAGE  _TASK  _TR  Estimate     Error     DF  t Value  Pr > |t|

    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
    X         X     X   X          X      X      X.XXXX    X.XXXX   XXXX     X.XX    0.XXXX
                                        The SAS System         15:01 Sunday, August 4, 2019 141


As you can see, every chunk starts with the same title, and ends with a date and page number in the bottom right corner. All of the chunks have the same format and same number of columns. If the format of the pasted chunks is wrong, the code likely won't work.


NOTE: when pasting the file path to your excel document, make sure excel is not running on your computer, or else there will be an error.
