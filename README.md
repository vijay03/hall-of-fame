# Academic Hall of Fame

These scripts allow you to create a Hall of Fame similar to the [SOSP/OSDI Hall of Fame](http://www.cs.utexas.edu/~vijay/hall.html)
and the [FAST Hall of Fame](cs.utexas.edu/~vijay/fast.html).

The scripts require publication information, and author information. The publication information is pulled 
from [DBLP](dblp.uni-trier.de/) via their XML API. The author information is obtained with permission from 
Prof. Emery Berger's [CSRankings](http://csrankings.org).

## Scripts ##

`getauthors.py` creates `authors.data` based on `faculty-affiliations.csv`.

`getdata.py` obtains publication data from DBLP and stores it in `sosp.data`, `osdi.data`, and `total.data`.

`analyze-markdown.py` creates a Markdown file for the Hall of Fame. You must then use `showdown` to convert it to HTML.

`analyze-latest.py` creates a Hall of Fame that excludes authors who have not published in the last five years.

`make` does all of this (except getting the `faculty-affiliations.csv`) automatically for you,
and opens the final `top.html` for you to see the Hall of Fame.

## Contact ##

Contact me at `vijay@cs.utexas.edu` for any questions. Drop me a note if you are using a version of these scripts! 
