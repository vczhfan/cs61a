; 1
(define (fib n)
    (if (< n 2) 
        1
        (+ (fib (- n 1)) (fib (- n 2)))))

; 2
(define (map fn lst)
    (if (null? lst)
        '()
        (cons (fn (car lst)) (map fn (cdr lst)))))

; 3
(define (reduce fn s lst)
    (if (null? lst)
        s
        (fn (car lst) (reduce fn s (cdr lst)))))

; 4
(define (make-btree entry left right)
    (cons entry (cons left right)))

(define (entry tree)
    (car tree))

(define (left tree)
    (car (cdr tree)))

(define (right tree)
    (cdr (cdr tree)))

; 5
(define (btree-sum tree)
    (if (null? tree)
        0
        (+ (entry tree)
            (btree-sum (left tree))
            (btree-sum (right tree)))))