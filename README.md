# Pygame Map Builder v1.1!

Hello! I've created this in an attempt to make pygame a little more accessible to new users as well as making it easier to create the tedious things. This allows someone
to physically create a map by dragging and droping tiles into place so that no code is nessecary. It is still a massive work in progress however v1.1 is officially out!

With the new edition from v1.0 to v1.1, the tags system was implemented! (although quite unsightly) it is used as a way to keep track of similar tiles that might be used for different purposes. Take a look at the myAwesomeGame example to see how you can use the tags system to help develop your games.

Other methods have been added to the mapBuilderLoader in order to keep your main code smaller and cleaner.

Create a map by running main.py

Load that map via:
```
  import mapBuilderLoader
  myMapLoader = mapBuilderLoader.MapLoader([MAP FOLDER], [SCREEN]) ## replace [MAP FOLDER] with the folder for your map (should be a string) and [SCREEN] with the variable holding your pygame display
  myMapLoader.display_map() ## Make sure to place this within the main game loop
```  
If you need further refrence to load a created map, check out myAwesomeGame.py
