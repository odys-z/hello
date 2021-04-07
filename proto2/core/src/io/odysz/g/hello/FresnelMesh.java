package io.odysz.g.hello;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Camera;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.VertexAttributes.Usage;
import com.badlogic.gdx.graphics.g3d.Material;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.Renderable;
import com.badlogic.gdx.graphics.g3d.model.NodePart;
import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.graphics.glutils.ShaderProgram;
import com.badlogic.gdx.math.Matrix4;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.utils.Disposable;

import io.oz.gdx.shapes.SphereShapeBuilder;

/**Using AddMesh for mesh merging.
 * Created by ody on 5/17/2017.
 */
public class FresnelMesh implements Disposable {
    public static final Vector3 fresnel = new Vector3(0.15f, 2.0f, 0.0f);
    public static final Vector3 ior = new Vector3(3.60f, 3.3f, 3.1f);

    private final int cubemapTexUnit;
//    private final Vector3 center;
//    private final Texture texture;
    private final Camera camera;
    private ShaderProgram shaderProgram;
    private Renderable renderable;

    public FresnelMesh(Camera camera, int cubeMapTextureUnit, Vector3 pos, Vector3 radius) {
        this.camera = camera;
        this.cubemapTexUnit = cubeMapTextureUnit;
//        this.center = pos;
//        this.texture = new Texture("badlogic.jpg");

        ModelBuilder modelBuilder = new ModelBuilder();
        Matrix4 mat4 = new Matrix4();
        modelBuilder.begin();
        MeshBuilder mpbuilder = (MeshBuilder) modelBuilder.part("part1", GL20.GL_TRIANGLES, Usage.Position | Usage.Normal, new Material());
        Vector3 p = new Vector3(); // center position
        //Vector3 d = new Vector3(radius).scl(2); // distance
        for (int i = 0; i < 90; i++) {
            p.x = (i % 10) * radius.x * 2 - radius.x * 5;
            p.y = (float) (Math.floor(i / 100) * radius.y * 2 - 2 * radius.y);
            p.z = (float) (Math.floor(i % 100 / 10) * -radius.z * 2 - 12 * radius.z);

            SphereShapeBuilder.build(mpbuilder, mat4.idt().translate(p), radius.x, radius.y, radius.z, 16, 16);
        }
        //mpbuilder.sphere(new Matrix4().translate(radius.x/2, 0f, 0f), radius.x, radius.y, radius.z, 36, 36);
        //mpbuilder.sphere(new Matrix4().translate(-2 * radius.x, 0f, 0f), radius.x, radius.y, radius.z, 36, 36);
        //mpbuilder.sphere(new Matrix4().translate( 2 * radius.x, 0f, 0f), radius.x, radius.y, radius.z, 36, 36);
        Model model = modelBuilder.end();
        model.calculateTransforms();

        renderable = new Renderable();
        NodePart blockPart = model.nodes.get(0).parts.get(0);
        //renderable.setRenderable(renderable);
        blockPart.setRenderable(renderable);
        renderable.environment = null;
        renderable.worldTransform.translate(pos);
        shaderProgram = new ShaderProgram(
                Gdx.files.internal("glsl/fresnel.vs").readString(),
                Gdx.files.internal("glsl/fresnel.fs").readString());
        if (!shaderProgram.isCompiled())
            System.out.println(shaderProgram.getLog());
    }

    @Override
    public void dispose() { }

    public void render() {
        shaderProgram.bind();
        setUniformsX1();
        renderable.meshPart.render(shaderProgram);
    }

    /**ex04.1.vs<pre>
        attribute vec4 a_position;
        attribute vec3 a_normal;
        attribute vec2 a_texCoord0;

        uniform vec3 CameraPos;
        uniform mat4 ModelWorld;
        uniform mat4 vpMatrix;

        uniform float mRefractionRatio;
        uniform float mFresnelBias;
        uniform float mFresnelScale;
        uniform float mFresnelPower;</pre>

     *ex04.1.fs<pre>
        uniform samplerCube tCube;
     *</pre>
     *
     * ex04.1.htm<pre>
     "mRefractionRatio": { value: 1.02 },
     "mFresnelBias": { value: 0.1 },
     "mFresnelPower": { value: 2.0 },
     "mFresnelScale": { value: 1.0 },
     ...</pre>
     */
    private void setUniformsX1() {
        shaderProgram.setUniformf("CameraPos", camera.position);
        shaderProgram.setUniformMatrix("ModelWorld", renderable.worldTransform);
        shaderProgram.setUniformMatrix("vpMatrix", camera.combined);
        shaderProgram.setUniformf("mRefractionRatio", 1.02f);
        shaderProgram.setUniformf("mFresnelBias", 0.1f);
        shaderProgram.setUniformf("mFresnelPower", 2.0f);
        shaderProgram.setUniformf("mFresnelScale", 1.0f);
        // shaderProgram.setUniformf("IoR_Values", ior);
        shaderProgram.setUniformi("tCube", cubemapTexUnit);
    }

    /**
     * ex04.7.fs<br>
     *     uniform float mRefractionRatio;<br>
     *     uniform float mFresnelBias;<br>
     *     uniform float mFresnelScale;<br>
     *     uniform float mFresnelPower;<br>
     *     uniform samplerCube tCube;
     */
    @SuppressWarnings("unused")
	private void setUniformsX7() {
        shaderProgram.setUniformf("CameraPos", camera.position);
        shaderProgram.setUniformMatrix("ModelWorld", renderable.worldTransform);
        shaderProgram.setUniformMatrix("vpMatrix", camera.combined);
        shaderProgram.setUniformf("mFresnelBias", fresnel);
        // shaderProgram.setUniformf("IoR_Values", ior);
        shaderProgram.setUniformi("tCube", cubemapTexUnit);
   }
}

