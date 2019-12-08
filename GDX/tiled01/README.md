# Import Project

    Android Studio -> Open
    path = tiled01/build.gradle

# Resource

[A QUICK LOOK AT TILED. AN OPEN SOURCE 2D LEVEL EDITOR](https://www.gamefromscratch.com/post/2014/04/15/A-quick-look-at-Tiled-An-open-source-2D-level-editor.aspx)

[LIBGDX TUTORIAL 11: TILED MAPS PART 1: SIMPLE ORTHOGONAL MAPS](https://www.gamefromscratch.com/post/2014/04/16/LibGDX-Tutorial-11-Tiled-Maps-Part-1-Simple-Orthogonal-Maps.aspx)

Resource from [Create a Canvas Tileset Background](http://blog.sklambert.com/create-a-canvas-tileset-background/)

# TMX

map w32h32.tmx
```
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.2" tiledversion="1.3.1" orientation="orthogonal" renderorder="right-down" compressionlevel="0" width="32" height="32" tilewidth="32" tileheight="32" infinite="0" nextlayerid="4" nextobjectid="10">
 <tileset firstgid="1" source="t01.tsx"/>
 <layer id="1" name="tiles01" width="32" height="32">
  <data encoding="base64" compression="zlib">
   eAHtl1...
  </data>
 </layer>
 <objectgroup id="3" name="static bodies">
  <object id="3" name="rock" x="633" y="485" width="147" height="186">
   <properties>
    <property name="rigid" value="true"/>
   </properties>
  </object>
  ...
  </objectgroup>
 ...
 <objectgroup id="11" name="players">
  <object id="12" name="fairyA" x="368" y="868" width="33" height="12">
   <ellipse/>
  </object>
 </objectgroup>
 <layer id="2" name="Tile Layer 2" width="32" height="32">
  <data encoding="base64" compression="zlib">
   eAHd1...
  </data>
 </layer>
</map>
```

tileset t01.tsx
```
<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.2" tiledversion="1.3.1" name="t01" tilewidth="32" tileheight="32" tilecount="256" columns="16">
 <properties>
  <property name="b2d type" type="int" value="0"/>
 </properties>
 <image source="tileset.png" width="512" height="512"/>
 <tile id="236">
  <animation>
   <frame tileid="167" duration="100"/>
   <frame tileid="168" duration="100"/>
   <frame tileid="151" duration="2200"/>
   <frame tileid="151" duration="100"/>
   <frame tileid="151" duration="100"/>
   <frame tileid="151" duration="100"/>
  </animation>
 </tile>
</tileset>
```

# Load a tiled TMX map

To load tiled map, see core/Tiled01.java

```
    @Override
    public void create () {
        tiledMap = new TmxMapLoader().load("w32h32.tmx");
        tiledMapRenderer = new OrthogonalTiledMapRenderer(tiledMap);
        ...
    }

    @Override
    public void render () {
        tiledMapRenderer.setView(camera);
        tiledMapRenderer.render();
    }
```

<img src='./readme/003 map-loaded.png' width='600px'><img>

## How does map data managed

Tiled map are managed by class from package com.badlogic.gdx.maps.tiled.

To access map layer:
```
    MapObjects objs = tiledMap.getLayers().get("static bodies").getObjects();
    TiledMapTileSets tilesets = tiledMap.getTileSets();
````
Map cell can be accessed with row / column index. These line print a char map at
system console;
```
    TiledMapTileLayer tilayer = (TiledMapTileLayer) tiledMap.getLayers().get("tiles01");
    int tw = tilayer.getWidth();
    int th = tilayer.getHeight();
    System.out.println(String.format("w: %s, h: %s", tw, th));
    for (int r = th - 1; r > 0; r--) {
        for (int c = 0; c < tw; c ++) {
            TiledMapTileLayer.Cell cell = tilayer.getCell(c, r);
            TiledMapTile t = cell.getTile();
            if (t.getId() == 79)
                System.out.print("   ");
            else if (t.getId() >= 230)
                System.out.print("[O]");
            else
                System.out.print("[ ]");
        }
        System.out.println("|");
    }
```

output:
```
    w: 32, h: 32
    [O][O]                              [ ][ ]                                                      |
    [O][O]                              [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
                                        [ ][ ]                                                      |
    [ ][ ][ ][ ][ ][ ]                  [ ][ ]                                                      |
    [ ][ ][ ][ ][ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
                [ ][ ]                  [ ][ ]                                                      |
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]                                                |
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]                                                |
                [ ][ ]                        [ ][ ]                                                |
                [ ][ ]                        [ ][ ]                                                |
                [ ][ ]                        [ ][ ]                                                |
                [ ][ ]                        [ ][ ][ ][ ]                                          |
                [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]                                          |
                [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]   [ ][ ]                                          |
                                                    [ ][ ]                                          |
                                                    [ ][ ]                                          |
                                                    [ ][ ]                                          |
```

- Tile layer is base64 and zipped

See map file above,
```
    <layer id="1" name="tiles01" width="32" height="32">
        <data encoding="base64" compression="zlib">
            eAHtl1...
        </data>
```

Tile map layer is actually array of tile id<int>. ids loaded for w32h32.tmx are:

```
 239 240 ___  77 168 ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 255 256 ___ 237 252 ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 184 185 184 185 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 200 201 200 201 200 201 ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 184 185 184 185 200 201 184 185 184 185 184 185 184 185 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 200 201 200 201 184 185 200 201 200 201 200 201 200 201 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ 184 185 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 184 185 185 185 185 185 185 184 185 201 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ 200 201 200 201 201 201 201 201 201 200 201 ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 184 185 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 200 201 ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
```
where " ___ " stands for 79.
Each tile id is increased by 1.

For example, the animated tile (236) in tileset is id = 236, but laoded as 237
(row 1, column 3).

The zipped data is extracted in method
```
   int[] com.badlogic.gdx.maps.tiled.BaseTmxMapLoader.getTileIds(Element element, int width, int height),
```
with java.util.zip.GZIPInputStream.GZIPInputStream for compression = glib and
java.util.zip.InflaterInputStream.InflaterInputStream for compression = zlib

- Tileset ids are calculated, not stored in map

Tilesets are loaded by TmxMapLoader.loadTileset()
```
Tiled01.create() {
    tiledMap = new TmxMapLoader().load("w32h32.tmx")
        ->  TileMap.load("w32h32.tmx")
            ->  TmxMapLoader.loadTilemap(root = <map nextlayerid="4" ...)
                ->  TmxMapLoader.loadTileset(root = <map nextlayerid="4" ...)
}
```

in loadTileset():
```
    for (int y = margin; y <= stopHeight; y += tileheight + spacing) {
            for (int x = margin; x <= stopWidth; x += tilewidth + spacing) {
                TextureRegion tileRegion = new TextureRegion(texture, x, y, tilewidth, tileheight);
                TiledMapTile tile = new StaticTiledMapTile(tileRegion);
                tile.setId(id);
                tile.setOffsetX(offsetX);
                tile.setOffsetY(flipY ? -offsetY : offsetY);
                tileset.putTile(id++, tile);
            }
        }
```
where stopHeight = textureHeight - tileHeight.

For t01.tsx, the loaded tileset.tiles is a size of 256 (16x16) IntMap, each element
is a com.badlogic.gdx.maps.tiled.tiles.StaticTiledMapTile object.

- How do animated tiles been rendered

In tsx tileset file, tile animation are defined as child of a tile.

<img src='./readme/001 tiled-anim-tileid.png' width='600px'></img>

Tile at row 15, col 27 is 236, which is animated in Tiled editor.

According to [TMX 1.3.1](https://doc.mapeditor.org/en/stable/reference/tmx-map-format/#animation),
each tile can have exactly one animation associated with it. In the future,
there could be support for multiple named animations on a tile.

Animation is defined in tileset.tsx.
```
<tile id="236">
 <animation>
  <frame tileid="167" duration="100"/>
  <frame tileid="168" duration="100"/>
  <frame tileid="151" duration="2200"/>
  <frame tileid="151" duration="100"/>
  <frame tileid="151" duration="100"/>
  <frame tileid="151" duration="100"/>
 </animation>
</tile>
```

It's been load by TmxMapLoader.loadTileset(), as instances of AnimatedTiledMapTile.
```
    if (animationElement != null) {

        Array<StaticTiledMapTile> staticTiles = new Array<StaticTiledMapTile>();
        IntArray intervals = new IntArray();
        for (Element frameElement: animationElement.getChildrenByName("frame")) {
            staticTiles.add((StaticTiledMapTile) tileset.getTile(firstgid + frameElement.getIntAttribute("tileid")));
            intervals.add(frameElement.getIntAttribute("duration"));
        }

        AnimatedTiledMapTile animatedTile = new AnimatedTiledMapTile(intervals, staticTiles);
        animatedTile.setId(tile.getId());
        animatedTiles.add(animatedTile);
        tile = animatedTile;
    }
```

The AnimatedTiledMapTile class override getTextureRegion() method, which is called by
OrthoCachedTiledMapRenderer.renderTileLayer(). In getTextureRegion(), the currrent
frame index is changed according to a time stamp, lastTiledMapRenderTime, which is
updated each time by application rendering call to OrthoCachedTiledMapRenderer.render().

Loaded animated tiles are an array of tiles. Break at OrthoCachedTiledMapRenderer.
renderTileLayer(), tiles 236 is rendered with an array of StaticTiledMapTile.

<img src='./readme/001 as-debug-animtile.png' width='600px'><img>

Here is the frameTiles' value:
```
((AnimatedTiledMapTile) tile).frameTiles = {StaticTiledMapTile[6]@2464}
 0 = {StaticTiledMapTile@2493}
  id = 168
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2496}
  offsetX = 0.0
  offsetY = 0.0
 1 = {StaticTiledMapTile@2494}
  id = 169
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2497}
  offsetX = 0.0
  offsetY = 0.0
 2 = {StaticTiledMapTile@2495}
  id = 152
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2498}
  offsetX = 0.0
  offsetY = 0.0
 3 = {StaticTiledMapTile@2495}
  id = 152
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2498}
  offsetX = 0.0
  offsetY = 0.0
 4 = {StaticTiledMapTile@2495}
  id = 152
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2498}
  offsetX = 0.0
  offsetY = 0.0
 5 = {StaticTiledMapTile@2495}
  id = 152
  blendMode = {TiledMapTile$BlendMode@1458} "ALPHA"
  properties = null
  objects = null
  textureRegion = {TextureRegion@2498}
  offsetX = 0.0
  offsetY = 0.0
```
