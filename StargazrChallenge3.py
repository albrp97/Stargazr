#Since this is not a real compilator expresions such as +++++++ are valid even though they serve no purpose
#Expresions like ++++ are considered multiple operators

#checkTokens process input string by expresion kind using auxiliar functions like isNumber, isOperator...

operators="+-*/#.,=:{}[]"

def isNumber(token):
    return str.isdigit(token) or token=='.'

def isOperator(token):
    return  operators.__contains__(token)

def isGrouping(token):
    return token=="(" or token == ")"

def checkTokens(t):
    output=0
    processed=""
    unprocessed=""+t
    while len(unprocessed) >0:
        if unprocessed[0] == "\"":  #Strings
            processed += unprocessed[0]
            unprocessed = unprocessed[1:]
            if len(unprocessed) < 1:
                print("Error: string not closed")
                return 0

            end=False
            while not end:
                if unprocessed[0] == "\\" and processed[-1]=="\\":
                    unprocessed = unprocessed[1:]
                    processed+="."
                else:

                    if unprocessed[0] == '"' and processed[-1]!="\\":
                        end=True
                        if len(unprocessed) <=1:
                            print("String")
                            return output + 2


                    processed += unprocessed[0]
                    unprocessed = unprocessed[1:]
                if len(unprocessed) <1:
                    print("Error: string not closed")
                    return 0

            output += 2
            print("String")
        elif str.isdigit(unprocessed[0]) or unprocessed[0] == "." and str.isdigit(unprocessed[1]): #Number
            oneDot=True
            while len(unprocessed) >0 and (str.isdigit(unprocessed[0]) or (unprocessed[0] == "." and oneDot)):
                if unprocessed[0] == ".":
                    oneDot=False
                processed+=unprocessed[0]
                unprocessed=unprocessed[1:]
            output +=3
            print("Number")
        elif unprocessed[0] ==" ": #blanks
            processed += unprocessed[0]
            unprocessed = unprocessed[1:]
        elif isOperator(unprocessed[0]): #Operators
            processed += unprocessed[0]
            unprocessed = unprocessed[1:]
            output += 5
            print("Operator")
        elif isGrouping(unprocessed[0]): #Groups
            processed += unprocessed[0]
            unprocessed = unprocessed[1:]
            output+=4
            print("Grouping")
        elif unprocessed[0].islower() or unprocessed[0].isupper() or unprocessed[0]=="_" and not isNumber(unprocessed[0]): #Names
            while unprocessed[0].islower() or unprocessed[0].isupper() or str.isdigit(unprocessed[0]) or unprocessed[0]=="_":
                if len(unprocessed)==1:
                    print("Name")
                    return output+7
                processed += unprocessed[0]
                unprocessed = unprocessed[1:]
            output += 7
            print("Name")
        else: #Unknown characters
            print("Error: unknown character "+unprocessed[0].__str__())
            return 0

    return output


f = open("./datasets/P3big.txt")
alltext=f.readlines()[1:]


solutions=[]
for thisText in alltext:
    text=thisText[:-1]
    print(text)
    solutions.append(checkTokens(text))

for i in range(len(solutions)):
    print("\n\n"+i.__str__()+": "+alltext[i].__str__())
    print(solutions[i].__str__())
