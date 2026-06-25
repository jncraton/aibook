all: dist

chapters = $(wildcard chapters/*.md)

pandocargs = --css style.css --extract-media=./media --request-header="User-Agent:pandoc/1.0 (jncraton@gmail.com)" --bibliography ref.bib --csl ieee.csl -f markdown+citations --lua-filter wp.lua --standalone --citeproc --toc --toc-depth=1

index.%: $(chapters) style.css chapters/media/phototropism.gif
	pandoc $(chapters) $(pandocargs) -o $@

dist: $(chapters) style.css chapters/media/phototropism.gif
	pandoc $(chapters) $(pandocargs) -t chunkedhtml -o $@
	cp style.css dist/style.css

spellcheck:
	for f in chapters/*.md; do aspell --home-dir=. --check --dont-backup "$$f"; done

clean:
	rm -f *.epub *.pdf *.html chapters/media/phototropism.gif
	rm -rf dist media
