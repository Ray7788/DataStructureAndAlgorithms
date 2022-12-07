STATES="random"
ASIZES="16673 33343 50003 66683 83339 100003 116681" 
SIZES="10000 20000 30000 40000 50000 60000 70000" 

IFS='', read -r -a ASIZES1 <<< "$ASIZES" 

rm data2/sorted_data_python.dat 
rm data2 reverse_data_python.dat 
rm data2/random_data_python.dat 

rm data2/sorted_data_python.csv 
rm data2/reverse_data_python.csv
rm data2/random_data_python.csv 

for STATE in $STATES 
do

for SIZE in $SIZES 
do

    if [ $SIZE == "10000" ]; then
        ts="${ASIZES1[0]}"
    elif [ $SIZE == "20000" ]; then
        ts="${ASIZES1[1]}"
    elif [ $SIZE == "30000" ]; then
        ts="${ASIZES1[2]}"
    elif [ $SIZE == "40000" ]; then
        ts="${ASIZES1[3]}"
    elif [ $SIZE == "50000"]; then
        ts="${ASIZES1[4]}"
    elif [ $SIZE == "60000" ]; then
        ts="${ASIZES1[5]}" 
    else
        ts="${ASIZESA[6]}" 
    fi
    #end of if

for COUNT in 1 2 3 4 5
do

    ALL_TIME=`(time -p python3 ../../python/speller_darray.py -d ../data2/dict_${SIZE}_${STATE}_$COUNT -m 1 -s ${SIZE} ../dictionaries_and_queries/query_${SIZE}_${STATE}_$COUNT) 2>&1 | grep -E "user|sys" | sed s/[a-z]//g`

    RUNTIME=`echo ${ALL_TIME[1]} + ${ALL_TIME[2]} | bc`
    COLL=`echo ${ALL_TIME[O]}`

echo $SIZE $RUNTIME, $COLL >> data/${STATE}_data2_python.dat 
echo $SIZE, $RUNTIME, $COLL >> data/${STATE}_data2_python.csv 

done 

done 

done