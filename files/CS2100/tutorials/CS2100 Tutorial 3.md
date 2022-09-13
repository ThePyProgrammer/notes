# CS2100 Tutorial 3

## D1
Given two integer arrays *A* and *B* with unknown number of elements, and their base addresses stored in registers **`$s0`** and **`$s1`** respectively, study the MIPS code below. Note that an integer takes up 32 bits of memory.
```assembly
	  addi $t0, $s0, 0
	  addi $t1, $s1, 0
loop: lw $t3, 0($t0) 
      lw $t4, 0($t1)
      slt $t5, $t4, $t3 # line A 
      beq $t5, $zero, skip # line B
      sw $t4, 0($t0) 
      sw $t3, 0($t1) 
skip: addi $t0, $t0, 4
	  addi $t1, $t1, 4
	  bne $t3, $zero, loop
```
```ad-question
title: What is the purpose of register **`$t1`** in this code?

It functions as a moving pointer that is traverting through array B.
```
```ad-question
title: If `A = {7, 4, 1, 6, 0, 5, 9, 0}` and `B = {3, 4, 5, 2, 1, 0, 0, 9}`, give the final content of the two arrays? How many `sw` operations are run?


Let's go by this step-by-step. `$t0` and `$t1` stores the pointers to the array index, initally set at the first value of each array. The `lw` operation dereferences said pointers to get the values. Hence initially, we have that:
- `$t3` = 7
- `$t4` = 3

When the `slt` operation is run, `$t5` now stores a 1 (since `$t4 < $t3`).

Thus, it does not loop out and instead continues through the `sw` operations, so only the first elements, and only 2 `sw` operations are run.
```
```ad-question
title: What is the value (in decimal) of the immediate field in the machine code representation of the **bne** instruction?


```

## Q1
Below is a C code that performs palindrome checking. A palindrome is a sequence of characters that reads the same backward and forward. For example, “madam” and “rotator” are palindromes.
```c
char string[size] = { ... }; // some string
int low, high, matched;
// Translate to MIPS from this point onwards
low = 0;
high = size-1;
matched = 1; // assume this is a palindrome
// In C, 1 means true and 0 means false
while ((low < high) && matched) {
	if (string[low] != string[high])
		matched = 0; // found a mismatch
	else {
		low++;
		high--;
	}
}
// "matched" = 1 (palindrome) or 0 (not palindrome)
```

Let the following variable mapping be in order:
|Variable|Register|
|---|---|
|`low`|`$s0`|
|`high`|`$s1`|
|`matched`|`$s3`|
|base adress of `string[]`|`$s4`|
|`size`|`$s5`|

`````ad-hint
title: Translate the C code into MIPS code by keeping track of the indices.

**My Solution**
```mips
	addi $s0, $zero, 0
	addi $s1, $s5, -1
	addi $s3, $zero, 1
if: slt $t0, $s0, $s1
	and $t1, $t0, $s3
	beq $t1, $zero, fi
	add $t2, $s4, $s0
	lb $t3, 0($t2)
	add $t2, $s4, $s1
	lb $t4, 0($t2)
	addi $s0, $s0, 1
	addi $s1, $s1, -1
	beq $t3, $t4, if
fi: 
```

**Suggested Solution (More Optimized)**
```py
	addi $s0, $zero, 0 # low = 0
	addi $s1, $s5, -1 # high = size-1
	addi $s3, $zero, 1 # matched = 1
if: slt $t0, $s0, $s1 # (low < high)?
	beq $t0, $zero, fi # exit if (low >= high)
	beq $s3, $zero, fi # exit if matched == 0
	add $t1, $s4, $s0 # find address of low character
	lb $t2, 0($t1) # take low character
	add $t3, $s4, $s1
	lb $t4, 0($t3)
	beq $t2, $t4, el
	addi $s3, $zero, 0
	J    eW
el: addi $s0, $s0, 1
	addi $s1, $s1, -1
eW: j loop
fi: 
```
`````

`````ad-hint
title: Translate the C code into MIPS code by using the idea of "array pointer".

```c
char string[size] = { ... }; // some string
int *low, *high;
int matched;

// Translate into MIPS from this point onwards
*low = string;
*high = &(string[size-1]);
int matched = 1;

while((low < high) && matched) {
	if(*low != *high) matched = 0;
	else {
		low++;
		high--;
	}
}
```

So we gotta translate that. Good.

```assembly
	add $t0, $s5, $zero # Low
	add $t1, $s1, $zero
	addi $s1, $s5

```
`````

## Q3
### 2a

`````ad-note
title: `addi $s1, $zero, 0`

|`addi`|`$s1`|`$zero`|`0`|
|---|---|---|---|
|`0x8`|17|0|0|
|001000|10001|00000|0000000000000000|
|`opcode`|`rt`|`rs`|`imm`|

Therefore, it is:
```python
0b00100000000100010000000000000000 = 0x20110000
```

`````
`````ad-note
title: `0x11000002`

```
0x11000002 = 0001 0001 0000 0000 0000 0000 0000 0010 in binary
= 000100 01000 00000 0000000000000010
```

|opcode|rs|rt|imm|
|---|---|---|---|
|000100|01000|00000|10|
|`0x4`|`0x8`|`0x0`|`0x2`|
|`beq`|`$t0`|`$zero`|`exit` (2 lines from next line)|

Therefore, the instruction is:
```python
beq $t0, $zero, exit
```
`````

`````ad-note
title: `0x22310001`

```
0x22310001 = 0010 0010 0011 0001 0000 0000 0000 0001
= 001000 10001 10001 (1 in 16 bits)
```

|opcode|rs|rt|imm|
|---|---|---|---|
|`8`|`17`|`17`|`1`|
|`addi`|`$s1`|`$s1`|1|

Therefore the instruction is:
```python
addi $s1, $s1, 1
```
`````

`````ad-note
title: `j loop`

|`j`|`loop`|
|---|------|
|0x2|0x00400028+0x4 = 0x0040002C|
|000010|~~0000~~ 0000 0100 0000 0000 0000 0010 11~~00~~|
|000010|0000 0100 0000 0000 0000 0010 11|

There the instruction is:
```py
0b0000 1000 0001 0000 0000 0000 0000 1011 = 0x0810000B
```
`````

### Final Code Table
|Instruction Encoding|MIPS Code|
|---|---|
||`# $s1 stores the result, $t0 stores a non-negative number`|
|`0x20110000`|`addi $s1, $zero, 0`|
|`0x00084042`|`loop: srl $t0, $t0, 1`|
|`0x11000002`|`beq $t0, $zero, exit`|
|`0x22310001`|`addi $s1, $s1, 1`|
|`0x0810000B`|`j loop`|
||`exit:`|



