; these are some of the procedures (re-implemented/reverse-engineered) from the `stk-simply` package, which doesn't support modern MacOS versions
; to use this library, do `scheme --load <path-to-this-file>`
; there has to be a more automatic way, by putting this file in some auto-loaded path, but I haven't figured that out yet!

; TODO: these don't work for lists, but they should
(define (first w) 
      (string->symbol (substring (symbol->string w) 0 1)))

(define (last w) 
      (define s (symbol->string w))
      (define len (string-length s))
      (string->symbol (substring s (- len 1) len)))

(define (butfirst w)
      (define s (symbol->string w))
      (define len (string-length s))
      (string->symbol (substring s 1 len)))

(define (butlast w)
      (define s (symbol->string w))
      (define len (string-length s))
      (string->symbol (substring s 0 (- len 1))))

(define (bf w) (butfirst w))
(define (bl w) (butlast w))

(define (word symbol1 symbol2)
      (define s1 (symbol->string symbol1))
      (define s2 (symbol->string symbol2))
      (string->symbol (string-append s1 s2)))

(define (sentence s1 s2) (list s1 s2))

(define (item idx word)
      (string->symbol (
          substring 
              (symbol->string word) 
              idx 
              (+ idx 1))))
