all: book.pdf

book.pdf:
	pandoc chapters/*.md --bibliography ref.bib -f markdown+citations --standalone --citeproc --toc -o $@

clean:
	rm -f *.epub *.pdf
