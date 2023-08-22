import sys
import math

def to_decimal(string): # only works on 8-bit strings
    sum = 0
    if string[0] == '1':
        sum += 128
    if string[1] == '1':
        sum += 64
    if string[2] == '1':
        sum += 32
    if string[3] == '1':
        sum += 16
    if string[4] == '1':
        sum += 8
    if string[5] == '1':
        sum += 4
    if string[6] == '1':
        sum += 2
    if string[7] == '1':
        sum += 1
    return sum

def parity(integer): # works to find the binary parity of some integer
    binary = bin(integer)
    binary = str(binary)
    binary = binary.replace('0b', '')
    if len(binary) > 4:
        binary = binary[len(binary)-4:]

    i = 0
    count = 0
    while i < len(binary):
        if binary[i] == '1':
            count += 1
        i += 1
    if count % 2 == 0:
        return 1
    else:
        return 0

# instr acts as the instruction segment of main memory
instr = []

f = open("bnry.txt")
lines = len(f.readlines())
f.close()
f = open ("bnry.txt")
i = 0
while i < lines:
    instr.append(f.readline())
    instr[i] = instr[i].replace('\n', '')
    i += 1
f.close()

r0 = [0]
r1 = [0]
r2 = [0]
r3 = [0]
r4 = [0]
r5 = [0]
r6 = [0]
r7 = [0]
flag_register = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 4:OF 8:SF 9:ZF 13:PF

data_segment = []
data_size = len(data_segment)

f = open("sim_cpu.rpt", "w")
f.write("")
f.close()

