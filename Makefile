all: authors.data sosp.data osdi.data
	python analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html --tables
	cat top.html | ssh  vijay@gilligan.cs.utexas.edu 'cat - > ~/public_html/hall.html; chmod 777 ~/public_html/hall.html'
	open top.html

local: authors.data sosp.data osdi.data
	python analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html --tables
	open top.html

active: authors.data
	python analyze-latest.py > top-active.md
	showdown makehtml -i top-active.md -o top-active.html --tables
	cat top-active.html | ssh  vijay@gilligan.cs.utexas.edu 'cat - > ~/public_html/hall-active.html; chmod 777 ~/public_html/hall-active.html'
	open top-active.html

authors.data:
	python getauthors.py

sosp.data:
	python getdata.py

osdi.data:
	python getdata.py

clean:
	rm *.data *.html *.md
