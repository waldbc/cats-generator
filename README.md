# Python Generative Art Engine

Python program focused on creating generative NFT collections based on layers of art. 

## Project Goals

Making an easy and accessible generative art program for programmers and non-programmers alike. 
The source is written in **python** to be accessible for everybody and easy to contribute.


## Dependencies
* Pillow (PIL Fork)
* All other dependencies come built-in with Python.

## How to use

Drop all of your organised folders of layers into the assets folder.

In the `config.py` file, simply replace the default folder names with your folder names,
and set required value to `True` or `False` depending on whether it is a mandatory layer or not.

### Setting the Rarities

The values in the rarities represent how often you want each layer to occur as a percentage out of 100.

For example, if you have two backgrounds, you may set the rarities to `[80, 20]`. 

The rarities should be in the same order as the layers are in the folder (typically alphabetical).

If the layer is *not* mandatory - e.g. a hat/accessory - add an extra value into rarities to represent the None value.

For example, if you have two hats, you could set the rarities as `[60, 30, 10]`. This means the first accessory will occur 60% of the time, the second 30% of the time, and *no accessory* 10% of the time.

## Contributing

1.  Fork it!
2.  Create your feature branch: `git checkout -b my-new-feature`
3.  Commit your changes: `git commit -m 'Add some feature'`
4.  Push to the branch: `git push origin my-new-feature`
5.  Submit a pull request

## License
MIT © [lapsha-dev](https://github.com/lapsha-dev)