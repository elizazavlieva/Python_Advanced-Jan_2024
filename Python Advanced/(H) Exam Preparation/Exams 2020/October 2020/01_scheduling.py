

jobs = [int(el) for el in input().split(', ')]
searched_index = int(input())
total_clock_cycles = 0
index_found = False
jobs_copy = jobs.copy()
while jobs_copy:
    task = min(jobs_copy)

    counter = jobs_copy.count(task)
    indexes = []
    if counter > 1:
        indexes = [index for index, value in enumerate(jobs) if value == task]

        for job in indexes:
            total_clock_cycles += jobs[job]
            if job == searched_index:
                index_found = True
                break
            jobs_copy.remove(task)

    else:
        total_clock_cycles += task
        if jobs.index(task) == searched_index:
            index_found = True
        jobs_copy.remove(task)
    if index_found:
        print(total_clock_cycles)
        break
