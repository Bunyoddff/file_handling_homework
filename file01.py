def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=[]
    for i in data.split(','):
        s.append(int(i))
    return s
f=open('txt_file/data01.txt')
f=f.read()
print(main(f))