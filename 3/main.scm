(use-modules (ice-9 textual-ports)
             (srfi srfi-1)
             (srfi srfi-60))

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

(define (print-num-list name content)
        (let ((content (string-join (map number->string content))))
             (format #t "~a: ~a\n" name content)))

(print-num-list "ones" ones)
(print-num-list "zeroes" zeroes)

(define gamma (map (lambda (ones zeroes)
                           (if (> ones zeroes)
                               1
                               0))
                   ones
                   zeroes))

(define epsilon (map (lambda (n)
                             (logxor n 1))
                     gamma))

(print-num-list "gamma" gamma)
(print-num-list "epsilon" epsilon)

(define (bin-list->integer bin-list)
        (string->number (string-join (map number->string
                                          bin-list)
                                     "")
                        2))

(define gamma-as-number (bin-list->integer gamma))
(define epsilon-as-number (bin-list->integer epsilon))

(format #t "gamma as number: ~a\n"
        gamma-as-number)
(format #t "epsilon as number: ~a\n"
        epsilon-as-number)
(format #t "product of gamma and epsilon: ~a\n"
        (* gamma-as-number epsilon-as-number))
