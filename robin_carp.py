
def find_substring( txt, pattern):
    # find str_b pattern within str_a 
    # step1: generate all the hases of length(str_b)
    # step2: verify the hash of pattern with the listing
    # step3: if same hash value, check the actual substring

    M = len(pattern)
    N = len(txt)

    for i in xrange(M-1):
        h = (L)



def main():
    str_a = "life is a bed of roses"
    str_b = "bed"
    print(find_substring(str_a,str_b))

if __name__ == "__main__":
    main()
