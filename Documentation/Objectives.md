[Error Thrower]: https://github.com/mkadiya20/heroic-hydra/blob/67f188d0a955d1ae60e08e426ccc68b27ff27e15/src/server/error_thrower.py
[Point Handler]: https://github.com/mkadiya20/heroic-hydra/blob/67f188d0a955d1ae60e08e426ccc68b27ff27e15/src/server/point_hardness.py
[License]: https://github.com/mkadiya20/heroic-hydra/blob/67f188d0a955d1ae60e08e426ccc68b27ff27e15/LICENSE
[Python 3.10]: https://www.python.org/downloads/release/python-3100/
[Project Dependencies]: https://github.com/mkadiya20/heroic-hydra/blob/67f188d0a955d1ae60e08e426ccc68b27ff27e15/poetry.lock
[LocalHost URL]: http://localhost/
[Alternative URL]: http://127.0.0.1/




<img src="https://www.pythondiscord.com/static/images/events/summer_code_jam_2022/site_banner.png" alt="Summer Code Jam Banner">


# <font color="#FF4040"> Error </font> Race

> <font color="#FFC125" style="bold">**Documentation for [Error Thrower] & [Point Handler]**  </font>

# Table of Contents <img src="https://www.iconpacks.net/icons/2/free-opened-book-icon-3163-thumb.png" width=50, height=50>
> [Project Dependencies](#Dependencies) <br>
> [License Terms](#License) <br>
> [Error Thrower Class](#ErrorThrower) <br>
> [Point Handler Class](#PointHandler)
> 

## Dependencies <span id="Dependencies"><span>
> The following are required to be installed to use **<font color="#FF4040"> Error </font> Race**
> 
> * [Python 3.10]
> * [Project Dependencies]
> * Access to [LocalHost URL] / [Alternative URL] using ports 8000 and 8060





## License <span id="License"><span>

> <font color="#FF4040">**BEFORE YOU CONTINUE!** </font>
> > Please Read the [License] Agreements before continuing. By continuing you hereby declare that you have read the contents of [license] and agree to its terms.
> 
> 



## Error Thrower <span id="ErrorThrower"><span>

> Initialize <font color="#FF8C00"> Error_Objective </font>:
> > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="20"> <font color="#FFD43B"> Python</font>:
> > <details>
> >    <summary>Inside of <code>error_thrower.py</code></summary>
> >     <br>
> >     Since you're already using the classes file; the <code>imports</code> are already present.
> >     You'll only need to add the following code to the bottom of the file:
> >     
> >     error_obj = Error_Objective()
> > 
> >   </details>
> > <details>
> >    <summary>Outside of <code>error_thrower.py</code></summary>
> >     <br>
> >     Since you're using a different python file to initialize <font color="#FF8C00"> Error_Objective </font>
> >     <br>
> >     You'll need to add the following imports to the top of the file:
> >     
> >     import asyncio
> >     from error_thrower import Error_Objective
> >    <br>
> >      Then, add the following in a spot you see fit:
> >    <br>
> >      
> >     error_obj = Error_Objective()
> > 
> >   </details>

> Call <font color="#FF8C00"> Error_Objective</font>
> > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="20"> <font color="#FFD43B"> Python</font>:
> >
> > <font color="#00C957">**NOTE: This step is the same regardless of the python file you've used.** </font>
> > <br>
> > <details>
> > <summary> Parameter Usage </summary>
> > <br>
> > <table>
> >   <tr>
> >     <td>Name</td>
> >     <td>Casting Type</td>
> >     <td>Default Value</td>
> >     <td> Required</td>
> >  </tr>
> >     <td><font color="#FF8C00"> difficulty</font></td> <td><font color="#959ed6">  int</font></td><td>>===>===></td><td>True</td></tr>
> >     <td><font color="#FF8C00"> already_used_keywords</font></td> <td><font color="#959ed6">list | tuple</font></td><td><font color="#FF8C00">    None</font></td><td>False</td>
> > </table>
> > </details>
> > <details>
> > <summary> Exception Information: </summary>
> > raises <code>DifficultyObjectivesCompleted</code> if <font color="#FF8C00"> already_used_keywords</font> matches the values in <code>self.ERRORS[difficulty]</code>.
> > </details>
> > Add the following on the line you want to call it from: <br>
> > <code> asyncio.run(error_obj.objective(...)) </code>


## Point Handler <span id="PointHandler"><span>

> Initialize <font color="#FF8C00"> PointHandlerError </font>:
> > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="20"> <font color="#FFD43B"> Python</font>:
> > <details>
> >    <summary>Inside of <code>point_hardness.py</code></summary>
> >     <br>
> >     Since you're already using the classes file; the <code>imports</code> are already present.
> >     You'll only need to add the following code to the bottom of the file:
> >     
> >     point_obj = PointHandler()
> > 
> > 
> >   </details>
> > <details>
> >    <summary>Outside of <code>point_hardness.py</code></summary>
> >     <br>
> >     Since you're using a different python file to initialize <font color="#FF8C00"> PointHandler </font>
> >     <br>
> >     You'll need to add the following imports to the top of the file:
> >     
> >     import asyncio
> >     from error_thrower import Error_Objective
> >     from user import User
> >    <br>
> >      Then, add the following in a spot you see fit:
> >    <br>
> >      
> >     point_obj = PointHandler()
> > 
> >   </details>

> Call <font color="#FF8C00"> PointHandler</font>
> > <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png" height="20"> <font color="#FFD43B"> Python</font>:
> >
> > <font color="#00C957">**NOTE: This step is the same regardless of the python file you've used** </font> <br>
> > <font color="#FF8C00">***ADDITIONAL NOTICE: If you've modified the name of the Error_Objective Class, you need to provide the new class name to ``error_obj``**</font>
> > <br>
> > <details>
> > <summary> Parameter Usage </summary>
> > <br>
> > <table>
> >   <tr>
> >     <td>Name</td>
> >     <td>Casting Type</td>
> >     <td>Default Value</td>
> >     <td> Required</td>
> >  </tr>
> >     <td><font color="#FF8C00"> Assignment</font></td> <td><font color="#959ed6">  str</font></td><td>>===>===></td><td>True</td></tr>
> >     <td><font color="#FF8C00"> client_user</font></td> <td>User</td><td>>===>===></td><td>True</td></tr>
> >     <td><font color="#FF8C00"> error_obj</font></td> <td>Error_Objective</td><td>Error_Objective()</td><td>*False </td></tr>
> > </table>
> > </details>
> > <details>
> > <summary> Exception Information: </summary>
> > raises <code>PointHandlerError</code> on Exception.
> > </details>
> > Add the following on the line you want to call it from: <br>
> > <code> asyncio.run(point_obj.point(...)) </code>









> Documentation by: <font color="#FF8C00" size="6"> Clyde#2021 <img src="https://cdn-icons-png.flaticon.com/128/616/616454.png" width="27">

  
