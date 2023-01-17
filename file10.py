def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=[]
    for i in data.split('\n'):
           s.append(len(i)) 
    return max(s)
f=open('txt_file/data10.txt')
f=f.read()
print(main(f))