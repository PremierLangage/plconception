

rm all.md nrm.md readme.md

echo "\tableofcontents" >>all.tutu
echo "\section{Glossaire}" >>all.tutu 
for i in *.md 
do
echo "<!-- $i -->" >>all.tutu
cat $i| sed -e "s/^#/##/" >>all.tutu
echo "1. [$i]($i)" >>nrm.md
done

mv nrm.md readme.md 
mv all.tutu all.md
pandoc -V geometry:margin=1.5cm all.md -o all.pdf

git commit -m "refection readme" readme.md 



