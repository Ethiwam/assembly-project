import sys

# Lines 1-5 for testing

filename = input("Enter a filename: ")
f = open(filename)
instr = []
loop = 0


def assemble(line, instr, loop):
    skipFlag = 0
    immediateFlag = 0
    errorFlag = 0
    op = ''
    inp = ''
    oreg = ''
    ireg = ''

    #Opcode Translation
    op = line[0]
    if op.lower() == "ld":
        op = "000"
    elif op.lower() == "st":
        op = "001"
    elif op.lower() == "mov":
        op = "010"
    elif op.lower() == "add":
        op = "011"
    elif op.lower() == "div":
        op = "100"
    elif op.lower() == "inp":
        op = "101"
    elif op.lower() == "prt":
        op = "110"
    elif op.lower() == "jne":
        op = "111"
    elif ':' in op:
        skipFlag = 1
        loop = "1111111111111111"
    elif op == ';':
        skipFlag = 1
    else:
        errorFlag = 1
    #print("op = " + op)  <-- TESTING

    #Register Translation
    if (skipFlag != 1) and (errorFlag != 1):
        inp = line[1]
        #print("inp = " + inp)  <-- TESTING
        if ',' in inp:                      # 2 Registers
            #print("COMMA FOUND")  <-- TESTING
            sinp = inp.split(',')
            oreg = sinp[0]
            #print("oreg = " + oreg)  <-- TESTING
            ireg = sinp[1]
            #print("ireg = " + ireg)  <-- TESTING
            if oreg == "r0":                # Output Register
                oreg = "000"
            elif oreg == "r1":
                oreg = "001"
            elif oreg == "r2":
                oreg = "010"
            elif oreg == "r3":
                oreg = "011"
            elif oreg == "r4":
                oreg = "100"
            elif oreg == "r5":
                oreg = "101"
            elif '[' and ']' in oreg:
                oreg = oreg.replace('[', '')
                oreg = oreg.replace(']', '')
                if 'r' in oreg:
                    if oreg == "r0":
                        oreg = "000"
                    elif oreg == "r1":
                        oreg = "001"
                    elif oreg == "r2":
                        oreg = "010"
                    elif oreg == "r3":
                        oreg = "011"
                    elif oreg == "r4":
                        oreg = "100"
                    elif oreg == "r5":
                        oreg = "101"
                elif len(oreg) == 4:
                    immediateFlag = 1
                    if '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in oreg:
                        oreg = str(bin(int(oreg)))
                        oreg = oreg.replace("0b", '')
                        while len(oreg) < 8:
                            oreg = '0' + oreg
                        oreg = "11" + oreg
                    else:
                        oreg = oreg
                elif oreg.isdigit():
                    immediateFlag = 1
                    oreg = str(bin(int(oreg)))
                    oreg = oreg.replace("0b", '')
                    while len(oreg) < 8:
                        oreg = '0' + oreg
                    oreg = "11" + oreg
            if ireg == "r0":                       # Input Register
                ireg = "000"
            elif ireg == "r1":
                ireg = "001"
            elif ireg == "r2":
                ireg = "010"
            elif ireg == "r3":
                ireg = "011"
            elif ireg == "r4":
                ireg = "100"
            elif ireg == "r5":
                ireg = "101"
            elif '[' and ']' in ireg:
                ireg = ireg.replace('[', '')
                ireg = ireg.replace(']', '')
                if 'r' in ireg:
                    if ireg == "r0":
                        ireg = "000"
                    elif ireg == "r1":
                        ireg = "001"
                    elif ireg == "r2":
                        ireg = "010"
                    elif ireg == "r3":
                        ireg = "011"
                    elif ireg == "r4":
                        ireg = "100"
                    elif ireg == "r5":
                        ireg = "101"
                elif len(ireg) == 4:
                    immediateFlag = 1
                    if '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in ireg:
                        ireg = str(bin(int(ireg)))
                        ireg = ireg.replace("0b", '')
                        while len(ireg) < 8:
                            ireg = '0' + ireg
                        ireg = "11" + ireg
                    else:
                        ireg = ireg
            elif ireg.isdigit():
                immediateFlag = 1
                ireg = str(bin(int(ireg)))
                ireg = ireg.replace("0b", '')
                while len(ireg) < 8:
                    ireg = '0' + ireg
                ireg = "11" + ireg
            if len(line) > 2:
                if line[2] != ';':
                    errorFlag = 1
        elif (op == "101") or (op == "110"):        # Single Register
            #print("NO COMMA LOCATED")  <-- TESTING
            if inp == "r0":
                inp = "0000000000000"
            elif inp == "r1":
                inp = "0010000000000"
            elif inp == "r2":
                inp = "0100000000000"
            elif inp == "r3":
                inp = "0110000000000"
            elif inp == "r4":
                inp = "1000000000000"
            elif inp == "r5":
                inp = "1010000000000"
        else:
            errorFlag = 1

    #Error Check and instruction appending
    if errorFlag == 1:
        return "ERROR FOUND"
        f.close()
        sys.exit("== Program closed due to error ==")
    else:
        if op == "001":
            binary = op + ireg + oreg
            if immediateFlag != 1:
                binary = binary + "0000000"
            instr.append(binary)
            return binary
        elif (op == "101") or (op == "110"):
            binary = op + inp
            instr.append(binary)
            return binary
        elif op == ';':
            return "This line got skipped"
        elif ':' in op:
            #print("Loop has been stored to r6")  <-- TESTING
            instr.append(loop)
            return 'x'
        else:
            binary = op + oreg + ireg
            if immediateFlag != 1:
                binary = binary + "0000000"
            instr.append(binary)
            return binary
        
#Lines past this point are for testing

f = open(filename)
lines = len(f.readlines())
f.close()
f = open(filename)

i = 0
while i < lines:
    l = f.readline()
    line = l.split()
    #print(assemble(line, instr, loop))
    assemble(line, instr, loop)
    i += 1

#print("Here's the instr:")
#print(instr)
f.close()
f = open("bnry.txt", "w")
for x in instr:
    if x == instr[0]:
        f.write(x)
    else:
        f.write("\n" + x)
f.close()