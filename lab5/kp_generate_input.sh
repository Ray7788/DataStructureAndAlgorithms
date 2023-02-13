CAPACITYS="5 6 7 8 9"
BOUNDS="5 6 7 8 9"

for CAPACITY in $CAPACITYS
do

for BOUND in $BOUNDS
do
echo $BOUND

for COUNT in 1 2 3 4 5
do

# number of items you want to put in the knapsack ｜ capacity of the knapsack ｜ upper bound on the profit and weight of each item ｜ name of the output file
    python3 kp_generate.py 5 ${CAPACITY} ${BOUND} ./data/data3b/${CAPACITY}_${BOUND}.txt 
    time (python3 ./python/dp_kp.py ./data/data3b/${CAPACITY}_${BOUND}.txt) 2>&1 | awk '/total/ {print strftime("%Y-%m-%d %H:%M:%S"), $1}' >> time.csv

done 

done 

done

    # python3 ./python/dp_kp.py "./data3b/6_7.txt" 
    # python3 kp_generate.py 5 6 7 ./data/data3b/te.txt 
    # query_${CAPACITY}_${BOUND}_$COUNT
    # ./data/data3b/${CAPACITY}_${BOUND}.txt 
