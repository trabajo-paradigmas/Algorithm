(define (merge A B)
  (cond
    ((null? A) B)
    ((null? B) A)
    ((< (car A) (car B)) (cons (car A) (merge (cdr A) B)))
    (else (cons (car B) (merge A (cdr B))))
    )
  )