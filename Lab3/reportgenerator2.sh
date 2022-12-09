STATES="random sorted reverse"
SIZES="100000 200000 300000 400000 500000"

rm data_output2/sorted_data_output_python.dat
rm data_output2/reverse_data_output_python.dat
rm data_output2/sorted_data_output_python.csv
rm data_output2/reverse_data_output_python.csv
rm data_output2/random_data_output_python.dat
rm data_output2/random_data_output_python.csv 

for STATE in $STATES
do

for SIZE in $SIZES
do

for COUNT in 1 2 3 4 5
do

    # Debugging statement to check program calls working as expected
    # python3 ../../search_and_sort_lab/python/speller_darray.py -d ../dictionaries_and_queries/dict_${SIZE}_${STATE}_$COUNT -m 1 -s ${SIZE} ../dictionaries_and_queries/query_${SIZE}_${STATE}_$COUNT

    ALL_TIME=`(time -p python3 ./python/speller_bstree.py -d ./test_data/test_dict/dict_${SIZE}_${STATE}_$COUNT -s ${SIZE} -m 0 ./test_data/test_query/query_${SIZE}_${STATE}_$COUNT) 2>&1 | grep -E "user|sys" | sed s/[a-z]//g`
    
    RUNTIME=0
    for i in $ALL_TIME;
    do RUNTIME=`echo $RUNTIME + $i|bc`;
    done
    echo $SIZE $RUNTIME >> data_output2/${STATE}_data_output_python.dat
    echo $SIZE, $RUNTIME >> data_output2/${STATE}_data_output_python.csv
    
done

done

done
