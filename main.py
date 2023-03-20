#Ēriks Lijurovs 221RDB041 16. grupa
# python3

def parallel_processing(n, m, data):
    output = []

    thread_sums = []
    for l in range(n):
        thread_sums.append(0)
    index = 0
    counter = 0

    for i in range(m):
        if counter < n:
            output.append((counter, thread_sums[counter]))
            thread_sums[counter] += data[i]
            counter += 1
        else:
            counter = 0
            output.append((counter, thread_sums[counter]))
            thread_sums[counter] += data[i]
            counter += 1

    return output

def main():
    # input consists of two lines
    # first line - n and m
    # n - thread count (Y U NO CALL IT THREADS THEN???)
    # m - job count
    n = 0
    m = 0

    # input from keyboard
    counts = list(map(int, input().split()))
    n = counts[0]
    m = counts[1]
    data = list(map(int, input().split()))


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
