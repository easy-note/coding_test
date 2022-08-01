
from ast import expr_context
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id=re.sub('[^a-z0-9-_.]', '', new_id)
    new_id=re.sub('[.]+', '.', new_id)
        
    try:
        if new_id[0] == '.':
            new_id=new_id[1:]
    except:
        pass
    
    try:
        if new_id[-1] == '.':
            new_id=new_id[:-1]
    except:
        pass
    
    if new_id == "":
        new_id = 'a'
        
    if len(new_id)>=16:
        new_id=new_id[:15]
        
    try:
        if new_id[-1] == '.':
            new_id=new_id[:-1]
    except:
        pass
    
    if len(new_id)<=2:
        while True:
            if len(new_id)>2:
                break
            new_id += new_id[-1]
            

    
    return new_id
    
if __name__ == '__main__':
    print(solution('abcdefghijklmn.p'))