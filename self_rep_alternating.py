#!/usr/bin/env python
COMMA=','; DQUOTE='"'; SQUOTE="'"; SEMICOLON=';'; SHEBANG='#!/usr/bin/env python'
G2='print B; print "COMMA="+S+C+S+E, "DQUOTE="+S+D+S+E, "SQUOTE="+D+S+D+E, "SEMICOLON="+S+E+S+E, "SHEBANG="+S+B+S; print "G2="+S+G2+S; print "G1="+S+G1+S; print G1'
G1='print SHEBANG; print "S="+DQUOTE+SQUOTE+DQUOTE+SEMICOLON, "D="+SQUOTE+DQUOTE+SQUOTE+SEMICOLON, "E="+SQUOTE+SEMICOLON+SQUOTE+SEMICOLON, "C="+SQUOTE+COMMA+SQUOTE+SEMICOLON, "B="+SQUOTE+SHEBANG+SQUOTE; print "G1="+SQUOTE+G1+SQUOTE; print "G2="+SQUOTE+G2+SQUOTE; print G2'
print SHEBANG; print "S="+DQUOTE+SQUOTE+DQUOTE+SEMICOLON, "D="+SQUOTE+DQUOTE+SQUOTE+SEMICOLON, "E="+SQUOTE+SEMICOLON+SQUOTE+SEMICOLON, "C="+SQUOTE+COMMA+SQUOTE+SEMICOLON, "B="+SQUOTE+SHEBANG+SQUOTE; print "G1="+SQUOTE+G1+SQUOTE; print "G2="+SQUOTE+G2+SQUOTE; print G2