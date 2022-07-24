# Update 07/24/2022 1:47 PM EST
### DEPRECATION OF "toggle_difficulty_level"
> ``toggle_difficulty_level`` will raise `DeprecationWarning` when called; additionally it'll be removed from the class within the next day or so.

### CHANGES TO "objective"
> ``objective`` now requres you to provide a ``difficulty`` parameter when called.
> 
> ``objective`` will raise ``DeprecationWarning`` when ``amount`` is more than 1.
> 
> ``objective`` will raise ``SyntaxError`` when ``difficulty`` is not provided.
> 
> > Old Usage:
> > > ```python
> > > errors = Error_Objective()
> > > errors.objective(amount=...)
> > > ```
> > New Usage:
> > > ```python
> > > errors = Error_Objective()
> > > errors.objective(difficulty=...)  # EASY | MOD | HARD
> > > ```