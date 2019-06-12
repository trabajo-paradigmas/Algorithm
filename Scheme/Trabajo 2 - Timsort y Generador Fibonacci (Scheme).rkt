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
      (< largo 18); Si se encuentra en el punto óptimo de galope (18 para Scheme)
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