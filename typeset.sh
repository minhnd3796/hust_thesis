mkdir build/
pdflatex -output-directory=build/ main.tex
cd build/
makeglossaries main
biber main
cd ..
pdflatex -output-directory=build/ main.tex
pdflatex -output-directory=build/ main.tex
mv build/main.pdf ../20146488_NguyenDucMinh.pdf
rm -r build/
