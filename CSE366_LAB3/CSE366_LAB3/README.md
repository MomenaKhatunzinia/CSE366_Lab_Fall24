In agent.py two mathod used.
Methods to:
Assign classes to the student based on availability.
Clear the schedule for new generations.

IN environment.py i have used fitness,selection,crossover & mutate function. Fitness function calculate the Fitness = Conflict Penalty + Preference Penalty.
IN selection between sorted fitness max half taken. In crossover 
- Select a random point in the parent schedules.
– Combine the genes (class assignments) of both parents up to the crossover
point.

In mutation Randomly select a class and reassign it to a new student.
Gene[i] = Random Student ID

IN run.py environment function call. population = next_generation will take after that current_best & current_fitness selected. Print best fitness and generation
