# About
This project mainly contains a [blender model](world-map_robinson-projection_first-political-division_cnc3018Pro.blend) of the world map.
With it a (wooden) world map for the wall can be created.
For cutting I used the CNC 3018-Pro.

# Additional steps
The base project can be extended with additional steps.

Here are some ideas.
- Countries have magnets and can be taken of the wall
- LED lid background via acryl plate
	- LEDs are controllable (eg via raspberry pi)
- Finer details like rivers via wood burning laser of cnc
- Countries have a hight profile (multilayer wood)

# Notes on the blender file
The model was created via the [svg file](https://upload.wikimedia.org/wikipedia/commons/f/fd/Blank_map_of_the_world_%28Robinson_projection%29_%2810E%29.svg) of the world which uses robinson projection with first level political division.
For the future I want to create the svg via the unfinished subproject [mapCreator](./mapCreator).

From it I hope to have:
- Less manual work in blender
- More flexiblity concerning the resolution 
- More flexiblity concerning the type of projection used

# Link dump
- [Explanation of Terminations](https://opendem.info/definitions.html)
- [Collection of free DEMs](https://www.opendem.info/link_dem.html)
- [GLOBE Documentation](https://www.ngdc.noaa.gov/mgg/topo/report/globedocumentationmanual.pdf)
- [Combining Projection with DEM](https://github.com/domlysz/BlenderGIS/wiki)
