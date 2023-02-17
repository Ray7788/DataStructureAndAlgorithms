CAPACITYS="10000 20000 30000 40000 50000 60000 70000 80000 90000 100000 110000 120000 130000 140000 150000 160000 170000 180000 190000 200000"

## initialise a folder which saves raw txt file
mkdir ./data/data3b/capacity
mkdir ./data/time3b/capacity
## clear and initialise csv and dat
rm ./data/time3b/capacity/time_capacity.csv
rm ./data/time3b/capacity/time_capacity.dat

touch ./data/time3b/capacity/time_capacity.csv
touch ./data/time3b/capacity/time_capacity.dat

for CAPACITY in $CAPACITYS
do

## special cases may use this
# for COUNT in 1 2 3 4 5
# do

## number of items you want to put in the knapsack ｜ capacity of the knapsack ｜ upper bound on the profit and weight of each item ｜ name of the output file
    python3 kp_generate.py 300 ${CAPACITY} 5000 ./data/data3b/capacity/capacity_${CAPACITY}.txt 

## record time
    ALL_TIME=`(time -p python3 ./python/dp_kp.py ./data/data3b/capacity/capacity_${CAPACITY}.txt) 2>&1 | grep -E "user|sys" | sed s/[a-z]//g`
    RUNTIME=0
    for i in $ALL_TIME;
    do RUNTIME=`echo $RUNTIME + $i|bc`;
    done
    echo $CAPACITY, $RUNTIME >> ./data/time3b/capacity/time_capacity.csv
    echo $CAPACITY $RUNTIME >> ./data/time3b/capacity/time_capacity.dat

# done 

done


# This script is written by Rui Xu, Feb 2023.
# Two main functions: 
# 1.Use kp_generate.py to generate source data by a different capacity for dp_kp.py 
# 2. record and save the execution time 