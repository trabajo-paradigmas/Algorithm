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

;Función de la succesión Fibonacci 
(define fib
  (lambda(x y)(+ x y)); Se suman los dos antesesores
  )

;Generador
(define (gen func a b)
  (list b (list (lambda () (gen func b (func a b))))); Devuelve una lista con el último término calculado y el generador siguiente
  )

;Aplica la función a un generador de dos parámetros
(define (take n func)
  (define (aux gen a b n acc); Se define la función auxiliar para mantener el conteo del acumulador
    (let; Sea
        (
         (A (eval (cadr gen))); A igual a la evaluación del próximo generador
         )
      (if; Si
       (= n 0) ;Se pide el termino °0
       (list); Se devuelve una lista vacía
       (if; De lo contrario, si
        (= n acc); el enésimo término es igual al acumulador
        (list b); Se devuelve el último término
        (cons b (aux A b (car A) n (+ acc 1))); De lo contrario, se devuelve la concatenación de el último elemento calculado con lo que resta de buscar el enésimo término
        )
       )
      )
    )
  (lambda()(aux (gen func 0 1) 0 1 n 1)); Se devuelve una función que enlista nos n primeros términos de un generador
  )
    
    

; Genera una lista de los primeros n términos de la suscesión Fibonacci dada por el generador
(define (gen->list func)
  (func); Se ejecuta el enlistado de (take (func) n)
  )