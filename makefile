all: index.html

index.%: chapters/media/phototropism.gif
	pandoc chapters/*.md --bibliography ref.bib --csl ieee.csl -f markdown+citations --lua-filter wp.lua --standalone --citeproc --toc -o $@

chapters/media/phototropism.gif:
	ffmpeg -i https://upload.wikimedia.org/wikipedia/commons/a/aa/Phototropism_in_Solanum_lycopersicum.webm -filter_complex "[0:v]select='not(mod(n,4))',setpts=0.15*PTS[forward];[0:v]select='not(mod(n,4))',setpts=0.15*PTS,reverse[backward];[forward][backward]concat=n=2:v=1:a=0,split[tpl_a][tpl_b];[tpl_a]palettegen[palette];[tpl_b][palette]paletteuse" $@.tmp.gif
	gifski --quality=25 --fps 12 --motion-quality=25 --lossy-quality=25 $@.tmp.gif --output $@

clean:
	rm -f *.epub *.pdf *.html chapters/media/*.gif
