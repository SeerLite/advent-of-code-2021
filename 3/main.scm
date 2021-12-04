(use-modules (ice-9 textual-ports)
             (srfi srfi-1))

(define inputs (filter-map (lambda (line)
                                   (define line-as-list (string->list line))
                                   (if (null? line-as-list)
                                       #f
                                       line-as-list))
                           (string-split
                            (with-input-from-file "input.txt"
                                                  (lambda () (get-string-all (current-input-port))))
                            #\newline)))
(define ones
        (let ((results (make-list (length (car inputs)) 0)))
           (fold (lambda (current-line results)
                         (map (lambda (val char)
                                      (if (eqv? char #\1)
                                         (1+ val)
                                         val))
                              results
                              current-line))
                 results
                 inputs)))
(define zeroes
        (let ((total-lines (length inputs)))
             (map (lambda (this-one)
                          (- total-lines this-one))
                  ones)))
         
; This for-each turned out to be more code than if I had just left
; the lines format duplicated lol
(for-each (lambda (data-pair)
                  (define name (car data-pair))
                  (define content (cdr data-pair))
                  (format #t "~a: ~a\n" name
                          (string-join (map number->string content))))
          `(("ones" . ,ones) ("zeroes" . ,zeroes)))


