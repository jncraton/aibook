all: dist

chapters = $(wildcard chapters/*.md)

pandocargs = --css style.css --extract-media=./media --request-header="User-Agent:pandoc/1.0 (jncraton@gmail.com)" --bibliography ref.bib --csl ieee.csl -f markdown+citations --lua-filter wp.lua --standalone --citeproc --toc --toc-depth=1

index.%: $(chapters) style.css chapters/media/phototropism.gif
	pandoc $(chapters) $(pandocargs) -o $@

dist: $(chapters) style.css chapters/media/phototropism.gif
	pandoc $(chapters) $(pandocargs) -t chunkedhtml -o $@
	cp style.css dist/style.css

chapters/media/phototropism.gif:
	ffmpeg -i https://upload.wikimedia.org/wikipedia/commons/a/aa/Phototropism_in_Solanum_lycopersicum.webm -filter_complex "[0:v]select='not(mod(n,2))*gte(n,240)',setpts=0.5*N/FRAME_RATE/TB,normalize,crop=0.8*iw:0.8*ih:iw-ow:ih-oh[forward];[0:v]select='not(mod(n,2))*gte(n,240)',setpts=0.5*N/FRAME_RATE/TB,reverse,normalize,crop=0.8*iw:0.8*ih:iw-ow:ih-oh[backward];[forward][backward]concat=n=2:v=1:a=0,split[tpl_a][tpl_b];[tpl_a]palettegen[palette];[tpl_b][palette]paletteuse" -pix_fmt yuv444p -f yuv4mpegpipe - | gifski --quality=50 --fps 12 --motion-quality=50 --lossy-quality=50 --output $@ -

spellcheck:
	for f in chapters/*.md; do aspell --home-dir=. --check --dont-backup "$$f"; done

clean:
	rm -f *.epub *.pdf *.html chapters/media/phototropism.gif
	rm -rf dist media
