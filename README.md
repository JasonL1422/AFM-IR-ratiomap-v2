# AFM-IR-ratiomap-v2
* This Mathematica script is to plot the ratio map of AFM-IR amplitude collected at different wavenumbers, which is not available in NanoScope software.
<img src="https://github.com/JasonL1422/AFM-IR-ratiomap-v2/blob/main/example.png" width="1200"/> </a>
* Difference from version 1 is:
  1. The input files are .txt files (not .csv). 
   - Each .txt file consists of number of values in one column.
   - The total number of values are nx (sample per line) x ny (number of line).
   - The first line of each .txt file is the value name. (i.e. Amplitude (V))
     
  2. Some user-friendly functions were added.
   - Defined 'IRmap[wvn,# of contour lines]'
   - Defined 'IRmap2[wvn,max,bin]'
     
  3. There are number of inputs that you need to manually type in. Explanations are in (*text*)

* Sample data and images are not allowed to be used public without permission.


