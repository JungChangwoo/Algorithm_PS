def solution(new_id):
    new_id = new_id.lower()
    
    for s in new_id:
        if s.isalnum() or s == '-' or s == '_' or s == '.':
            continue
        else:
            new_id = new_id.replace(s, '')
    
    stack = []
    for s in new_id:
        if stack and (stack[-1] == '.' and s == '.'):
            continue
        stack.append(s)
    new_id = ''.join(s for s in stack)
    
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    if not new_id:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id