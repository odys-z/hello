/*******************************************************************************
 * Copyright 2011 See AUTHORS file.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 ******************************************************************************/

package io.oz.gdx.shapes;

import com.badlogic.gdx.graphics.g3d.utils.MeshBuilder;
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder;
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.VertexInfo;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Matrix4;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.utils.ShortArray;

/** Helper class with static methods to build sphere shapes using {@link MeshPartBuilder}.
 * @author xoppa */
public class SphereShapeBuilder extends BaseShapeBuilder {
	/**Temp center*/
	private final static Vector3 tc = new Vector3(0f, 0f, 0f);
	private final static ShortArray tmpIndices = new ShortArray();

	public static void build (MeshBuilder builder, float width, float height, float depth, int divisionsU, int divisionsV) {
		build(builder, width, height, depth, divisionsU, divisionsV, 0, 360, 0, 180);
	}

	/**Original Suggestion: use {@link MeshPartBuilder#setVertexTransform(Matrix4)} instead of using the method signature taking a matrix. */
	public static void build (MeshBuilder builder, final Matrix4 transform, float width, float height, float depth,
		int divisionsU, int divisionsV) {
		build(builder, transform, width, height, depth, divisionsU, divisionsV, 0, 360, 0, 180);
	}

	public static void build (MeshBuilder builder, float width, float height, float depth, int divisionsU, int divisionsV,
		float angleUFrom, float angleUTo, float angleVFrom, float angleVTo) {
		build(builder, matTmp1.idt(), width, height, depth, divisionsU, divisionsV, angleUFrom, angleUTo, angleVFrom, angleVTo);
	}

	/**Original Suggestion: use {@link MeshPartBuilder#setVertexTransform(Matrix4)} instead of using the method signature taking a matrix. */
	public static void build (MeshBuilder builder, final Matrix4 transform, float width, float height, float depth,
							  int divisionsU, int divisionsV, float angleUFrom, float angleUTo, float angleVFrom, float angleVTo) {
		// FIXME create better sphere method (- only one vertex for each pole, - position)
		final float hw = width * 0.5f;
		final float hh = height * 0.5f;
		final float hd = depth * 0.5f;
		final float auo = MathUtils.degreesToRadians * angleUFrom;
		final float stepU = (MathUtils.degreesToRadians * (angleUTo - angleUFrom)) / divisionsU;
		final float avo = MathUtils.degreesToRadians * angleVFrom;
		final float stepV = (MathUtils.degreesToRadians * (angleVTo - angleVFrom)) / divisionsV;
		final float us = 1f / divisionsU;
		final float vs = 1f / divisionsV;
		float u = 0f;
		float v = 0f;
		float angleU = 0f;
		float angleV = 0f;
		VertexInfo curr1 = vertTmp3.set(null, null, null, null);
		curr1.hasUV = curr1.hasPosition = curr1.hasNormal = true;

		final int s = divisionsU + 3;
		tmpIndices.clear();
		tmpIndices.ensureCapacity(divisionsU * 2);
		tmpIndices.size = s;
		int tempOffset = 0;

		// odysseus 2017-05-18
		//final float l_mat[] = transform.val;
        //float tx = l_mat[Matrix4.M03];
		//float ty = l_mat[Matrix4.M13];
		//float tz = l_mat[Matrix4.M23];
        tc.set(0, 0, 0);
		tc.mul(transform);

		builder.ensureVertices((divisionsV + 1) * (divisionsU + 1));
		builder.ensureRectangleIndices(divisionsU);
		for (int iv = 0; iv <= divisionsV; iv++) {
			angleV = avo + stepV * iv;
			v = vs * iv;
			final float t = MathUtils.sin(angleV);
			final float h = MathUtils.cos(angleV) * hh;
			for (int iu = 0; iu <= divisionsU; iu++) {
				angleU = auo + stepU * iu;
				u = 1f - us * iu;
				// Fixme : wrong normal calculation if transform
				curr1.position.set(MathUtils.cos(angleU) * hw * t, h, MathUtils.sin(angleU) * hd * t).mul(transform);

				// odysseus 2017-05-18
				// curr1.normal.set(curr1.position).nor();
                // norm = p - trans[3]
				Vector3 p = curr1.position;
				curr1.normal.set(p.x - tc.x, p.y - tc.y, p.z - tc.z).nor();

				curr1.uv.set(u, v);
				tmpIndices.set(tempOffset, builder.vertex(curr1));
				final int o = tempOffset + s;
				if ((iv > 0) && (iu > 0)) // FIXME don't duplicate lines and points
					builder.rect(tmpIndices.get(tempOffset), tmpIndices.get((o - 1) % s), tmpIndices.get((o - (divisionsU + 2)) % s),
						tmpIndices.get((o - (divisionsU + 1)) % s));
				tempOffset = (tempOffset + 1) % tmpIndices.size;
			}
		}
	}
}
