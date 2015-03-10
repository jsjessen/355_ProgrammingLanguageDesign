; #lang R5RS
; Linux/Unix

; James Jessen
; 10918967
; CptS 355 HW4

;================================================================

;Assume that the index, n, is at least 0 and smaller than the length of the list. 
;Return the nth element of a list (0-based indexing). 
(define (nth L n) 
  (cond 
    ((= n 0) (car L))
    (#t (nth (cdr L) (- n 1)))
    ))

;Test nth
(define (nthTest)
  (if
    (equal? 
      (nth '(1 2 3 4) 1)
      2)
    (display "nth: PASS 1") 
    (display "nth: FAIL 1"))
  (newline)
  (if
    (equal? 
      (nth '(1 2 3) 0)
      1)
    (display "nth: PASS 2") 
    (display "nth: FAIL 2"))
  (newline)
  (if
    (equal? 
      (nth '(2 3 4) 2)
      4)
    (display "nth: PASS 3") 
    (display "nth: FAIL 3"))
  (newline))

;----------------------------------------------------------------

;Assume that the index i is at least 0 and smaller than the length of the list. 
;Return a new list which is the same as L except that the ith element is v. 
(define (repl L i v) 
  (cond 
    ((= i 0) (cons v (cdr L)))
    (#t (cons (car L) (repl (cdr L) (- i 1) v)))
    ))

;Test repl
(define (replTest)
  (display "---------------")
  (newline)
  (if
    (equal? 
      (repl '(1 2 3 4) 1 7)   
      '(1 7 3 4)) 
    (display "repl: PASS 1") 
    (display "repl: FAIL 1"))
  (newline)
  (if
    (equal? 
      (repl '(1 2 3) 0 81)   
      '(81 2 3)) 
    (display "repl: PASS 2") 
    (display "repl: FAIL 2"))
  (newline)
  (if
    (equal? 
      (repl '(1 2 3) 2 -6)   
      '(1 2 -6)) 
    (display "repl: PASS 3") 
    (display "repl: FAIL 3"))
  (newline))

;----------------------------------------------------------------

;Return a list of integers (min min+1 ... max-1). 
;If min ≥ max return the empty list. Example:
(define (range min max)
  (cond 
    ((>= min max) '() )
    (#t (cons min (range (+ min 1) max)))
    ))

;Test range
(define (rangeTest)
  (display "---------------")
  (newline)
  (if 
    (equal? 
      (range 4 6) 
      '(4 5)) 
    (display "range: PASS 1") 
    (display "range: FAIL 1"))
  (newline)
  (if 
    (equal? 
      (range 8 6) 
      '()) 
    (display "range: PASS 2") 
    (display "range: FAIL 2"))
  (newline)

  (if 
    (equal? 
      (range 5 16) 
      '(5 6 7 8 9 10 11 12 13 14 15)) 
    (display "range: PASS 3")
    (display "range: FAIL 3"))
  (newline))

;----------------------------------------------------------------

;Merge two lists of integers, each already in ascending order, 
;into a new list that is also in ascending order.
(define (merge2 L1 L2)
  (cond 
    ((null? L1) L2)
    ((null? L2) L1)
    (#t (if (<= (car L1) (car L2)) 
          (cons (car L1) (merge2 (cdr L1) L2))
          (cons (car L2) (merge2 (cdr L2) L1))
          ))))

;Test merge2
(define (merge2Test)
  (display "---------------")
  (newline)
  (if 
    (equal? 
      (merge2 '(2 4 6) '(1 4 5))
      '(1 2 4 4 5 6))
    (display "merge2: PASS 1")
    (display "merge2: FAIL 1"))
  (newline)
  (if 
    (equal? 
      (merge2 '(4 5 6) '(1 2 3))
      '(1 2 3 4 5 6))
    (display "merge2: PASS 2")
    (display "merge2: FAIL 2"))
  (newline)
  (if 
    (equal? 
      (merge2 '(1 2 3 200) '(4 5 6 70))
      '(1 2 3 4 5 6 70 200))
    (display "merge2: PASS 3")
    (display "merge2: FAIL 3"))
  (newline))

;----------------------------------------------------------------

;Given
;Combine the elements of L using fcombine, return basecase if L is empty 
(define (fold fcombine basecase L)
  (cond
    ((null? L) basecase)
    (#t (fcombine (car L) (fold fcombine basecase (cdr L))))
    ))

;----------------------------------------------------------------

;Take a list of lists, each list already in ascending order
;Return a new list containing all of the elements in ascending order. 
(define (mergeN LL) (fold merge2 '() LL))

;Test mergeN
(define (mergeNTest)
  (display "---------------")
  (newline)
  (if 
    (equal? 
      (mergeN '()) 
      '() )
    (display "mergeN: PASS 1") 
    (display "mergeN: FAIL 1"))
  (newline)
  (if 
    (equal? 
      (mergeN '((2 4 6) (1 4 5)))
      '(1 2 4 4 5 6)) 
    (display "mergeN: PASS 2") 
    (display "mergeN: FAIL 2"))
  (newline)
  (if 
    (equal? 
      (mergeN '((2 4 5) (1 4 6) (3 7 9)))
      '(1 2 3 4 4 5 6 7 9))
    (display "mergeN: PASS 3") 
    (display "mergeN: FAIL 3"))
  (newline))

;================================================================

(define (test)
  (nthTest)
  (replTest)
  (rangeTest)
  (merge2Test)
  (mergeNTest))

(test)
