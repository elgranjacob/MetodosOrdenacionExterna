my_list = [-1, -5, -40, 100, 589, 27, -95]
 
def merge_runs(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
 
def natural_merge_sort(my_list):
    if len(my_list) <= 1: 
        return my_list
    print(f"Original list: {my_list}")
    
    runs = []
    start = 0
    end = 1
    while end < len(my_list):        
        if my_list[end] < my_list[end-1]:
            runs.append(my_list[start:end])
            start = end
        end += 1
    runs.append(my_list[start:end])
    
    print(f"Initial runs: {runs}")
    
    iteration = 1
    while len(runs) > 1: 
        print(f"\nIteration {iteration}:")
        merged_runs = []
        i = 0
        while i < len(runs) - 1:
            merged = merge_runs(runs[i], runs[i+1])
            print(f" Merging {runs[i]} and {runs[i+1]} -> {merged}")
            merged_runs.append(merged)
            i += 2
        if len(runs) % 2 == 1:
            merged_runs.append(runs[-1])
            print(f" Remaining run: {runs[-1]}")
        runs = merged_runs
        iteration += 1
        print(f" Runs after iteration {iteration - 1}: {runs}")
    
    return runs[0]
 
print("\nSorted list:")
print(natural_merge_sort(my_list))
