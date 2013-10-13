; 1
(define (factorial_recursive n)
    (if (= n 0)
        1
        (* n (factorial_recursive (- n 1)))))

; 2
(define (factorial_iterative x)
    (fact_iter_helper 1 1 x))

(define (fact_iter_helper product count max)
    (if (> count max)
        product
        (fact_iter_helper (* product count) (+ count 1) max)))

; Lists
; 1
(define structure (cons (cons 1 '()) (cons 2 (cons (cons 3 4)) (cons 5 '()))))

; 2
(define (interleave lst1 lst2)
    (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (cons (car lst1) (car lst2)) (interleave (cdr lst1) (cdr lst2))))))

(define (interleave lst1 lst2)
    (cond ((null? lst1) lst2)
          ((null? lst2) lst1)
          (else (cons (car lst1) (interleave lst2 (cdr lst1))))))

; 3
(define (remove item lst)
    (cond ((null? lst) '())
          ((equal? item (car lst)) (remove item (cdr lst)))
          (else (cons (car lst) (remove item (cdr lst))))))

; 4
(define (all_satisfies lst pred)
    (= (length (filter pred lst)) (length lst)))

;5
(define (repeat_els lst pred)
    (reduce append (map (lambda (n) (if (pred n) (list n n) (list n))) lst)))
