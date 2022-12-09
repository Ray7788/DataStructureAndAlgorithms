STATES="random sorted reverse"
SIZES="100000 200000 300000 400000 500000"

for STATE in $STATES
do

for SIZE in $SIZES
do

echo $SIZE

for COUNT in 1 2 3 4 5
do

    python3 generate.py random ./test_data/test_dict/dict_${SIZE}_${STATE}_$COUNT ./test_data/test_query/query_${SIZE}_${STATE}_$COUNT $SIZE 0 $STATE 0

done 

done 

done