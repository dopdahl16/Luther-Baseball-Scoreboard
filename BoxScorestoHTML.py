# Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved. 
# Permission to copy and modify is granted under the GNU General Public License v3.0 license
# Last revised 8/26/2019

import os

for box_score in os.listdir("\\path\\to\\LCBoxScores"):
    print(box_score)
    os.rename("\\path\\to\\LCBoxScores\\"+box_score, "\\path\\to\\LCBoxScores\\"+box_score+".html")
    