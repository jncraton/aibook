all: book.pdf

book.pdf:
	pandoc chapters/*.md -f gfm --standalone --toc -o $@

clean:
	rm -f *.epub *.pdf
