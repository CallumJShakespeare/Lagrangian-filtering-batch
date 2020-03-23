# Lagrangian-filtering-batch
A collection of bash and python scripts for batch submission of lagrangian filtering jobs on Gadi Cascade Lake Nodes

# qsub_multi 
is the template submission script to submit 200 zlevels and N times
(N=12 currently), over the requesite number of jobs.
Each job runs on 48 cores, and issues 48 python commands

#submit_all_levels 
will create the PBS submission scripts for each job

# sub_one_level.py
Each job calls multiple instances of the core filtering script sub_one_level.py

# run_concat_all
At the end of the filtering,  all output can be collate with run_concat_all
