def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=[]
    for i in data:
        if i.isdigit():
            s.append(i)
    return s
f=open('txt_file/data03.txt')
f=f.read()
print(main(f))