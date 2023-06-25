# self-replicating-programs
## A number of self replicating programs (quines)

* [PHP](q2.php), probably v5.x on into v8.0.2
* `self_replicating.py` - Python 2.x
* `self_rep_alternating.py` - Python 2.x, alternates generations
* `replicate.html` - JavaScript and HTML, replicates in a browser. [Try it!](https://bediger4000.github.io/replicate.html)
* `triplet` - Perl, Bash, Python 2.x and PHP quine relay/ouroboros program. Execute `run_replication` to try it out.
* [Shell script](replicate), Bash, probably ksh. Changes just a little with each reproduction.
* [Python 3.x "f" strings](fstrings.py)
* [GNU m4 macro](r1.m4)
* [awk](r.awk)
* [GPP](r.gpp)

The Python3, m4, awk and PHP versions are conceptually similar to
my [Go self-replicating program](https://github.com/bediger4000/Self-replicating-go/)
in that they all use a formatting string as an argument to formatting.
The specifics of this are peculiar to each language,
but are reminiscent of Combinatory Logic's `M M` term.

You have to run the self-replicating `awk` program like this:

```
$ awk -f r.awk
```

The `m4` macro processor self-replicator is of interest.
First, `m4` input doesn't have a way to escape characters in its input.
Second, `m4` quoted strings use matched pairs of "grave accents" (\`) (ASCII 0x27)
and single quotes (\') (ASCII 0x2c),
allowing embedding quoted strings in quoted strings.
Between allowing quoted strings in quoted strings,
and the `defn` built-in,
it's not too hard to write a self-replicating `m4` input.
Avoiding a trivial self replicator is the hard part.
Any input that does not define and use a macro
will cause `m4` to produce output identical to its input.
Using the `defn` builtin,
which doesn't technically violate the rules of writing quines,
seems roughly equivalent to those programs that open the
file of their own source and write it out.

[m4 macro language notes](https://mbreen.com/m4.html)

I found writing a quine in
[GPP](https://logological.org/gpp) (and [here](https://arxiv.org/abs/2008.00840v1)),
the Generic Preprocessor,
terrifically difficult.

Default user macros make it impossible to interpolate strings in macro bodies
and in outputs without also having whitespace.
Bash can interpolate variables like this: `some${variable}text`,
using curly braces to lexically mark the variable. Default GPP doesn't have that.

Default string format, and macro expansion inside strings make it
easy to write infinitely-expanding macros
In contrast, Python has `'`, `"` and `"""` delimiters for strings,
Bash, PHP and Perl have `"` and `'`, Go has `"` and `.
In all of these languages, one mode of delimiting strings allows
variable interpolation, and one mode does not allow it.

I used GPP's "meta macros" to change macro definition and macro expansion
rules part way through the quine to overcome these difficulties.
