# AFM-IR-ratiomap-v2
* This Mathematica code is to plot ratio maps of the AFM-IR amplitude maps collected at different wavenumbers, which is not available in NanoScope software. [Contact: jongcheol1422@gmail.com]
  
<img src="https://github.com/JasonL1422/AFM-IR-ratiomap-v2/blob/main/v2.1_uploaded/v2.1_example22.png" width="1200"/> </a>

* Difference from version 1 is:
  1. The input files are .txt files (not .csv). 
   - Each .txt file consists of number of values in one column.
   - The total number of values are nx (sample per line) x ny (number of line).
   - The first line of each .txt file is the value name. (i.e. Amplitude (V))
     
  2. Some user-friendly functions were added.
   - Defined 'IRmap[wvn,# of contour lines]'
   - Defined 'IRmap2[wvn,min,max,bin].' The color scheme/range/bin are automatically reset (v2.1)
     
  3. There are number of inputs that you need to manually enter. Explanations were added next to each functions,definitions,etc. in (*text*)
     
  4. [important] Make sure that you check the file names imported, and properly assign them to proper names in order. Otherwise, you will end up with wrong/weird results! (v2.1)

* Sample data and images are not allowed to be used public without permission.
* v2.1 explanation added. 2024.07.04


