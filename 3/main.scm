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

(define (print-num-list name content)
        (let ((content (string-join (map number->string content))))
             (format #t "~a: ~a\n" name content)))

(define (bin-list->integer bin-list)
       (string->number (string-join (map number->string
                                         bin-list)
                                    "")
                       2))

(define total-lines (length inputs))

(define
 (part-1 inputs)
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
         (map (lambda (this-one)
                      (- total-lines this-one))
              ones))

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

 (define gamma-as-number (bin-list->integer gamma))
 (define epsilon-as-number (bin-list->integer epsilon))

 (format #t "gamma as number: ~a\n"
         gamma-as-number)
 (format #t "epsilon as number: ~a\n"
         epsilon-as-number)
 (format #t "product of gamma and epsilon: ~a\n"
  (* gamma-as-number epsilon-as-number)))

(define
 (part-2 inputs)
 (define (filter-by-first-num inputs num)
         (if (= (length inputs) 1)
             inputs
             (filter (lambda (line)
                             (= (car line)
                                num))
                     inputs)))
 
 (define (traverse inputs criteria)
         (let loop ((inputs inputs))
              (if (null? (car inputs))
                  '()
                  (begin
                   (cond ((= (length inputs) 1)
                          (car inputs))
                         ((criteria (apply + (map car inputs))
                           (/ (length inputs) 2))
                          (cons 1 (loop (map cdr (filter-by-first-num inputs 1)))))
                         (else
                          (cons 0 (loop (map cdr (filter-by-first-num inputs 0))))))))))
              
         
 (let* ((inputs (map (lambda (line)
                             (map (compose string->number string) line))
                     inputs))
        (oxygen-generator-rating
          (bin-list->integer (traverse inputs >=)))
        (co2-scrubber-rating 
          (bin-list->integer (traverse inputs <))))
      (format #t "oxygen generator rating: ~a\n" oxygen-generator-rating)
      (format #t "CO2 scrubber rating: ~a\n" co2-scrubber-rating)
      (format #t "life support rating (product of above): ~a\n"
              (* oxygen-generator-rating co2-scrubber-rating))))

(part-1 inputs)
(part-2 inputs)