while len(data_segment) <= 0xFFFF:
    if r7[0] == len(instr):
        break
    address_flag = 0
    task = instr[r7[0]]
    opcode = task[0:3]
    reg1 = task[3:6]
    reg2 = task[6:9]
    extra = task[9:16]
    # PRINTS FOR TESTING
    #print("Opcode: " + opcode)
    #print("Reg 1: " + reg1)
    #print("Reg 2: " + reg2)
    #print("Extra: " + extra)
    #print("Flags: " + str(flag_register))

    if task == "1111111111111111":
        r6[0] = r7[0]
        address_flag = 1

    if opcode == "000": # Load Instructions --------------------------------------------
        if reg1 == "000":
            if reg2 == "000":
                r0[0] = data_segment[r0[0]]
            if reg2 == "001":
                r0[0] = data_segment[r1[0]]
            if reg2 == "010":
                r0[0] = data_segment[r2[0]]
            if reg2 == "011":
                r0[0] = data_segment[r3[0]]
            if reg2 == "100":
                r0[0] = data_segment[r4[0]]
            if reg2 == "101":
                r0[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r0[0] = data_segment[idec]
        if reg1 == "001":
            if reg2 == "000":
                r1[0] = data_segment[r0[0]]
            if reg2 == "001":
                r1[0] = data_segment[r1[0]]
            if reg2 == "010":
                r1[0] = data_segment[r2[0]]
            if reg2 == "011":
                r1[0] = data_segment[r3[0]]
            if reg2 == "100":
                r1[0] = data_segment[r4[0]]
            if reg2 == "101":
                r1[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r1[0] = data_segment[idec]
        if reg1 == "010":
            if reg2 == "000":
                r2[0] = data_segment[r0[0]]
            if reg2 == "001":
                r2[0] = data_segment[r1[0]]
            if reg2 == "010":
                r2[0] = data_segment[r2[0]]
            if reg2 == "011":
                r2[0] = data_segment[r3[0]]
            if reg2 == "100":
                r2[0] = data_segment[r4[0]]
            if reg2 == "101":
                r2[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r2[0] = data_segment[idec]
        if reg1 == "011":
            if reg2 == "000":
                r3[0] = data_segment[r0[0]]
            if reg2 == "001":
                r3[0] = data_segment[r1[0]]
            if reg2 == "010":
                r3[0] = data_segment[r2[0]]
            if reg2 == "011":
                r3[0] = data_segment[r3[0]]
            if reg2 == "100":
                r3[0] = data_segment[r4[0]]
            if reg2 == "101":
                r3[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r3[0] = data_segment[idec]
        if reg1 == "100":
            if reg2 == "000":
                r4[0] = data_segment[r0[0]]
            if reg2 == "001":
                r4[0] = data_segment[r1[0]]
            if reg2 == "010":
                r4[0] = data_segment[r2[0]]
            if reg2 == "011":
                r4[0] = data_segment[r3[0]]
            if reg2 == "100":
                r4[0] = data_segment[r4[0]]
            if reg2 == "101":
                r4[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r4[0] = data_segment[idec]
        if reg1 == "101":
            if reg2 == "000":
                r5[0] = data_segment[r0[0]]
            if reg2 == "001":
                r5[0] = data_segment[r1[0]]
            if reg2 == "010":
                r5[0] = data_segment[r2[0]]
            if reg2 == "011":
                r5[0] = data_segment[r3[0]]
            if reg2 == "100":
                r5[0] = data_segment[r4[0]]
            if reg2 == "101":
                r5[0] = data_segment[r5[0]]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r5[0] = data_segment[idec]


    if opcode == "001": # Store Instructions ---------------------------------------------------
        if reg1 == "000":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r0[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r0[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r0[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r0[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r0[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r0[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r0[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r0[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r0[0])
        if reg1 == "001":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r1[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r1[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r1[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r1[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r1[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r1[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r1[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r1[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r1[0])
        if reg1 == "010":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r2[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r2[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r2[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r2[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r2[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r2[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r2[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r2[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r2[0])
        if reg1 == "011":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r3[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r3[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r3[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r3[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r3[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r3[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r3[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r3[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r3[0])
        if reg1 == "100":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r4[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r4[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r4[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r4[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r4[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r4[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r4[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r4[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r4[0])
        if reg1 == "101":
            if reg2 == "000":
                if r0[0] < len(data_segment):
                    data_segment[r0[0]] = r5[0]
                else:
                    while len(data_segment) < r0[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2 == "001":
                if r1[0] < len(data_segment):
                    data_segment[r1[0]] = r5[0]
                else:
                    while len(data_segment) < r1[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2 == "010":
                if r2[0] < len(data_segment):
                    data_segment[r2[0]] = r5[0]
                else:
                    while len(data_segment) < r2[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2 == "011":
                if r3[0] < len(data_segment):
                    data_segment[r3[0]] = r5[0]
                else:
                    while len(data_segment) < r3[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2 == "100":
                if r4[0] < len(data_segment):
                    data_segment[r4[0]] = r5[0]
                else:
                    while len(data_segment) < r4[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2 == "101":
                if r5[0] < len(data_segment):
                    data_segment[r5[0]] = r5[0]
                else:
                    while len(data_segment) < r5[0]:
                        data_segment.append(0)
                    data_segment.append(r5[0])
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                if idec < len(data_segment):
                    data_segment[idec] = r5[0]
                else:
                    while len(data_segment) < idec:
                        data_segment.append(0)
                    data_segment.append(r5[0])


    if opcode == "010": # Move Instructions ---------------------------------------------
        if reg1 == "000":
            if reg2 == "000":
                r0[0] = r0[0]
            if reg2 == "001":
                r0[0] = r1[0]
            if reg2 == "010":
                r0[0] = r2[0]
            if reg2 == "011":
                r0[0] = r3[0]
            if reg2 == "100":
                r0[0] = r4[0]
            if reg2 == "101":
                r0[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r0[0] = idec
        if reg1 == "001":
            if reg2 == "000":
                r1[0] = r0[0]
            if reg2 == "001":
                r1[0] = r1[0]
            if reg2 == "010":
                r1[0] = r2[0]
            if reg2 == "011":
                r1[0] = r3[0]
            if reg2 == "100":
                r1[0] = r4[0]
            if reg2 == "101":
                r1[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r1[0] = idec
        if reg1 == "010":
            if reg2 == "000":
                r2[0] = r0[0]
            if reg2 == "001":
                r2[0] = r1[0]
            if reg2 == "010":
                r2[0] = r2[0]
            if reg2 == "011":
                r2[0] = r3[0]
            if reg2 == "100":
                r2[0] = r4[0]
            if reg2 == "101":
                r2[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r2[0] = idec
        if reg1 == "011":
            if reg2 == "000":
                r3[0] = r0[0]
            if reg2 == "001":
                r3[0] = r1[0]
            if reg2 == "010":
                r3[0] = r2[0]
            if reg2 == "011":
                r3[0] = r3[0]
            if reg2 == "100":
                r3[0] = r4[0]
            if reg2 == "101":
                r3[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r3[0] = idec
        if reg1 == "100":
            if reg2 == "000":
                r4[0] = r0[0]
            if reg2 == "001":
                r4[0] = r1[0]
            if reg2 == "010":
                r4[0] = r2[0]
            if reg2 == "011":
                r4[0] = r3[0]
            if reg2 == "100":
                r4[0] = r4[0]
            if reg2 == "101":
                r4[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r4[0] = idec
        if reg1 == "101":
            if reg2 == "000":
                r5[0] = r0[0]
            if reg2 == "001":
                r5[0] = r1[0]
            if reg2 == "010":
                r5[0] = r2[0]
            if reg2 == "011":
                r5[0] = r3[0]
            if reg2 == "100":
                r5[0] = r4[0]
            if reg2 == "101":
                r5[0] = r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r5[0] = idec


    if opcode == "011": # Add Instructions ---------------------------------------------
        if reg1 == "000":
            if reg2 == "000":
                r0[0] = r0[0] + r0[0]
            if reg2 == "001":
                r0[0] = r0[0] + r1[0]
            if reg2 == "010":
                r0[0] = r0[0] + r2[0]
            if reg2 == "011":
                r0[0] = r0[0] + r3[0]
            if reg2 == "100":
                r0[0] = r0[0] + r4[0]
            if reg2 == "101":
                r0[0] = r0[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r0[0] = r0[0] + idec
            if r0[0] > 0xffff: # FLAG REGISTER ==============
                r0[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r0[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r0[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r0[0])
        if reg1 == "001":
            if reg2 == "000":
                r1[0] = r1[0] + r0[0]
            if reg2 == "001":
                r1[0] = r1[0] + r1[0]
            if reg2 == "010":
                r1[0] = r1[0] + r2[0]
            if reg2 == "011":
                r1[0] = r1[0] + r3[0]
            if reg2 == "100":
                r1[0] = r1[0] + r4[0]
            if reg2 == "101":
                r1[0] = r1[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r1[0] = r1[0] + idec
            if r1[0] > 0xffff: # FLAG REGISTER ==============
                r1[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r1[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r1[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r1[0])
        if reg1 == "010":
            if reg2 == "000":
                r2[0] = r2[0] + r0[0]
            if reg2 == "001":
                r2[0] = r2[0] + r1[0]
            if reg2 == "010":
                r2[0] = r2[0] + r2[0]
            if reg2 == "011":
                r2[0] = r2[0] + r3[0]
            if reg2 == "100":
                r2[0] = r2[0] + r4[0]
            if reg2 == "101":
                r2[0] = r2[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r2[0] = r2[0] + idec
            if r2[0] > 0xffff: # FLAG REGISTER ==============
                r2[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r2[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r2[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r2[0])
        if reg1 == "011":
            if reg2 == "000":
                r3[0] = r3[0] + r0[0]
            if reg2 == "001":
                r3[0] = r3[0] + r1[0]
            if reg2 == "010":
                r3[0] = r3[0] + r2[0]
            if reg2 == "011":
                r3[0] = r3[0] + r3[0]
            if reg2 == "100":
                r3[0] = r3[0] + r4[0]
            if reg2 == "101":
                r3[0] = r3[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r3[0] = r3[0] + idec
            if r3[0] > 0xffff: # FLAG REGISTER ==============
                r3[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r3[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r3[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r3[0])
        if reg1 == "100":
            if reg2 == "000":
                r4[0] = r4[0] + r0[0]
            if reg2 == "001":
                r4[0] = r4[0] + r1[0]
            if reg2 == "010":
                r4[0] = r4[0] + r2[0]
            if reg2 == "011":
                r4[0] = r4[0] + r3[0]
            if reg2 == "100":
                r4[0] = r4[0] + r4[0]
            if reg2 == "101":
                r4[0] = r4[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r4[0] = r4[0] + idec
            if r4[0] > 0xffff: # FLAG REGISTER ==============
                r4[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r4[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r4[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r4[0])
        if reg1 == "101":
            if reg2 == "000":
                r5[0] = r5[0] + r0[0]
            if reg2 == "001":
                r5[0] = r5[0] + r1[0]
            if reg2 == "010":
                r5[0] = r5[0] + r2[0]
            if reg2 == "011":
                r5[0] = r5[0] + r3[0]
            if reg2 == "100":
                r5[0] = r5[0] + r4[0]
            if reg2 == "101":
                r5[0] = r5[0] + r5[0]
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                r5[0] = r5[0] + idec
            if r5[0] > 0xffff: # FLAG REGISTER ==============
                r5[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r5[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r5[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r5[0])


    if opcode == "100": # Division Instructions ------------------------------------------
        if reg1 == "000":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r0[0] = r0[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r0[0] = r0[0] >> div
            if r0[0] > 0xffff: # FLAG REGISTER ==============
                r0[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r0[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r0[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r0[0])
        if reg1 == "001":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r1[0] = r1[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r1[0] = r1[0] >> div
            if r1[0] > 0xffff: # FLAG REGISTER ==============
                r1[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r1[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r1[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r1[0])
        if reg1 == "010":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r2[0] = r2[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r2[0] = r2[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r2[0] = r2[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                #print("Log2 = " + str(div))
                div = int(div)
                #print("Log2int = " + str(div))
                r2[0] = r2[0] >> div
                #print("Final = " + str(r2[0]))
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r2[0] = r2[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r2[0] = r2[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r2[0] = r2[0] >> div
            if r2[0] > 0xffff: # FLAG REGISTER ==============
                r2[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r2[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r2[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r2[0])
        if reg1 == "011":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r3[0] = r3[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r3[0] = r3[0] >> div
            if r3[0] > 0xffff: # FLAG REGISTER ==============
                r3[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r3[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r3[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r3[0])
        if reg1 == "100":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r4[0] = r4[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r4[0] = r4[0] >> div
            if r4[0] > 0xffff: # FLAG REGISTER ==============
                r4[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r4[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r4[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r4[0])
        if reg1 == "101":
            if reg2 == "000":
                div = math.log2(r0[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2 == "001":
                div = math.log2(r1[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2 == "010":
                div = math.log2(r2[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2 == "011":
                div = math.log2(r3[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2 == "100":
                div = math.log2(r4[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2 == "101":
                div = math.log2(r5[0])
                div = int(div)
                r5[0] = r5[0] >> div
            if reg2[0:2] == "11":
                ibin = reg2[2] + extra
                idec = to_decimal(ibin)
                div = math.log2(idec)
                div = int(div)
                r5[0] = r5[0] >> div
            if r5[0] > 0xffff: # FLAG REGISTER ==============
                r5[0] = 0xffff
                flag_register[4] = 1
            else:
                flag_register[4] = 0
            if r5[0] < 0:
                flag_register[8] = 1
            else:
                flag_register[8] = 0
            if r5[0] == 0:
                flag_register[9] = 1
            else: 
                flag_register[9] = 0
            flag_register[13] = parity(r5[0])


    if opcode == "101": # Input Instructions ------------------------------------------------
        if reg1 == "000":
            temp = r0[0]
            r0[0] = input()
            if r0[0].isdigit():
                r0[0] = int(r0[0])
            else:
                r0[0] = temp
            if r0[0] > 0xff:
                r0[0] = 0xff
        if reg1 == "001":
            temp = r1[0]
            r1[0] = input()
            if r1[0].isdigit():
                r1[0] = int(r1[0])
            else:
                r1[0] = temp
            if r1[0] > 0xff:
                r1[0] = 0xff
        if reg1 == "010":
            temp = r2[0]
            r2[0] = input()
            if r2[0].isdigit():
                r2[0] = int(r2[0])
            else:
                r2[0] = temp
            if r2[0] > 0xff:
                r2[0] = 0xff
        if reg1 == "011":
            temp = r3[0]
            r3[0] = input()
            if r3[0].isdigit():
                r3[0] = int(r3[0])
            else:
                r3[0] = temp
            if r3[0] > 0xff:
                r3[0] = 0xff
        if reg1 == "100":
            temp = r4[0]
            r4[0] = input()
            if r4[0].isdigit():
                r4[0] = int(r4[0])
            else:
                r4[0] = temp
            if r4[0] > 0xff:
                r4[0] = 0xff
        if reg1 == "101":
            temp = r5[0]
            r5[0] = input()
            if r5[0].isdigit():
                r5[0] = int(r5[0])
            else:
                r5[0] = temp
            if r5[0] > 0xff:
                r5[0] = 0xff


    if opcode == "110": # Print Instructions ------------------------------------------------
        if reg1 == "000":
            print(r0[0])
        if reg1 == "001":
            print(r1[0])
        if reg1 == "010":
            print(r2[0])
        if reg1 == "011":
            print(r3[0])
        if reg1 == "100":
            print(r4[0])
        if reg1 == "101":
            print(r5[0])


    if (opcode == "111") and (address_flag == 0): # Jump Instructions ----------------------
        if reg1 == "000":
            if reg2 == "000":
                if r0[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r0[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r0[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r0[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r0[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r0[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
        if reg1 == "001":
            if reg2 == "000":
                if r1[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r1[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r1[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r1[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r1[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r1[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
        if reg1 == "010":
            if reg2 == "000":
                if r2[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r2[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r2[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r2[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r2[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r2[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
        if reg1 == "011":
            if reg2 == "000":
                if r3[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r3[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r3[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r3[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r3[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r3[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
        if reg1 == "100":
            if reg2 == "000":
                if r4[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r4[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r4[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r4[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r4[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r4[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
        if reg1 == "101":
            if reg2 == "000":
                if r5[0] != r0[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "001":
                if r5[0] != r1[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "010":
                if r5[0] != r2[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "011":
                if r5[0] != r3[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "100":
                if r5[0] != r4[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break
            if reg2 == "101":
                if r5[0] != r5[0]:
                    r7[0] = r6[0]
                else:
                    r7[0] = 0xffff
                    break

    # PRINTS FOR TESTING
    #print("r0: " + str(r0))
    #print("r1: " + str(r1))
    #print("r2: " + str(r2))
    #print("r3: " + str(r3))
    #print("r4: " + str(r4))
    #print("r5: " + str(r5))
    #print("r6: " + str(r6))
    #print("r7: " + str(r7))
    #print("ds: " + str(data_segment))

    flagvals = '' # dec to bin vals
    for x in flag_register:
        flagvals = flagvals + str(x)

    f = open("sim_cpu.rpt")
    if f.readline() == "":
        f.close()
        f = open("sim_cpu.rpt", "a")
        f.write("== Register Outputs ==\n")
    f.close()
    f = open("sim_cpu.rpt", "a")
    regout = "r0: [{0}] | r1: [{1}] | r2: [{2}] | r3: [{3}] | r4: [{4}] | r5: [{5}]\n" + "Loop Register (r6): [{6}]\n" + "Instruction Pointer (r7): [{7}]\n" + "Flag Register: [{8}]\n" + "===\n"
    regout = regout.format(r0[0], r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], flagvals)
    f.write(regout)
    f.close()

    r7[0] += 1

if r7[0] == 0xffff:
    sys.exit("== End of program reached ==")