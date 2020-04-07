

rm all.md nrm_md readme.md

echo "## Activity " >>all.tutu
for j in standard types plugapps 
do
echo "### **$j**" >>all.tutu 
cat $j/readme.md >>all.tutu
for i in $j/*.md
do
if test $i == $j/readme.md
then
echo $i
else
echo "<!-- $j $i -->" >>all.tutu
echo "<a id=\"$i\"></a>" >>all.tutu
echo >>all.tutu
cat $i| sed -e "s/^#/###/"  >>all.tutu
echo >>all.tutu
fi
done
done

mv all.tutu all.md
