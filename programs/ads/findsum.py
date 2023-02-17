def find_sum(seq, target): #pri zdvojnasobeni sa najhorsi pripad zdvojnasobi tiez
    """finds the first subsequence of an array with the given sum
    returns: start and end index of the subsequence or None if not found
    args: iterable of nums, target sum
    Time complexity: O(n) - trvaversal through the sequence
    Memory complexity: O(1)
    """
    #najkratsie to trva, ak je suctom prvy prvok
    #najdlhsie to trva, ak prebehne cele pole
    start = 0
    sum = seq[0]
    end = 1

    while end<=len(seq):

        while sum > target and start < end-1:
            sum -= seq[start]
            start+=1

        if sum == target:
            return (start, end)
        
        if end < len(seq):
            sum+=seq[end]
            
        end+=1


def findSum(seq, target): #pri zdvojnasobeni dlzky pola sa cas zvacsi styrikrat
    #zvysok plati ako pri linearnom traversali
    """finds the first subsequence of an array with the given sum
    returns: start and end index of the subsequence or None if not found
    args: iterable of nums, target sum
    Time complexity: O(n**2)
    Memory complexity: O(1)
    """
    
    n = len(seq)
    for start in range(n+1):
        sum = 0
        for end in range(start,n):
            sum+=seq[end]
            if sum == target:
                return (start,end+1)
            elif sum > target:
                break
    #zacne byt vyrazne pomaly pri cca 10k-prvkovom poli

def firstOccurance(element, record): #kratko - ak je to prvy prvok, dlho - ak je posledny
    # tiez sa zdvojnasobi cas
    #10**11 uz nedalo :D
    """finds the first occurance in the sequence if the given value
    returns: index or None if not found
    args: target value and record of values
    Time complexity: O(n)
    """
    for index, value in enumerate(record):
        if value == element:
            return index
    
            
    
    
