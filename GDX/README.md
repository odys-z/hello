# TODO

- [gdx 2D texture packer and physics editor](https://github.com/libgdx/libgdx/wiki/Texture-packer#textureatlas)

[tutorial](https://www.codeandweb.com/texturepacker/tutorials/libgdx-physics)

One thing that's very important to realize when working with LibGDX, is that you
cannot instantiate most LibGDX classes outside of the create() method. As a Java
programmer, you might instinctively want to do something like this:

```
    // BAD EXAMPLE
    final SpriteBatch batch = new SpriteBatch();
    final Texture img = new Texture("badlogic.jpg");
```

Go ahead and try that now to see what I happens. You should get an UnsatisfiedLinkError.
This is because LibGDX uses a native library, which needs to be loaded into memory
before we can start working with it. So the only only safe place we have to instantiate
LibGDX objects is in the create method.

- [BDX](https://github.com/GoranM/bdx)

[reading](https://www.gamefromscratch.com/post/2015/03/16/Create-a-3D-game-in-Blender-using-LibGDX-and-BDX.aspx)
