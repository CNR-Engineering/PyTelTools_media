FILENAME=TUC2017_PyTelTools_Duron_Wang_CNR

all: ${FILENAME}.pdf

${FILENAME}.pdf: ${FILENAME}.tex
	pdflatex -shell-escape $< && bibtex ${FILENAME} && pdflatex -shell-escape $<

clean:
	rm -f ${FILENAME}.{aux,log,nav,out,snm,toc,bbl,blg}
	rm -f texput.log log
	rm -f -r _minted*

.PHONY: all clean animations
