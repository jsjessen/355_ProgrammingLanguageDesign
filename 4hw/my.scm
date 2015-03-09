#lang racket
; Language: R5RS 
; Linux/Unix

; James Jessen
; 10918967
; CptS 355 HW4

;Setup
;-----
;For Linux systems you can probably find a racket package in your distribution's package manager. After installing use the drracket command to start up the IDE. Be sure to select R5RS as the language on the language menu. You should only have to do this once after installing.

;Turning in your work
;--------------------
;Turn in the assignment by uploading your file to the ANGEL system. Turn in a text file containing legal Scheme code -- you should be able to take the contents of your file and run it through Racket without errors. Create your own test cases for each function: you may include the test cases in what you turn in.

;General rules
;-------------
;Unless directed otherwise, you should implement your functions using recursive definitions that you build up from the basic built-in functions such as CONS, CAR, CDR, LIST, etc. 

;Don't use set! and 
;Don't define anything except functions!

;(car list) returns the first element of list
;(cdr list) return list with its first element removed
;(length list) return the number of elements in list
;(append L1 L2 L3 ...) return a list with L1's elements followed by L2's elements followed by L3's....
;(reverse list) return a list with all of the elements in opposite order
;(memv list obj) Return the first sublist of list whose first element is obj
;(map + L1 L2) would return a list such that each element is the sum of the element at the same position in L1 L2 L3...
;                and 'add' can of course be replaced with any proc (argc required by proc must = # of lists)
;================================================================

;Assume that the index, n, is at least 0 and smaller than the length of the list. 

;;Return the nth element of a list (0-based indexing). 
(define (nth L n) 
    (cond ((= n 0) (car L))
        (else (nth (cdr L) (- n 1)))
    )
)

;Test nth
(cond
  ((equal?  (nth '(1 2 3 4) 1)  2) "nth: PASS")
  (else "nth: FAIL"))

;----------------------------------------------------------------
;(car list) returns the first element of list
;(cdr list) return list with its first element removed
;(length list) return the number of elements in list
;(append L1 L2 L3 ...) return a list with L1's elements followed by L2's elements followed by L3's....
;(reverse list) return a list with all of the elements in opposite order
;(memv list obj) Return the first sublist of list whose first element is obj
;(map + L1 L2) would return a list such that each element is the sum of the element at the same position in L1 L2 L3...
;                and 'add' can of course be replaced with any proc (argc required by proc must = # of lists)

;Assume that the index i is at least 0 and 
;smaller than the length of the list. 

;;Return a (new) list which is the same as L except that the ith element is v. 
(define (repl L i v) (i))

(display "*************** EVERYTHING BELOW THIS LINE IS JUNK ***************************\n")
;> (repl '(1 2 3 4) 1 7) 
;(1 7 3 4)

;Test repl
(cond
  ((equal?  (repl '(1 2 3 4) 1 7)  (1 7 3 4)) "repl: PASS")
  (else "repl: FAIL"))
;----------------------------------------------------------------

;Return a list of integers (min min+1 ... max-1). 
;If min ≥ max return the empty list. Example:

;;Act like the Python range function
(define (range min max) (+ min max))

;> (range 4 6)
;(4 5)

;Test range
(if 
  (equal? 
    (range 4 6) 
    (4 5)) 
  "range: PASS" 
  "range: FAIL")

;----------------------------------------------------------------

;Define a function merge2 that merges two lists of integers, each already in ascending order, into a new list that is also in ascending order. The length of the new list is the sum of the lengths of the original lists. 

(define (merge2 l1 l2) (+ l1 l2))

;> (merge2 '(2 4 6) '(1 4 5))
;(1 2 4 4 5 6)

;Test merge2
(if 
  (equal? 
    (merge2 '(2 4 6) '(1 4 5))
    (1 2 4 4 5 6))
  "merge2: PASS" 
  "merge2: FAIL")

;----------------------------------------------------------------

;Just use the definition given in class. You'll need it for the function below. 
(define (fold XXX) (XXX))

;----------------------------------------------------------------

(define (mergeN XXX) (XXX))

;Using merge2 and the fold function defined above you can now define mergeN which takes a list of lists, each already in ascending order, and returns a new list containing all of the elements in ascending order. 

; > (mergeN '())
; ()
; 
; > (mergen '((2 4 6) (1 4 5)))
; (1 2 4 4 5 6)
; 
; > (mergeN '((2 4 5) (1 4 6) (3 7 9)))
; (1 2 3 4 4 5 6 7 9)

;Note that this requires making sure that your understanding of fold encompasses seeing that it can return a list, not just a simple value; but the solution is, in fact, a very simple use of fold once you choose the right value for the base case corresponding to the empty list as input.

;Test mergeN
(if 
  (equal? 
    (mergeN '()) 
    null) ; Compiler made me change () to null
  "mergeN: PASS_1" 
  "mergeN: FAIL_1")

(if 
  (equal? 
    (mergeN '((2 4 6) (1 4 5)))
    (1 2 4 4 5 6)) 
  "mergeN: PASS_2" 
  "mergeN: FAIL_2")

(if 
  (equal? 
    (mergeN '((2 4 5) (1 4 6) (3 7 9)))
    (1 2 3 4 4 5 6 7 9))
  "mergeN: PASS_3" 
  "mergeN: FAIL_3")
