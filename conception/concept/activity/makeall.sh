

rm all.md nrm_md readme.md

echo "## Activity " >>all.tutu
for i in *.md 
do
echo "<!-- $i -->" >>all.tutu
echo "<a id=\"$i\"></a>" >>all.tutu
echo >>all.tutu
cat $i| sed -e "s/^#/###/"  >>all.tutu
echo >>all.tutu
done

mv all.tutu all.md
