from basic_data_structures import *

def binary_search(arr, val):
    end = len(arr) - 1
    start = 0
    while end >= start:
        mid = (end + start) // 2
        if arr[mid] > val:
            end = mid - 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            return mid

    return -1

def partition(arr, start, end):
    pivot = start
    start += 1
    while end >= start:
        if arr[start] < arr[pivot]:
            start += 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1

    arr[end], arr[pivot] = arr[pivot], arr[end]
    return end

def quicksort(arr, start, end):
    if end > start:
        i = partition(arr, start, end)
        quicksort(arr, start, i - 1)
        quicksort(arr, i + 1, end)

def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    res = np.empty(n + m)
    j = 0
    k = 0
    for i in range(n + m):
        if j < n and k < m:
            if arr1[j] < arr2[k]:
                res[i] = arr1[j]
                j += 1
            else:
                res[i] = arr2[k]
                k += 1
        elif j < n:
            res[i] = arr1[j]
            j += 1
        else:
            res[i] = arr2[k]
            k += 1

    return res

def graph_bfs(g, s):
    g_visited = g.copy()
    for key, value in g_visited.items():
        g_visited[key] = False

    q = Queue()
    q.enqueue(s)
    g_visited[s] = True
    while not q.is_empty():
        v = q.dequeue()
        print(v)
        for u in g[v]:
            if not g_visited[u]:
                q.enqueue(u)
                g_visited[u] = True

def graph_dfs(g, g_visited, s):
    print(s)
    g_visited[s] = True
    for v in g[s]:
        if not g_visited[v]:
            graph_dfs(g, g_visited, v)
