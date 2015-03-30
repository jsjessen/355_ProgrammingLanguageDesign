;Assume that the index, n, is at least 0 and smaller than the length of the list. 
;Return the nth element of a list (0-based indexing). 
(define (lookup L key) 
  (cond 
    ((= (car(car L)) key) ())
    ((= n 0) (car L))
    (#t (nth (cdr L) (- n 1)))
    ))

;Test
(define (lookupTest)
  (if
    (equal? 
      (lookup '((1 4) (14 5) (7 3) (22 6)) 14)
      5)
    (display "lookup: PASS") 
    (display "lookup: FAIL"))
  (newline))
