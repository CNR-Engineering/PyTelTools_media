# Compile twice to make explicitly index
%.pdf: %.tex
	pdflatex $< && pdflatex $<

all: mathematical_definitions.pdf equations.pdf

clean:
	find \( -name '*.aux' -o -name '*.idx' -o -name '*.ilg' -o -name '*.ind' -o -name '*.log' -o -name '*.toc' -o -name '*.out' \) -delete

mrproper: clean
	find -name '*.pdf' -delete

.PHONY: all clean
