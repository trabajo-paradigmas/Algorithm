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

; Devuelve la mitad menor del largo de una lista
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

;Ordenamiento por inserción por medio de una operación binaria
(define (in_sort B op)
  (if
   (or (null? B) (null? (cdr B))); Si es vacía se devuelve la misma lista
   B
   (insert (car B) (in_sort (cdr B) op) op); De lo contrario se toma el primer elemento para ser insertado en lo que retorna el ordenar el resto de la lista
   )
  )

; Inserta en orden un elemento a lista
(define (insert x B op)
  (if
   (or (null? B) (op x (car B))); Si es vacío o la comparación es verdadera
   (cons x B); Se concatena el elemento a insertar con el resto de la lista
   (cons (car B) (insert x (cdr B) op)); De lo contrario se concatena el primer elemento con el resultado de ordenar la lista restante
   )
  )
  
;Timsort
(define (timsort L op)
  (define (Tim_aux L largo op);Usa el algoritmo de mergesort
    (if
     (= (length L) 1); Si tiene un elemento
     L; Se devuelve la lista ya que un elemento único está ordenado
     (if
      (< largo 18); Si se encuentra en el punto óptimo de galope
      (in_sort L op); Entonces devuelve lista ordenada por inserción
      (let*; De lo contrario
          (;Sea
           (AB (split L)); AB la separación en mitades de la lista
           (A (Tim_aux (car AB) (length (car AB)) op)); Se ordena una mitad por mergesort
           (B (Tim_aux (car (cdr AB)) (length (cdr AB)) op)); Se ordena la otra mitad por mergesort
           )
        (merge A B op); Se unen ambas listas con merge
        )
      )
     )
    )
  (Tim_aux L (length L) op)
  )

(define (fib) (lambda(x y)(+ x y)))

;Aplica la función a dos parámetros
(define (next_gen func a b)
  (list (func a b))
  )

;(take n) Genera el enésimo término de un generador Fibonacci
(define (gen func n)
  (define(gen_aux func a b n acc); Define una función auxiliar
    (if
     (= acc n); Si el la posición del numero buscado es igual al acumulador
     (car (next_gen func a b)); Se devuelve el numero generado por la función
     (gen_aux func b (car (next_gen func a b)) n (+ acc 1)); De lo contrario se sigue al próximo generador
     )
    )
  (if
   (= n 0) (list); Si  se pide el elemento 0 se devuelve una lista vacía
   (if
    (= n 1) 1; Si se busca el primer elemento se devuelve un uno
    (gen_aux func 0 1 n 2); De lo contrario se llama a la función auxiliar para avanzar a la posición buscada
    )
   )
  )

;(gen_list) Genera una lista de los primeros n términos de la suscesión Fibonacci
(define (gen->list func n); Lo mismo que la anterior
  (define(gen_aux func a b n acc)
    (if
     (= acc n)
     (list(car (next_gen func a b)))
     (cons (+ a b)(gen_aux func b (car (next_gen func a b)) n (+ acc 1))); Pero al final se enlista el resultado
     )
    )
  (if
   (= n 0) (list)
   (if
    (= n 1) (list 1)
    (cons 1(gen_aux func 0 1 n 2)); Acá también se enlista el primer elemento omitido, el uno
    )
   )
  )