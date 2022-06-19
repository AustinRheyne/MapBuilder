# MapBuilder

Hello! I've created this in an attempt to make pygame a little more accessible to new users as well as making it easier to create the tedious things. This allows someone
to physically create a map by dragging and droping tiles into place so that no code is nessecary. It is still a massive work in progress however v1.0 is officially out!

Create a map by running main.py

Load that map via:
  import mapBuilderLoader
  myMapLoader = mapBuilderLoader.MapLoader([MAP FOLDER], [SCREEN]) ## replace [MAP FOLDER] with the folder for your map (should be a string) and [SCREEN] with the variable holding your pygame display
  myMapLoader.display_map() ## Make sure to place this within the main game loop
  
If you need further refrence to load a created map, check out myAwesomeGame.py
