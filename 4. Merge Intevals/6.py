class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

def find_max_cpu_load(jobs):

    jobs.sort(key = lambda x: x.start)

    max_load = jobs[0].cpu_load
    merged = [jobs[0]]

    for j in jobs[1:]:
        
        cur = merged[-1]
        if j.start <= cur.end:
            merged.pop()
            merged.append(job(min(cur.start, j.start), max(cur.end, j.end), cur.cpu_load + j.cpu_load))
            max_load = max(max_load, cur.cpu_load + j.cpu_load)
        else:
            max_load = max(max_load, j.cpu_load)

    return max_load
    




def main():
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
