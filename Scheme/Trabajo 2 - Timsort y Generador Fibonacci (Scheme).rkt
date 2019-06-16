#lang scheme
;Estudiantes:
;            - Javier Gómez
;            - Ignacio Sanhueza

;Profesor:   - Pablo Pérez Lantero

;Ramo:       - Paradigmas de la programación



;Trabajo número dos: Timsort y generadores en Scheme


; Une dos listas ordenadas
(define (merge A B op)
  (cond
    ((null? A) B); Si es una lista vacía
    ((null? B) A); Se devuelve la otra lista
    (else; De lo contrario
     (if
      (op (car A) (car B)); Si el primer elemento de la primera es menor a de la segunda
      (cons (car A) (merge (cdr A) B op)); Se concatena ese elemento con lo que retorna de ordenar la lista restante
      (cons (car B) (merge A (cdr B) op)); o al revés
      )
     )
    )
  )

; Devuelve el largo de la mitad menor de una lista
(define (mid_length L)
  (quotient (length L) 2)
  )

; Parte una lisa en un índice determinado
(define (split_at A k)
  (cond
    ((= k 0) (list (list) A)); Si la lista es vacía devuelve una lista con primer elemento una lista vacía y segundo la lista restante
    (else (let
              ([B (split_at (cdr A) (- k 1))]) (cons(cons (car A) (car B))(cdr B))); De lo contrario se concatena el primer elemento con el primer elemento que devuelve de partir la lista
          )
    )
  )

; Parte una lista a la mitad con la mitad menor como primer elemento
(define (split L)
  (split_at L (mid_length L))
  )

;Ordenamiento por mezcla
(define (merge_sort L op)
  (if; Si
   (<= (length L) 1); El largo es igual o menor a 1
   L; Se devuelve la lista
   (let*;De lo contrario, sea:
       (
        (AB (split L)); AB igual a la partición a la mitad de la lista
        (A (merge_sort (car AB) op)); A igual a seguir ordenando por la primera mitad
        (B (merge_sort (car (cdr AB)) op)); B igual a seguir ordenando por la segunda mitad
        )
     (merge A B op); Se retorna el ordenamiento por mezcla de ambas mitades
     )
   )
  )

;Ordenamiento por inserción
(define (in_sort B)
  (if
   (or (null? B) (null? (cdr B))); Si es vacía se devuelve la misma lista
   B
    (insert (car B) (in_sort (cdr B))); De lo contrario se toma el primer elemento para ser insertado en lo que retorna el ordenar el resto de la lista
   )
  )

; Inserta en orden un elemento a lista
(define (insert x B)
  (define (cmp_keys x y) (< (car x) (car y))); Define una funcíon de comparación
  (if; Si
   (or (null? B) (cmp_keys x (car B)));  O la lista esta vacía, o la comparación del elemento da ser menor al primer elemento de la lista
   (cons x B); Se concatena el elemento a la lista
   (cons (car B) (insert x (cdr B))); De lo contrario se concatena el primer elemento de la listo con lo que resta por insertar en la lista
   )
  )

;Ordenamiento por insersión
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
  
;Timsort
(define (timsort L op)
  
  (define (cmp op x y)
    (cond
      (< (op x) (op y)) (car (list 1))
      (> (op x) (op y)) (car (list -1))
      (= (op x) (op y)) (car (list 0))
      )
    )
  
  (define (OP_merge L1 L2 op)
    (merge_sort L1 L2 (lambda(x y)(< (op x)(op y))))
    )
  
  (define (rev L)
    (define (rev2 A B)
      (if
       (null? B)
       A
       (rev2
        (cons (car B) A)
        (cdr B)
        )
       )
      )
    (rev2 (list) L)
    )
  
  (define (subsec op_ant L acc); Cuenta en dónde realizar el corte mediante (split_at) y retorna una lista de subsequencias ordenadas
    (let*
        (
         ()
         )
      ()
        )
    )
    
  (subsec 2 L 1)
  )
;El punto óptimo del galope fue calculado mididendo diferentes tiempos de ejecución para diferentes largos de listas, que se incrementan en uno por cada prueba nueva,
;hasta que el algoritmo por insersión resultara por primera vez pase de tener menor tiempor de ejecución frente al ordenamiento por mezcla
;a todo lo contrario (hasta que el ordenamiento por mezcla presente menor tiempor de ejecución que por insersión). Eso en Scheme ocurre en el largo 18 de lsitas
; siendo 19 un largo óptimo para mergesort


;Próximo generador
(define (next_gen gen op); gen = generador: (último-valor (próximo-generador op) ; op = función a operar
  (let*; Sea
      (
       (A(car gen)); A igual al último valor generado 
       (B (caadr gen)); B igual al próximo valor a generar
       )
      (list B (list (op A B) (lambda()(op A B)) op)); Devuelve el próximo generador
      )
  )

;Generador base de la succesión Fibonacci
(define fib
  (let; Sea
      (
       (x(car '(0))); x igual a 0
       (y(car '(1))); y igual a 1
       )
    (next_gen (list x (list (+ x y) (lambda()(lambda()(+ x y)))) +) +); Se entrega el primer generador de la sucesión Fibonacci
    )
  )


;Generador que devuelve un generador acotado
(define (take gen n)
  (if; Si 
   (= n 0); El número buscado es igual a 0
   (cons #f (cdr gen)); Se devuelve un generador con (car) = falso
   (list (car gen) (lambda ()(take (next_gen gen (caddr(cadr gen))) (- n 1)))); De lo contrario, se devuelve un generador con (car)= elemento generado y (cdr)= siguiente generador
   )
  )
    
    

; Función que aplica un generador acotado y lo enlista
(define (gen->list gen); gen = generador que entrega un nuevo generador acotado
  (if; Si
   (equal? (car gen) #f); El (car) de "gen" es equivalente a falso
   null; Se retorna una lista vacía
   (cons (car gen)(gen->list ((cadr gen)))); De lo contrario, se devuelve la concatenación del primer elmeneto del "gen" con lo que resta de enlistar los siguientes generadores "((cdr gen))"
   )
  )