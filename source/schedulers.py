import math
from des import SchedulerDES
from event import Event, EventTypes
from process import Process, ProcessStates

class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        #Return current process without prioritization
        return self.processes[cur_event.process_id]
                
    def dispatcher_func(self, cur_process):
        #Run process for its entire service time
        run_time = cur_process.run_for(cur_process.service_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        #Return an event indicating the process has completed
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=run_time+self.time)

class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        #Select process with the minimum service time from the list of ready processes
        cur_event = [p for p in self.processes if p.process_state == ProcessStates.READY]
        min_process = min(cur_event, key=lambda p: p.service_time)
        return min_process

    def dispatcher_func(self, cur_process):
        #Run process for its entire service time
        run_time = cur_process.run_for(cur_process.service_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        #Return an event indicating the process has completed
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=run_time + self.time)

class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        #Return the current process without prioritization
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        #Run the process for the quantum or if remaining time is shorter
        run_time = min(self.quantum, cur_process.remaining_time)
        cur_process.run_for(run_time, self.time)

        if cur_process.remaining_time == 0:
            # If process is completed, mark as TERMINATED and return an event
            cur_process.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time + run_time)
        else:
            # If process is not completed, mark as READY for the next round
            cur_process.process_state = ProcessStates.READY
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=self.time + run_time)

class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        #Select process with the minimum remaining time from the list of ready processes
        cur_event = [p for p in self.processes if p.process_state == ProcessStates.READY]
        return min(cur_event, key=lambda p: p.remaining_time)

    def dispatcher_func(self, cur_process):
        #Run process for the remaining time or until the next event, whichever is shorter
        if self.next_event_time() == math.inf:
            run_time = cur_process.run_for(self.quantum, self.time)
        else:
            run_time = cur_process.run_for(self.next_event_time() - self.time, self.time)
        if cur_process.remaining_time == 0:
            #If process is completed, mark as TERMINATED and return an event
            cur_process.process_state = ProcessStates.TERMINATED
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=run_time + self.time)
        else:
            #If process is not completed, mark as READY for the next round
            cur_process.process_state = ProcessStates.READY
            return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_REQ, event_time=run_time + self.time)
