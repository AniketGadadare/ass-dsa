def brackets_check(x):
    var = []
 
    for i in x:
        if i in ["(", "{", "["]:
            var.append(i)
            
        else:
            if not var:
                return False
            temp_char = var.pop()
            if temp_char == '(':
                if i != ")":
                    return False
            if temp_char == '{':
                if i != "}":
                    return False
            if temp_char == '[':
                if i != "]":
                    return False
 
    if var:
        return False
    return True

x = "{()}[(]"
    
if brackets_check(x):
    print("Balanced")
else:
    print("Not Balanced")