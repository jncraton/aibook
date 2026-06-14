all: book.epub

book.epub:
	pandoc chapters/*.md --toc -o $@

clean:
	rm -f *.epub
