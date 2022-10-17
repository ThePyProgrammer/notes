# Tutorial 4
(oops)

### Question 1
Given below are the contents of some registers and memory locations, where `mem(A)` refers to the data word stored in the memory location at address `A`: 
|Register|Memory Location|Data|
|---|---|---|
|`$s0`|100|mem (100) = 1000|
|`$s1`|160|mem (160) = 1600|
|`$s2`|200|mem (200) = 2000|
|`$s3`|240|mem (240) = 2400|
|`$s4`|300|mem (300) = 3000|
|`$t0`|10000|mem (10000) = 100|
|`$t1`|15000|mem (15000) = 150|
|`$t2`|20000|mem (20000) = 200|
|`$t3`|25000|mem (25000) = 250|
|`$t4`|30000|mem (30000) = 300|

For each of the MIPS instructions below, ‘op’ is an unknown opcode, which is not of our concern here. For each of the data operands in the instruction, if the format is legal, give its memory address (if applicable) and the content inside. Note that `$s0`-`$s4`, `$t1`-`$t4` are symbolic register names, `$zero` is register 0 with content zero inside, and only the three addressing modes (register, immediate, and displacement) mentioned in class are considered as legal.

<ol  type = "A">
<li><pre><code>op $t1, $t2</code></pre></li>
<li><code>op $s2, 100($zero)</code></li>
<li><code>op $t4, 40($s2)</code></li>
<li><code>op $s3, 200($zero)</code></li>
<li><code>op $t3, $zero($t1)</code></li>
<li><code>op $s1, 140($s1)</code></li>
</ol>

The answers for (a) have been done for you.

|Q|Operand|Target Memory Address|Content|
|---|---|---|---|
|(a)|`$t1`<br>`$t2`|Not Applicable<br>Not Applicable|15000<br>20000|
|(b)|`$s2`<br>`100($zero)`|Not Applicable<br>`100`|`200`<br>`1000`|
|(c)|`$t4`<br>`40($s2)`|Not Applicable<br>`240`|`30000`<br>`2400`|
|(d)|`$s3`<br>`200($zero)`|Not Applicable<br>`200`|`240`<br>`2000`|
|(e)|`$t3`<br>`$zero($t1)`|Not Applicable<br>**Illegal**|`25000`<br>**Illegal**|
|(f)|`$s1`<br>`140($s1)`|Not Applicable<br>`300`|`160`<br>`3000`|

basically `n($...)` is getting the memory added by that number, `n`.

<hr>

### Question 2

|ISA|Instructions|
|---|---|
|Stack|`push @src` - Loads value to top of stack<br>`pop @dest` - Transfers value at the top out<br>`add` - pop top 2, add them, push sum|
|Accumulator|`load @src` - Loads value into accumulator<br>`add @src` - Adds value to accumulator<br>`store @dest` - Stores value in accumulator|
|Memory-Memory|`add @dest, @src1, @src2` - Adds and stores automatically|
|Register-Register|`load $reg, @src` - loads value into `$reg`<br>`add $dest, $src1, $src2`|Adds values from registers and stores into `$dest`<br>`store $reg, @dest` - Stores value in `$reg`|

Task: Encode the following code in each architecture
```python
a0 = a1 + a2;
a1 = a0 + a2;
a2 = a0 + a1;
```

#### Stack
```python
push @a1
push @a2
add
pop @a0

push @a0
push @a2
add
pop @a1

push @a0
push @a1
add
pop @a2
```

#### Accumulator
```python
load @a1
add @a2
store @a0
add @a2
store @a1
add @a0
store @a2
```

#### Memory-Memory
```python
add @a0, @a1, @a2
add @a1, @a0, @a2
add @a2, @a0, @a1
```

#### Register-Register
```python
load $r1, @a1
load $r2, @a2
add $r0, $r1, $r2
store $r0, @a0

add $r1, $r0, $r2
store $r1, @a1

add $r2, $r0, $r1
store $r2, @a2
```

<hr>

### Question 3
#### Part(a)


### Question 4
#### Part (a)


## In-Class
### Harder Qn

You are designing a machine with 16-bit fixed-length instructions containing only 12 registers and 126 byte addressable memory. You will need to have three kinds of instructions with the following operands:
- **Type A**: one address and one register
- **Type B**: one address
- **Type C**: two registers

Assume that all instruction types exist and all bits are utilised.


Notes:
- Registers can be represented with 4 bits
- Addresses can be represented by 7 bits

For **Type A**: 5 Bit Opcode
For **Type B**: 9 Bit Opcode
For **Type-C**: 8 Bit Opcode

#### Minimum
We must minimize **B** and **C**.
|Type|First 5|Next 3|Last|Number of Ways|
|---|---|---|---|---|
|A|**00001 to 11111**|||31|
|B|00000|000|**0 to 1**|2|
|C|00000|**001 to 111**||7|

#### Maximum

|Type|First 5|Next 3|Last|Number of Ways|
|---|---|---|---|---|
|A|**00001 to 11111**|||31|
|B|00000|000|**0 to 1**|2|
|C|00000|**001 to 111**||7|
