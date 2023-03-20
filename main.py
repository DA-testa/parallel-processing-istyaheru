#Ēriks Lijurovs 221RDB041 16. grupa
# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
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

    choice = input()

    if choice.__contains__('F'):
        test = input()
        
        if test.__contains__('a'):
            return
        else:
            gh_bypass = os.path.join(os.getcwd(), 'tests', test)
            with open(gh_bypass) as file:
                counts = list(map(int, file.readline().split(" ")))
                n = counts[0]
                m = counts[1]
                data = list(map(int, file.readline().split(" ")))
            file.close()
    elif choice.__contains__('I'):
        # input from keyboard
        counts = list(map(int, input().split()))
        n = counts[0]
        m = counts[1]
        data = list(map(int, input().split()))
    else:
        print("Please enter I or F!")
        return

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result:
        print(i, j)



if __name__ == "__main__":
    main()
