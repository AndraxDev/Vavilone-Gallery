# Vavilone Gallery
Version: 1.0

This gallery contains all avaliabe and unavaliable images. Program based on autogeneration

## How to use
Place image to the same directory with processor.py and rename as ***input.png***

(Also you can use other formats, but do not forget to change file type at line 222 at ***processor.py***. Tested jpg and png. Other at you ovn risk. WARNING: Vector graphics not supported. You need to rasterize vector images first.)

Run following command:

```ssh
$ py processor.py
```

The programm convert image to decimal value and show position in gallery

Run following command to start searching by id:

```ssh
$ py cycle.py
```

Note: before run you can change values of some variables

To simple convert decimal number to image use ***search.py***
