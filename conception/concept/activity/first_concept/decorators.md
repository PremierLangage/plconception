# Decorators

The Decorators Solving gives a first Boolean, if it's True, the we look at the answers.
If we get two True, it's a succes, else it's a failure.
If the decorators Solving gives a False, then we restart the exercise (Or something else ? Strategy ?).

```
            Player
               |
               |
    Decorator Initializations<-----
               |                  |
               |                  |
             Start                |
               |                  |
               |              (False, ?)
             Answer               |
               |                  |
               |                  |
    |--->Decorators Solving--------
 ForEach    |  |
    --------|  |
               |
              / \
             /   \
            /     \
 (True, True)     (True, False)
          /         \
      Success    Failure
```
