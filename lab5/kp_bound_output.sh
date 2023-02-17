BOUNDS="5000 6000 7000 8000 9000 10000 11000 14000 15000 16000 17000 18000 19000 20000"

## initialise a folder which saves raw txt file
mkdir ./data/data3b/bound
mkdir ./data/time3b/bound
## clear and initialise csv and dat
rm ./data/time3b/bound/time_bound.csv
rm ./data/time3b/bound/time_bound.dat

touch ./data/time3b/bound/time_bound.csv
touch ./data/time3b/bound/time_bound.dat

for BOUND in $BOUNDS
do

## special cases may use this
# for COUNT in 1 2 3 4 5
# do

## number of items you want to put in the knapsack ｜ capacity of the knapsack ｜ upper bound on the profit and weight of each item ｜ name of the output file
    python3 kp_generate.py 300 10000 ${BOUND} ./data/data3b/bound/bound_${BOUND}.txt 

## record time
    ALL_TIME=`(time -p python3 ./python/dp_kp.py ./data/data3b/bound/bound_${BOUND}.txt) 2>&1 | grep -E "user|sys" | sed s/[a-z]//g`
    RUNTIME=0
    for i in $ALL_TIME;
    do RUNTIME=`echo $RUNTIME + $i|bc`;
    done
    echo $BOUND, $RUNTIME >> ./data/time3b/bound/time_bound.csv
    echo $BOUND $RUNTIME >> ./data/time3b/bound/time_bound.dat

# done 

done

# UNUSED
# This script is written by Rui Xu, Feb 2023.
# Two main functions: 
# 1.Use kp_generate.py to generate source data by a different bound for dp_kp.py 
# 2. record and save the execution time 