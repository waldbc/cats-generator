## Python Art Engine

### What It Does

This is a program I built with the intention of combining multiple layers of art into one final image. This kind of art generator is ideal for creating something like an NFT collection.

### Features
- Customisable rarities - Set your own rarities for each trait.
- Complete Metadata Creation - Creates metadata for each created image, and can be updated with an IPFS URI ready for use with a smart contract.
- No Duplicates - Each time a set of images are created, the program checks that it doesn't match any already created. This means every image is unique and ensures there are no duplicates

### Configuring The Files

All of the sub folders of images are placed into the assets directory. From here, head into the config file and edit the existing layers with your own directory names and desired weights, as specified in the inital comments of the config file.

### Using The Program

Upon running the main.py file, the program will prompt the user for some details about the collection, e.g. the name, description and amount desired. Once this information has been given, the program will begin.

### Improving The Program

This program was a fun challenge to build. I decided to do this from scratch without following any other projects which helps me improve my knowledge.

The code itself initially had quite a lot of global variables, which I managed to pass into the functions instead to avoid this. I think the actual structure of the program could be improved a bit; I toyed with the idea of nesting the functions within main to give it enough scope - However I was unsure. I suppose with more features a class structure could also be considered.

I think a very beneficial feature would be to allow for easier control of non-required layers. Currently an transparent png is simply added to represent the absence of a layer, but having the program decide this for itself would be more beneficial.

Another useful feature might be an option to decide the size of the images created. Currently the program uses the dimensions of the given images, but it may be useful to be able to shrink these to reduce file size or if a higher resolution is unnecessary.