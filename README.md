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

The Python3, m4 and PHP versions are conceptually similar to
my [Go self-replicating program](https://github.com/bediger4000/Self-replicating-go/)
in that they all use a formatting string as an argument to formatting.
The specifics of this are peculiar to each language,
but are reminiscent of Combinatory Logic's `M M` term.

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
[m4 macro language notes](https://mbreen.com/m4.html)
