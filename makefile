all: book.pdf

book.pdf:
	pandoc chapters/*.md --bibliography ref.bib --csl ieee.csl -f markdown+citations --lua-filter wp.lua --standalone --citeproc --toc -o $@

clean:
	rm -f *.epub *.pdf
