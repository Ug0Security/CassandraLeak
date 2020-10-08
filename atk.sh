# ferme la vlad xD
cat "iplist" | while read line
do
echo $line
torify timeout 15 python -W ignore meh.py $line 
done
