<a href="https://ibb.co/dQJ9hBc"><img src="https://i.ibb.co/2jY2bq6/image.png" alt="image" border="0"></a>

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
> > > 
> > > 
# Update 07/24/2022 5:19 PM EST
### REMOVAL OF "toggle_difficulty_level"
> ``toggle_difficulty_level`` has been removed.

### CHANGES TO "objective"
> ``objective`` now requres you to provide a ``difficulty`` parameter when called.
> 
> ``objective`` no longer takes ``amount`` as a parameter.
> 
> ``objective`` will raise an exception if difficulty is not provided.
> 
> ``objective`` will raise ``DifficultyObjectivesCompleted`` if ``already_used_keywords`` is equal to ``self.ERRORS[difficulty]``
> 
> ``objective`` now allows you to provide ``already_used_keywords`` as a parameter, to prevent duplicate objectives.
> > Old Usage:
> > > ```python
> > > errors = Error_Objective()
> > > errors.objective(amount=...)
> > > ```
> > New Usage:
> > > ```python
> > > errors = Error_Objective()
> > > errors.objective(difficulty=..., already_used_keywords= list | None)  # EASY | MOD | HARD
> > > ```

# Update 07/24/2022 9:13 PM EST
### ASYNC ADDED 

> ``objective`` now requires you to ``await`` it.
> > Old Usage:
> > > ```python
> > > errors = Error_Objective()
> > > errors.objective(difficulty=..., already_used_keywords= list | None)
> > > ```
> > New Usage:
> > > ```python
> > > errors = Error_Objective()
> > > foo = await errors.objective(difficulty=..., already_used_keywords= list | None)
> > > ```
> > > Thanks [Barko]
> 
> [Barko]: https://github.com/bark-o