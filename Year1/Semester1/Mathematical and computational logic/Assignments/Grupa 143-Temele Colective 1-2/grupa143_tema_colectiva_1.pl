%Notez cu U,^,\,/\ reuniunea, intersectia, diferenta si diferenta
% simetrica a doua multimi, respectiv, cu <=,<,>=,> incluziunea
% nestricta, incluziunea stricta, incluziunea nestricta de sens
% contrar si incluziunea stricta de sens contrar intre doua multimi,
% respectiv, iar cu @ multimea vida.

difer(A,B) :- A, not(B).
implica(A,B) :- not(A);B.
echiv(A,B) :- implica(A,B), implica(B,A).
inclusstrict(A,B) :- implica(A,B), not(echiv(A,B)).
difsim(A,B) :- difer(A,B);difer(B,A).

%1.@\A=@
propr1 :- not((member(A,[true,false]), write(A), nl, not(echiv(difer(false,A),false)))).


%2.A/\@=A
propr2 :- not((member(A,[true,false]), write(A), nl, not(echiv(difsim(A,false),A)))).


%3.A/\B=@ <=> A=B
ms3(A,B) :- echiv(difsim(A,B),false).
md3(A,B) :- echiv(A,B).
propr3 :- not((member(A,[true,false]), member(B,[true,false]), write((A,B)), nl, not(echiv(ms3(A,B),md3(A,B))))).


%4.A<=B<C => A<C
ms4(A,B,C) :- implica(A,B), inclusstrict(B,C).
propr4 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(implica(ms4(A,B,C),implica(A,C))))).


%5.A<B<C => A<C
ms5(A,B,C) :- implica(A,B), implica(B,C).
propr5 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(implica(ms5(A,B,C),implica(A,C))))).


%6.A<=B => A^C<=B^C
propr6 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(implica(implica(A,B),implica((A,C),(B,C)))))).


%7.A<=B => A\C<=B\C
propr7 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(implica(implica(A,B),implica(difer(A,C),difer(B,C)))))).


%8.(A<=B si C<=D) => AUC<=BUD
ms8(A,B,C,D) :- implica(A,B),implica(C,D).
md8(A,B,C,D) :- implica((A;C),(B;D)).
propr8 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]),member(D,[true,false]), write((A,B,C,D)), nl,not(implica(ms8(A,B,C,D),md8(A,B,C,D))))).


%9 (A<=B si C<=D) => A^C<=B^D
ms9(A,B,C,D) :- implica(A,B),implica(C,D).
md9(A,B,C,D) :- implica((A,C),(B,D)).
propr9 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]),member(D,[true,false]), write((A,B,C,D)), nl,not(implica(ms9(A,B,C,D),md9(A,B,C,D))))).


%10 (A<=B si C<=D) => A\D<=B\C
ms10(A,B,C,D) :- implica(A,B),implica(C,D).
md10(A,B,C,D) :- implica(difer(A,D),difer(B,C)).
propr10 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]),member(D,[true,false]), write((A,B,C,D)), nl,not(implica(ms10(A,B,C,D),md10(A,B,C,D))))).


%11 (A<=C si B<=C) <=> AUB<=C
ms11(A,B,C) :- implica(A,C),implica(B,C).
md11(A,B,C) :- implica((A;B),C).
propr11 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(echiv(ms11(A,B,C),md11(A,B,C))))).


%12 (A<=B si A<=C) <=> A<=B^C
ms12(A,B,C) :- implica(A,B),implica(A,C).
md12(A,B,C) :- implica(A,(B,C)).
propr12 :- not((member(A,[true,false]), member(B,[true,false]), member(C,[true,false]), write((A,B,C)), nl, not(echiv(ms12(A,B,C),md12(A,B,C))))).


%13 A^(A\B)=A\B
propr13 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv((A,(difer(A,B))),difer(A,B))))).


%14 A^(B\A)=@
propr14 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv((A,(difer(B,A))),false)))).


%15 A\B=A\(A^B)
propr15 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(difer(A,B),(difer(A,(A,B))))))).


%16 A/\B=(AUB)\(A^B)
ms16(A,B) :- difsim(A,B).
md16(A,B) :- difer((A;B),(A,B)).
propr16 :-  not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(ms16(A,B),md16(A,B))))).


%pentru orice parte M a lui T, notam cu M' complementara lui M fata de T: M'=T\M,
%care este o parte a lui T

%17 a doua lege a lui De Morgan: (A^B)'=A'UB'
ms17(A,B) :- not((A,B)).
md17(A,B) :- not(A);not(B).
propr17 :-  not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(ms17(A,B),md17(A,B))))).


%18 A<=B <=> B'<=A'
ms18(A,B) :- implica(A,B).
md18(A,B) :- implica(not(B),not(A)).
propr18 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(ms18(A,B),md18(A,B))))).


%19 A=B <=> A'=B'
ms19(A,B) :- echiv(A,B).
md19(A,B) :- echiv(not(B),not(A)).
propr19 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(ms19(A,B),md19(A,B))))).


%20 A<B <=> B'<A'
ms20(A,B) :- inclusstrict(A,B).
md20(A,B) :- inclusstrict(not(B),not(A)).
propr20 :- not((member(A,[true,false]), member(B,[true,false]),write((A,B)), nl, not(echiv(ms20(A,B),md20(A,B))))).


%21 A^A'=@
md21(A) :- A,(not(A)).
propr21 :- not((member(A,[true,false]),write(A), nl, not(echiv(md21(A),false)))).

%Luam un T a.i. T<=A si T<=B ==> T =true
%
%22 AUA'=T
propr22:- not((member(A,[true,false]),write((A)),nl,not(echiv((A;not(A)),true)))).

%23 A^B=@ <=> A<=B'
ms23(A,B) :- echiv((A,B),false).
md23(A,B) :- implica(A,(not(B))).
propr23:- not((member(A,[true,false]),member(B,[true,false]),write((A,B)),nl,not(echiv(ms23(A,B),md23(A,B))))).

%24 AUB=T <=> A>=B'
ms24(A,B) :- echiv((A;B),true).
md24(A,B) :- implica(not(B),A).
propr24:- not((member(A,[true,false]),member(B,[true,false]),write((A,B)),nl,not(echiv(ms24(A,B),md24(A,B))))).

%25 (A^B=@ si AUB=T) <=> A=B'
ms25(A,B) :- echiv((A,B),false),echiv((A;B),true).
md25(A,B) :- echiv(A,not(B)).
propr25:- not((member(A,[true,false]),member(B,[true,false]),write((A,B)),nl,not(echiv(ms25(A,B),md25(A,B))))).










