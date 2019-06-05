#lang scheme

(define (merge A B op)
  (cond
    ((null? A) B)
    ((null? B) A)
    (else
     (if
      (op (car A) (car B))
      (cons (car A) (merge (cdr A) B op))
      (cons (car B) (merge A (cdr B) op))
      )
     )
    )
  )

(define (mid_length L)
  (quotient (length L) 2)
  )

(define (split_at A k)
  (cond
    ((= k 0) (list (list) A))
    (else (let
              ([B (split_at (cdr A) (- k 1))]) (cons(cons (car A) (car B))(cdr B)))
          )
    )
  )

(define (split L)
  (split_at L (mid_length L))
  )

(define (merge_sort L op)
  (if
   (<= (length L) 1)
   L
   (let*
       (
        (AB (split L))
        (A (merge_sort (car AB) op))
        (B (merge_sort (car (cdr AB)) op))
        )
     (merge A B op)
     )
   )
  )

(define (insert x B)
  (define (cmp_keys x y) (<= (car x) (car y)))
  (if
   (or (null? B) (cmp_keys x (car B)))
   (cons x B)
   (cons (car B) (insert x (cdr B)))
   )
  )

(define (in_sort B)
  (if
   (or (null? B) (null? (cdr B)))
   B
   (insert (car B) (in_sort (cdr B)))
   )
  )

(define (insertion_sort A key)
  (define (key_elem x) (list (key x) x))
  (if
   (or (null? A) (null? (cdr A)))
   A
   (let*
       (
        (B (map key_elem A))
        (C (in_sort B))
        )
     (map cadr C)
     )
   )
  )


(define (binary_search V x)
  (define (bsearch V x i j)
    (if
     (> i j)
     #f
     (let*
         (
          (m (quotient (+ i j) 2))
          (y (vector-ref V m))
          )(cond
             ((= x y) #t)
             ((< x y) (bsearch V x i (- m 1)))
             (else (bsearch V x (+ m 1) j))
             )
       )
     )
    )
  (bsearch V x 0 (- (vector-length V) 1))
)


(define (Tim_sort L op)
  (define (Tim_aux L largo op)
    (if
     (null? L)
     L
     (if
      (< largo 6)
      (insertion_sort L op)
      (let*
          (
           (AB (split L))
           (A (merge_sort (car AB) op))
           (B (merge_sort (car (cdr AB)) op))
           )
        (merge A B op)
        )
      )
     )
    )
  (Tim_aux L (length L) op)
  )

(define (fib) (lambda(x y)(+ x y)))

(define (next_gen func a b)
  (let
      (
       (A (func a b))
       )
    (list A '(next_gen func b A))
    )
  )

(define (gen func n)
  (define(gen_aux func a b n acc)
    (if
     (= acc n)
     (car (next_gen func a b))
     (gen_aux func b (car (next_gen func a b)) n (+ acc 1))
     )
    )
  (gen_aux func 0 1 n 0)
  )

(define (gen->list func n)
  (define (gen_l a b func n acc)
    (cond
      (= n 0)
      (list)
      (= n acc)
      (list (car (next_gen a b)))
      (let
          (
          (A (next_gen a b))
          )
        (cons (gen_l b (car A) func n (+ acc 1)) (car A)))
    )
    )
  (gen_l 0 1 func n 1)
  )