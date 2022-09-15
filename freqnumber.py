import sys

def save_file(output_file, integers, reals):
    """ Write to output file """
    file = open(output_file, "w")
    kk = len(integers[0])
    if kk>0:
        file.write('integer:\n')
    for i in range(kk):
        file.write(str(integers[0][i])+' '+str(integers[1][i])+'\n')
    kk = len(reals[0])
    if kk > 0:
        file.write('real:\n')
    for i in range(kk):
        file.write(str(reals[0][i]) + ' ' + str(reals[1][i]) + '\n')
    file.close()

def read_file(input_file):
    """ Read input file """
    file = open(input_file, "r")
    text = file.read()
    file.close()
    return text

def find_k_most_integers( k , input_text ):
    """ Find k most integer numbers """
    k = int(k)
    splitted_numbers = input_text.split()
    pure_integers = list(filter(lambda item: test_integer(item), splitted_numbers))
    unique_integers = list(set(pure_integers))
    freqs = list(map(lambda item: freq_count(pure_integers,item),unique_integers))
    parallel_list = list(map(lambda x,y: (x,y) ,unique_integers,freqs))
    after_sort = bubble_sort(parallel_list)
    final_freqs = list(map (lambda item:(item[1]),after_sort))
    if len(final_freqs)>k:
        freq_lst = list(set(final_freqs))
        min_freq = min(freq_lst[len(freq_lst)-k:])
        ks = len(list(filter(lambda x: x[1]>=min_freq,after_sort)))
    else:
        ks = k
    final_freqs =list(map (lambda item:(item[1]),after_sort))[:ks]
    final_integers = list(map (lambda item:(item[0]),after_sort))[:ks]
    return (final_integers,final_freqs)

def find_k_most_reals( k , input_text ):
    """ Find k most real numbers """
    k = int(k)
    splitted_reals = input_text.split()
    pure_reals = list(filter(lambda item: test_real(item), splitted_reals))
    unique_reals = list(set(pure_reals))
    freqs = list(map(lambda item: freq_count(pure_reals, item), unique_reals))
    parallel_list = list(map(lambda x, y: (x, y), unique_reals, freqs))
    after_sort = bubble_sort(parallel_list)
    final_freqs = list(map(lambda item: (item[1]), after_sort))
    if len(final_freqs) > k:
        freq_lst = list(set(final_freqs))
        min_freq = min(freq_lst[len(freq_lst) - k:])
        ks = len(list(filter(lambda x: x[1] >= min_freq, after_sort)))
    else:
        ks = k
    final_freqs = list(map (lambda item:(item[1]),after_sort))[:ks]
    final_reals = list(map (lambda item:(item[0]),after_sort))[:ks]
    return (final_reals, final_freqs)

def test_integer(s):
    """ Method to verify integer number"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def test_real(s):
    """ Method to verify real number"""
    try:
        if float(s) and '.' in str(s) and str(s)[-1]!='.':
            return True
    except ValueError:
        return False

def freq_count(lst,key):
    """ Counts freq. of key in the lst """
    if lst == []:
        return 0
    if lst[0] == key:
        return 1 + freq_count(lst[1:],key)
    else:
        return 0 + freq_count(lst[1:],key)

def bubble_sort(ar):
    """ Customized Recursive Bubble Sort """
    if len(ar) <= 1:
        return ar
    if len(ar) == 2:
        return ar if ar[0][1] > ar[1][1] else (ar if (ar[0][1] == ar[1][1] and 0<ar[1][1] and 1<ar[1][1]) else [ar[1], ar[0]])
    a, b = ar[0], ar[1]
    bs = ar[2:]
    res = []
    if a[1] >= b[1]:
        if a[1] == b[1] and 1>a[1]:
            res = [b] + bubble_sort([a] + bs)
        else:
            res = [a] + bubble_sort([b] + bs)
    else:
        res = [b] + bubble_sort([a] + bs)
    return bubble_sort(res[:-1]) + res[-1:]



############### APPLICATION ###############
### Read args
if len(sys.argv)>=2 and len(sys.argv[1].split(";"))==3:
    # validate input args
    args = sys.argv[1]
    k = args.split(";")[0].split("=")[1]
    if(not test_integer(k)):
        # validate input k
        print("Error! Valid k is required!")
        exit()
    input_file = args.split(";")[1].split("=")[1]
    output_file = args.split(";")[2].split("=")[1]
else:
    print("Error! Please correct your arguments as: k=3;input=input.txt;output=freqnumber.txt")
    exit()

### Read input file
try:
    f = open(input_file,'r').readlines()
    input_text = read_file(input_file)
except FileNotFoundError:
    print("Error! Input file not accessible!")
    exit()

### Count Integers
integers = find_k_most_integers(k,input_text)

### Count Reals
reals = find_k_most_reals(k,input_text)

### Save Result
save_file(output_file,integers,reals)
