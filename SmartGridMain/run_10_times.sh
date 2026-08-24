for ((i = 0 ; i < 10 ; i++)); do
    taskset -c 4-5 ./smartgrid_run.sh;
done
