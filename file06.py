def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=[]
    for i in data.split('\n'):
            s.append(len(i))
            
    return s
f=open('txt_file/data06.txt')
f=f.read()
print(main(f))