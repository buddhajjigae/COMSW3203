#COMS3203 DISCRETE MATHEMATICS
#CODING ASSIGNMENT 1

#YOUR NAME: Alex Yu
#YOUR UNI: ajy2116


def format_prop(prop):

    operators = ["or","and","if","iff","xor"]
    notoperator = ["not"]   

    #base case
    if isinstance(prop, list) == False:
        return prop
    #if operator
    elif prop[0] in operators:
        operator = str(prop[0])
        if operator == "if":
            operator = "->"
        if operator == "iff":
            operator = "<->"
        prop1 = "(" + format_prop(prop[1])
        prop2 = format_prop(prop[2]) + ")"
        return prop1 + " " + operator + " " + prop2
    #not operator
    elif prop[0] in notoperator:
        n1 = "(" + prop[0]
        p1 = format_prop(prop[1]) + ")"
        return n1 + " " + p1
    
    return ""

def eval_prop(prop, values):

    operators = ["or", "and", "if", "iff", "xor"]
    notoperator = ["not"]   
    evaluate = 0
    
    #base case
    if isinstance(prop, list) == False:
        if prop == "true":
            return 1
        elif prop == "false":
            return 0
        else:
            i = int(prop[1:])
            return values[i-1]
    #if operator
    elif prop[0] in operators:
        operator = str(prop[0])
        prop1 = eval_prop(prop[1], values)
        prop2 = eval_prop(prop[2], values)                
        if operator == "or":
            if prop1 == 1 or prop2 == 1:
                evaluate = 1
        if operator == "and":
            if prop1 == 1 and prop2 == 1:
                evaluate = 1
        if operator == "if":
            if prop2 == 1:
                evaluate = 1
            elif prop1 == 0 and prop2 == 0:
                evaluate = 1
        if operator == "iff":
            if prop1 == 1 and prop2 == 1:
                evaluate = 1
            elif prop1 == 0 and prop2 == 0:
                evaluate = 1
        if operator == "xor":
            if prop1 == 1:
                if prop2 == 0:
                    evaluate = 1
            elif prop2 == 1:
                if prop1 == 0:
                    evaluate = 1
    #not operator 
    elif prop[0] in notoperator:
        p1 = eval_prop(prop[1], values)
        if p1 == 0:
            evaluate = 1
        elif p1 == 1:
            evaluate = 0

    return evaluate

def print_table(prop, n_var):

    statement = format_prop(prop)
    
    for i in range(n_var):
        print("p" + str(i+1), end = " | ")
    print(statement)
        
    for j in range(2**n_var):
        valuesStr = bin(j)[2:].zfill(n_var)
        values = list(map(int, valuesStr))
        evaluate = eval_prop(prop, values)
        print('  | '.join(valuesStr) + "  | " + str(evaluate))

    pass


if __name__ == '__main__':
    print("---------------------------------------")
    print("Welcome to Propositional Logic!")
    print("---------------------------------------")
    values = [1, 1, 0]
    prop = ["if", ["and", "p1", ["not", "p2"]], "p3"]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    prop_str = format_prop(prop)
    print("Evaluating proposition p =", prop_str)
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print()
    values = [1, 0, 1]
    prop = ["iff", "p1", ["or", "p2", ["not", "p3"]]]
    ps_str = " ".join("p{}={}".format(i + 1, v) for i, v in enumerate(values))
    print("Evaluating proposition p =", format_prop(prop))
    prop_val = eval_prop(prop, values)
    print("over", ps_str, ":", prop_val)

    print("---------------------------------------------------")
    print("Table:")
    print_table(["if", ["and", "p1", ["not", "p2"]], "p3"], 3)
