# -----------------------------------------------------------------------------
# Python & OpenGL for Scientific Visualization
# www.labri.fr/perso/nrougier/python+opengl
# Copyright (c) 2018, Nicolas P. Rougier
# Distributed under the 2-Clause BSD License.
# -----------------------------------------------------------------------------
import math
from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;
    attribute vec4 color;
    uniform float theta;
    varying vec4 v_color;
    void main() {
        float c = cos(theta);
        float s = sin(theta);
        float x = c*position.x - s*position.y;
        float y = s*position.x + c*position.y;
        gl_Position = vec4(0.7*vec2(x,y), 0.0, 1.0);
        v_color = color;
    } """ 

fragment = """
    varying vec4 v_color;
    void main() { gl_FragColor = v_color; } """


window = app.Window(color=(1,1,1,1))
quad = gloo.Program(vertex, fragment, count=4)
quad['position'] = (-1,+1), (+1,+1), (-1,-1), (+1,-1)
quad['color'] = (1,1,0,1), (1,0,0,1), (0,0,1,1), (0,1,0,1)

angle = 0.0
@window.event
def on_draw(dt):
    global angle
    angle += 1.0 * math.pi/180.0
    window.clear()
    quad["theta"] = angle
    quad.draw(gl.GL_TRIANGLE_STRIP)

# We set the framecount to 360 in order to record a movie that can
# loop indefinetly. Run this program with:
# python quad-scale.py --record quad-scale.mp4
app.run(framecount=360)
