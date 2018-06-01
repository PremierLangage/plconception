
cat >all.md </dev/null
for i in *.md >>all.md
do
echo "<<<     "+ $i+"         >>>"
cat $i
echo
done


