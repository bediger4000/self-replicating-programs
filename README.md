# self-replicating-programs
## A number of self replicating programs

* [PHP](q2.php), probably v5.x on into v8.0.2
* `self_replicating.py` - Python 2.x
* `self_rep_alternating.py` - Python 2.x, alternates generations
* `replicate.html` - JavaScript and HTML, replicates in a browser. [Try it!](https://bediger4000.github.io/replicate.html)
* `triplet` - Perl, Bash, Python 2.x and PHP quine relay/ouroboros program. Execute `run_replication` to try it out.
* [Shell script](replicate), Bash, probably ksh. Changes just a little with each reproduction.
* [Python 3.x "f" strings](fstrings.py)

The Python3 and PHP versions are conceptually similar to
my [Go self-replicating program](https://github.com/bediger4000/Self-replicating-go/)
in that they both use a formatting string as an argument to formatting.
The specifics of this are peculiar to each language,
but are reminiscent of Combinatory Logic's `M M` term.
