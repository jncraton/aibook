all: book.epub

book.epub:
	pandoc chapters/*.md -o $@

clean:
	rm -f *.epub
