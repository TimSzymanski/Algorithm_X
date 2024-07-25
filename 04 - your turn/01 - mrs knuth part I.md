# Time to Finish Mrs. Knuth - Part I

You have everything you need to finish Mrs. Knuth's first puzzle and get her through the summer. Again, that puzzle can be found here:

[Codingame](https://www.codingame.com/home)

Here's a little pseudocode to help you finish up the first puzzle:

```text
copy all the AlgorithmX code

define MrsKnuthPartISolver as a subclass of AlgorithmXSolver
    override the constructor to build your requirements and actions from
    the passed in techer_availability and students

read all input
organize input
    teacher_availability
    students

create an instance of your new MrsKnuthPartISolver class, passing teacher_availability and students to the constructor

for each solution in solver.solve()
    for each action in solution
        add the student/instrument to schedule at hour/day

print the schedule
```

If you run into trouble, review the previous sections and I think you will find everythig you need. Now that Mrs. Knuth is ready to go, let's look at a few other puzzles you are already fully prepared to solve!