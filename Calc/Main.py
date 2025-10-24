test_term = "1+"

def cleanUp(formula):
    formulaClean = ""

    formula.strip
    for i in formula:
        if i != " ":
            formulaClean += i

    return formulaClean

def tokenize(term:str):
    last_char = ""
    counter = 0
    tokens = []
    for i in term:
        if counter == 0:
            last_char = i
        else:
            if i != " ":
                match last_char.isdigit(),i.isdigit():
                    case False, False:
                        raise SyntaxError(f"Two consecutive operators ... {last_char+" "+i} ...")
                    case True, False:
                        tokens.append(last_char)
                        last_char = i
                    case False, True:
                        tokens.append(last_char)
                        last_char = i
                    case True,True:
                        last_char += i 
        counter += 1
    tokens.append(last_char)
    return tokens

tokens = tokenize(cleanUp(test_term))
print(tokens)

def doMeth(num1,op,num2):
    match op:
        case "+":
            return str(float(num1) + float(num2))
        case "-":
            return str(float(num1) - float(num2))
        case "*":
            return str(float(num1) * float(num2))
        case "/":
            return str(float(num1) / float(num2))

def firstSolve(tokens):
    while any(op in tokens for op in ["*", "/"]):
        for i in range(len(tokens)):
            if tokens[i] in ["*","/"]:
                print(f"{tokens[i-1]}{tokens[i]}{tokens[i+1]}={doMeth(tokens[i-1],tokens[i],tokens[i+1])}")
                asw = doMeth(tokens[i-1],tokens[i],tokens[i+1])
                del tokens[i-1]
                del tokens[i-1]
                tokens[i-1] = asw
                # print(tokens)
                break
    return tokens

def secondSolve(tokens):
    while any(op in tokens for op in ["+", "-"]):
        for i in range(len(tokens)):
            if tokens[i] in ["+","-"]:
                print(f"{tokens[i-1]}{tokens[i]}{tokens[i+1]}={doMeth(tokens[i-1],tokens[i],tokens[i+1])}")
                asw = doMeth(tokens[i-1],tokens[i],tokens[i+1])
                del tokens[i-1]
                del tokens[i-1]
                tokens[i-1] = asw
                # print(tokens)
                break
    return tokens

def solveTokens(tokens):
    solveOne = firstSolve(tokens)
    # print(solveOne)
    return secondSolve(solveOne)

print(f"Ergebniss: {solveTokens(tokens)[0]}")