for ((i = 0 ; i < 10 ; i++)); do
    taskset -c 0-1 ./smartgrid_run.sh;
done
