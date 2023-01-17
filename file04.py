def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=[]
    for i in data:
        if i.isalpha():
            s.append(i)
    return s
f=open('txt_file/data04.txt')
f=f.read()
print(main(f))