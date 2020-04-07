

rm all.md nrm_md readme.md

echo "Title: Concepts" >table.tutu
echo "Date: $(LANG=en date)" >>table.tutu
echo >>nrm_md

echo "Title: Glossaire " >all.tutu
echo "Date: $(LANG=en date)" >>all.tutu
echo >>all.tutu
#echo "\tableofcontents" >>all.tutu
#echo "\section{Glossaire}" >>all.tutu 
for i in *.md 
do
echo "<!-- $i -->" >>all.tutu
echo "<a id=\"$i\"></a>" >>all.tutu
echo >>all.tutu
cat $i| sed -e "s/^#/##/" -e "s/](/](glossaire.html#/"  >>all.tutu
echo "1. [$i](glossaire.html#$i)" >>table.tutu
echo >>all.tutu
done

mv table.tutu	index.md
mv all.tutu all.md




