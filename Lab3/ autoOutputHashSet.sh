STATES="sorted reverse random"
SIZES="100000 200000 300000 400000 500000 600000 700000"

# rm data/sorted_data_python.dat
# rm data/reverse_data_python.dat
# rm data/none_data_python.dat
# rm data/sorted_data_python.csv
# rm data/reverse_data_python.csv
# rm data/none_data_python.csv

for STATE in $STATES
do

for SIZE in $SIZES
do

for COUNT in 1 2 3 4 5
do

    # Debugging statement to check program calls working as expected
    # python3 ../../search_and_sort_lab/python/speller_darray.py -d ../dictionaries_and_queries/dict_${SIZE}_${STATE}_$COUNT -m 1 -s ${SIZE} ../dictionaries_and_queries/query_${SIZE}_${STATE}_$COUNT

    ALL_TIME=`(time -p python3 ./python/speller_hashset.py -d ./test_data/test_dict/dict_${SIZE}_${STATE}_$COUNT -s ${SIZE} -m 0 ./test_data/test_query/query_${SIZE}_${STATE}_$COUNT) 2>&1 | grep -E "user|sys" | sed s/[a-z]//g`
    
    RUNTIME=0
    for i in $ALL_TIME;
    do RUNTIME=`echo $RUNTIME + $i|bc`;
    done
    echo $SIZE $RUNTIME >> data_output/hashset_output/${STATE}_hashset_data_output_python.dat
    echo $SIZE, $RUNTIME >> data_output/hashset_output/${STATE}_hashset_data_output_python.csv
    
done

done

done
