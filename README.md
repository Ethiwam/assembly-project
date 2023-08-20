# Designing an Instruction Set Architecture
The programs in this repo were originally for the Instruction Set Architecture project for Dr. Benjamin Schaefer's computer architecture course at University of Texas at Dallas. All files created by Ethan Iwama.

There are three components in this project:
1. avg8.asm
    - A program written in my assembly language
3. assembler.py
    - A program that assembles code written in my assembly language
4. hardware.py
    - A program simulating the processor my language is designed for

## avg8.asm
The assembly program, avg8.asm, takes the moving average of the last 8 unsigned 8-bit integers in
memory. It accepts user values, stores them in memory, and takes the average of the last 8 integers
stored. Upon first starting the program, memory addresses 0-7 are filled with zeros and are used with
the first user input to create the first average. From there user values will continue being put into
the data segment, averages will continue being made, until the end of data segment has been reached or
the user exits the program.

There is no help section in the program itself. No text to explain the program. The moment you start
the program, the only thing you can do is input a number. When a number is input, an output is spit
out without any flavor text. So the the only thing that appears in the terminal is user values
alternating with average values. Only numbers.

## assembler.py
The assembler program, assembler.py, is a Python program that takes in an assembly file and outputs
the machine code in a text file. It can only translate assembly files written in my 16-bit assembly
language. When executing the file, it will ask the user to input a filename. This can be tested by
simply inputting "avg8.asm" while the avg8 program is in the same directory.

The assembler program will output the binary file (labeled "bnry.txt") in the same directory that the
program is stored. To execute the binary, just execute the cpu simulator labeled "hardware.py".
This is a cpu simulator written in Python that inputs binary as a text file and executes the program
written in my assembly language. There is no need to enter a filename for hardware.py, it will read
the file named "bnry.txt" when it's in the same directory.

## hardware.py
The cpu simulator will execute the assembly program and also output a report file named "cpu_sim.rpt".
This report file records the status of every register in the system after every instruction is
executed. The processor I developed uses 9 registers total: general purpose r0-r5, loop address
storage r6, instruction pointer r7, and an unnamed flag register. Each register's value will be output
in the report file after each instruction in the assembly program is executed. The values are all
the decimal values stored within the registers, except for the flag register which will output the
binary value of the register.

Also enclosed in this zip file is a text file called "__ProjectNotes.txt" which can explain how my
assembly language works, as well as a powerpoint that gives an overview of the project.

Thank you for reading, I hope you end up satisfied with these programs.
