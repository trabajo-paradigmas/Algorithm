#lang scheme
(define (merge A B)
  (cond
    ((null? A) B)
    ((null? B) A)
    ((< (car A) (car B)) (cons (car A) (merge (cdr A) B)))
    ((= (car A) (car B)) (cons (car A) (merge (cdr A) (cdr B))))
    (else (cons (car B) (merge A (cdr B))))
    )
  )

(define (insertion A k)
  (cond
    ((null? A) (list k))
    ((< (car A) k) (cons (car A) (insertion (cdr A) k)))
    ((> (car A) k) (cons k A))
    (else(A))
    )
  )

(define (counter A)
  (cond
    ((null? A) 0)
    (else (+ (counter (cdr A)) 1))
    )
  )

(define (split_at A k)
  (cond
    ((= k 0) (list(list) A))
    (else (let
              ([B (split_at (cdr A) (- k 1))]) (list(cons (car A) (car B)) (cdr B)))
          )
    )
  )
