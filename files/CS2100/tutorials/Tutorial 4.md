# Tutorial 4
(oops)

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
|(b)|`$s2`<br>`100($zero)`|||
|(c)|`$t4`<br>`40($s2)`|||

