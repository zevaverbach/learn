(define (pigl wd)
  (if (pl-done? wd)
      (word wd 'ay)
      (pigl (word (bf wd) (first wd)))))

(define (pl-done? wd)
  (vowel? (first wd)))

(define (vowel? letter)
  (member? letter '(a e i o u)))

; copied from https://stackoverflow.com/a/48548725/4386191 without understanding it yet
(define member?
  (lambda (x los)
    (cond
      ((null? los) #f)
      ((eq? x (car los)) #t)
      (else (member? x (cdr los))))))
