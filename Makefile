COMPILER = pdflatex
CFLAGS = -halt-on-error
OBJECTS = Intro.tex

# ultimate target:
talk: $(OBJECTS)
	$(COMPILER) $(CFLAGS) talk.tex
	evince talk.pdf&

bib: $
	bibtex talk
	
# other targets:

# Dependencies;
talk.pdf: Intro.tex

# clean up rule

clean:
	rm -f *.aux *.log *.out *.snm *.toc *.nav
