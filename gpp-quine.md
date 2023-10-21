# GPP Quine

[GPP](https://logological.org/gpp)
is the General Purpose Preprocessor,
a [macro preprocessor](https://en.wikipedia.org/wiki/General-purpose_macro_processor)
for various forms of structured and unstructured text.

I wrote what I believe to be the first non-vacuous self-replicating program in the GPP language.

`gpp` copies its input to its output,
making almost any text file into a quine (self-replicating program).
That's vacuous in the mathematical sense.
A non-vacuous quine would produce output via macro invocation.

Here's my non-vacuous quine:
```
#mode preservelf off
#define S '
#define H #
#define D $
#mode user "$" "$" "(" "," ")" "(" ")" "#" ""
#mode string qqq "'" "'"
#define g '$H$mode preservelf off
$H$define S $S$
$H$define H $H$
$H$define D $D$
$H$mode user "$" "$" "(" "," ")" "(" ")" "$H$" ""
$H$mode string qqq "$S$" "$S$"
$H$define g $S$#1$S$
$H$defeval quine $D$g$D$
$D$quine($D$g$D$)'
#defeval quine $g$
$quine($g$)
```

The above program does create output via a function call ("macro evaluation"),
so it's not merely using `gpp`-the-program to copy itself from input to output.
It's not 100% correct, because `gpp`-the-program has a bug in the `preservelf` mode:
`#mode` lines in `gpp` input show up as blank lines in the output.

Conceptually, this is just as easy as any other quine.
And by _easy_, I mean twisted and headache-inducing.
This quine has a string (set with `#define g` above) that can be used
as both an output specification, and an input.
For a macro-preprocessor like `gpp`, an "output specification"
means the evaluated body of a macro.
`gpp`-the-program evaluate the macro and puts the result of that evaluation
on its output.
The string `g` gets used to make a function ("define a macro"),
and finally gets used as a formal argument to the macro.
In that sense, this quine is the same as `M M` in 
[Combinatory Logic](https://plato.stanford.edu/entries/logic-combinatory/):
a replicator applied to itself.
Ah yes, conceptually quite easy.

The difficulty in writing a quine which executes `gpp` macro definitions
revolves around interpolating strings of characters
inside other strings of characters to produce a new string of characters.

Default `gpp` interpolation notation ends up requiring white space
Here's a small `gpp` input:

```
#define IN some string
interpolation between this IN and this
but there's no interpolation between thisINand this
```

The output looks like this:
```
interpolation between this some string and this
but there's no interpolation between thisINand this
```

The `IN` macro ("some string") gets interpolated in the first input line
because `IN` has a space character before and after.
The `IN` macro does not get interpolated in the second input line
because `thisINand` has no space before and after the "IN" substring.

For a counter-example, Linux shell scripts can interpolate strings like this:

```
IN='a lengthy substring'
echo output between this $IN and this
echo and there is interpolation between this${IN}and this
```

The Linux [bash shell](https://www.gnu.org/software/bash/)
uses '$' to distinguish between "the value of variable IN" and "assign a string to the variable named IN".
`bash` scripts can interpolate strings using `$IN` if there's surrounding white space,
and interpolate `${IN}` if there's not surrounding whitespace.
In that situation, the curly brackets delimit the variable name.
Excuting the 3-line shell script above yields this:

```
output between this a lengthy substring and this
and there is interpolation between thisa lengthy substringand this
```

A clever programmer can interpolate a string without whitespace delimiting a variable name.

---

The second problem with writing `gpp` quines is that `gpp` does not
by default
have a way to escape a character in a string.
It's not possible to include a double quote (ASCII 0x22) inside a double quoted string.

Other programming languages, have different solutions to this situation,
which arises more often than anyone would like.

Characters in the C programming language string literals can be "escaped" with backslashes:

```
"include a double quote \" in a C string literal"
```
[Python](https://www.python.org/) has quoted string literals that require escaping 
certain characters to keep them in the literal,
and triple-quoted string interals that don't require escaping:

```
"""include a double quote " in a Python string literal"""
```

[Go](https://go.dev/) has double-quoted strings, backslashes for escaping the next character,
and back-quoted ("grave accent") string literals that
contain every character between delimiters.

The [m4 preprocessor](https://www.gnu.org/software/m4/) uses grave accent characters to start a string literal,
and single quote to end a string literal,
so it allows nested string literals.
`m4` does not have single-character escaping.
It does have the `defn` built-in,
which can be used to write a quine,
but is not required.

---

I speculate that the combination of these two features mean that a quine in
the default `gpp` syntax is impossible.
If true, that would mean that default `gpp` syntax isn't turing complete,
some outputs are impossible.
That implication makes me distrust my speculation.

You can use the default mode syntax and the `#1`, `#2` macro formal argument
convention to interpolate substrings.
It's just very tricky.
This may be the key to a default syntax `gpp` self-replicating program.
I couldn't get it to work.

---

`gpp` does have the interesting feature of "meta-macros",
instructions to a running `gpp` process that allow a `gpp` program to re-define
the syntax of macro definition,
string delimiters, and whether or not string interpolation can take place.
I had to use meta-macros to write a working quine.

## Detailed Explanation

```
  1 #mode preservelf off
  2 #define S '
  3 #define H #
  4 #define D $
  5 #mode user "$" "$" "(" "," ")" "(" ")" "#" ""
  6 #mode string qqq "'" "'"
  7 #define g '$H$mode preservelf off
  8 $H$define S $S$
  9 $H$define H $H$
 10 $H$define D $D$
 11 $H$mode user "$" "$" "(" "," ")" "(" ")" "$H$" ""
 12 $H$mode string qqq "$S$" "$S$"
 13 $H$define g $S$#1$S$
 14 $H$defeval quine $D$g$D$
 15 $D$quine($D$g$D$)'
 16 #defeval quine $g$
 17 $quine($g$)
```

*Line 1:* should cause `gpp`-the-program to not print empty lines in output
where corresponding input line is a meta-macro.
There's a bug in `gpp` code that prevents this from working,
so my putative quine actually has three blank lines more than
the input has, due to the presence of three `#mode` statements.


*Line 2, 3, 4:*  defines three macros. Further appearances of S, H, D as macros in evaluated input
will be replaced by single-quote, hash (octothorpe) or dollar sign respectively.

*Line 5:* use the `mode user` meta-macro to redefine how subsequent input text gets treated.
This particular piece of gibberish means:

* macros start with a '$' character
* macros without arguments end with a '$' character
* arguments to macros have a '(' to begin with
* arguments to macros are separated by ',' characters
* arguments to macros end with a ')'
* stack '#' characters for argument balancing, I don't know what this means.

`mode user` only changes user macro syntax, not meta-macro syntax.

*Line 6:* use the `mode string` meta-macro to make strings start and end with single-quote "'" character.
The "qqq" is actually 3 'q' indicators, each of which means "output strings without delimiters".

1. First 'q' means inside meta-macro calls 
2. Second 'q' means inside user macro calls. I think this is the only one that makes a difference
to my quine code.
3. Third 'q' means outside of any macro call

*Lines 7 - 15:* make `g` a macro, that, when invoked, is a big string.
This string has substrings like `$H$`, `$D$`, which because of line 5,
and whichever of lines 2-4,
could under some circumstances cause `gpp` to interpolate a hash, a dollar sign,
or a single-quote.
The interpolation will happen later, the `g` macro invoked alone, will output what's literally between single-quotes
without any substring interpolation.
`g` acts like a variable in imperative languages.

*Line 16:* Here's a trick. Use the `#defeval` meta-macro to create a new macro named `quine`
with the **value** of `g` as the body of the macro.
Line 5 changed how `gpp`-the-program parses input text to recognize when a macro should get called.
The `$g$` is the value of `g`, set on lines 7-15. No arguments.
`#defeval` also "evaluates" the raw string `$g$`.
That raw string is full of `$D$`, `$H$`, etc, places where `gpp`-the-program
will do some macro evaluation and interpolate the results.


*Line 17:* `$quine($g$)`: call the macro named  `quine`, created by the `defeval` of line 16,
with the string, the value of macro `g`, created on lines 7-15, as the only formal argument.
The macro invocation puts the text of the original quine on `gpp` output,
plus 3 blank lines due to the `preservelf` bug.

Lines 7-15 created a quoted string, single quotes begin and end the string,
as the `mode string` meta-macro specified.
The `mode string` meta-macro of line 6 also sets "qqq",
which causes the `$quine($g$)` macro call to output an *unquoted* string.

Lines 7-15 also echo the structure of the whole quine,
except with special characters to be interpolated.

```
  1 #mode preservelf off
  2 #define S '
  3 #define H #
  4 #define D $
...
  7 #define g '$H$mode preservelf off
  8 $H$define S $S$
  9 $H$define H $H$
 10 $H$define D $D$
...
```

Line 7 outputs (a copy of) line 1 when `$H$` has the H macro interpolated.
Line 8 outputs (a copy of) line 2, line 9 outputs line 3, line 10 outputs line 4,
and so forth.

Line 13 is important: `$H$define g $S$#1$S$`

The `defeval` will make this into: `#define g '#1'` as part of a macro body.

`#1` is where `gpp`-the-program will interpolate the first formal argument to any invocations
of the macro named `quine`.
When line 17, `$quine($g$)` gets evaluated, The `#1` turns into lines 7-15

## How I figured this out

I've written a [number of quines](https://github.com/bediger4000/self-replicating-programs)
over the years.
My shell script quines on [this page](https://www.nyx.net/~gthompso/self_sh.txt)
date to no later than 1992, which is about when I lost access to rtgds1.den.mmc.com,
a Sun 3 workstation.
I wrote one of those shell script quines circa 1988, when I bought an AT&T 3b1
running System VR3 unix, which had the slick new Korn Shell.

My usual process is implicit in my
[Go self-replicating program](https://github.com/bediger4000/Self-replicating-go/)
repo.
First, I figure out how to create a "format" string with a single "hole" for string interpolation,
which will later be filled by the format string.
Experience tells me that I need to figure out how to create strings with string-delimiter-characters
and maybe other metacharacters in them.
I also need to figure out how to use the format string with the format string as input,
as in Combinatory Logic's `M M`

I noodled around with `gpp` inputs to internalize knowledge of how to interpolate strings
into other strings, how macro calls work, and to internalize the format of macro definition
and invocation.
Ultimately, I realized that the default `gpp` syntax for macro invocation (surrounded by white space),
would not allow creating a "format" string with metacharacters in the right places.

I experimented with different methods of getting metacharacters
(mainly '#' and '\\' in default `gpp` syntax) interpolated into format strings.
I tried macro arguments, whose values get interpolated where `#1`, `#2` etc
appear in the macro body.
Getting a multi-line macro body was tricky in default `gpp` syntax.
I was having trouble understanding when macro evaluation occurred inside the
body of a macro.

After quite some experimentation,
I decided I couldn't do what I want in default `gpp` syntax.
I resorted to careful reading of the manual.
I discovered how to use `mode user` to change how a running `gpp` process
parses out macro invocation sites.
I discovered how to use `mode string` to output quoted strings,
which can be used to define multi-line macro bodies, without quote characters.
Finally, I realized that `defeval` could be used to interpolate metacharacters
into a macro body.

## Obvious further questions

I think the above work leads to an obvious questions:

Can a quine exist using only default `gpp` syntax, without meta-macros
redefining user macro invocation format?

I don't have the answer.
