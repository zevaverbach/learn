Installed `mit-scheme`, which doesn't have some of the procedures demonstrated in the lecture. I think I installed it from gnu.org. I also installed `rlwrap` (`brew install rlwrap`) and aliased `scheme` to rlwrap scheme` in order to have my expected shell keyboard bindings and command history.

# Syntax

There's not much syntax to Scheme/Lisp, which is something people brag about; it lets you dive into hands-on learning quickly.

## Special Forms

- `(define x 42)` this assigns a value to the variable `x`
- `(define (square x) (x * x))` this creates a procedure `square` with formal parameter `x` and body `(x * x)`. Whitespace is insignificant, and by convention the body goes on its own line:

```lisp
(define (square x)
        (x * x)
)
```

# Vocabulary
- formal parameter
- body

# Built-ins
- `equal?` - a predicate function (returns true or false)

# Lab

## `plural`

In the class we defined the procedure
```lisp
(define (plural wd) 
    (if (equal? (last wd) 'y)
        (word (bl wd) 'ies)
        (word wd 's))
```

However, this doesn't work for `(plural 'boy)`, which outputs `boies``. Make it output `boys`:

```lisp
(define (plural wd) 
    (if (and (equal? (last wd) 'y) (not (equal? wd 'boy)))
        (word (bl wd) 'ies)
        (word wd 's)))
```

# Pig Latin

