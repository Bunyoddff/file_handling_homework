def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=0
    for i in data:
        if i.isdigit():
            s+=1
    return [s,len(data)-s]
f=open('txt_file/data05.txt')
f=f.read()
print(main(f))