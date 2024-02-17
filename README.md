# first_scheduling_algorithms
Networks and Operating Systems Essentials 2, 2nd Semester Assessed Exercise 2

Implements and showcases the following scheduling algorithms based on events, waiting queues, processes, process scheduling and dispatching:
1. First Come First Served
2. Shortest Job First
3. Round Robin
4. Shortest Remaining Time First

As well as including a report discussing the the scheduling algorithms.

APPENDIX - The Discrete Event Simulator
In the simple discrete event simulator, we have
three types of events:
• PROC_ ARRIVES: A new process arrives in the system.
• PROC_CPU_REQ: An existing process requests access to the CPU.
• PROC_CPU_DONE: A process has run its course and, thus, terminates.
Similarly, simulated processes can be in one of the following states:
• NEW: A new process arrives in the system at some point.
• READY: A process is waiting for the CPU to be allocated; note that this can be
a new process that just arrived, an older process that was never scheduled, or
an older process that was preempted.
• RUNNING: A process currently executes on the CPU.
• TERMINATED: A process has run its service time and, thus, terminates.
Initially, the simulator creates a list of processes to be simulated. Each process has the
following attributes:
• Process ID: A number uniquely identifying the process in the system. As all
processes are added to a table (aka the process table), their ID is simply the
table index for the cell at which their info is stored, starting from 0.
• Arrival time: The time of arrival of the process.
• State: The state in which the process currently is, as discussed above.
• Service time: The total amount of CPU burst time required by the process.
• Remaining time: The remaining CPU burst time for the process.
Each process keeps track of its execution time and offers a set of utility functions:
• A function that returns its departure time, after the process has terminated.
• A function that computes and returns its total waiting time.
• A function that computes and returns its turnaround time.
• A function that executes the process for up to a specified amount of time.
