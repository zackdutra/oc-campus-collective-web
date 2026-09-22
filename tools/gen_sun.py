import math
def sun_svg(cx, cy, r, ray_stroke=True):
    # rays: (angle deg, math convention y-up, outer radius as multiple of r)
    rays=[(156,1.72),(118,2.2),(82,2.3),(47,1.95),(4,2.1),(-21,1.7)]
    rin=1.24; hw=0.15
    out=[]
    for ang,ro in rays:
        a=math.radians(ang); t=math.radians(ang+90)
        bx,by=cx+math.cos(a)*rin*r, cy-math.sin(a)*rin*r
        tx,ty=cx+math.cos(a)*ro*r,  cy-math.sin(a)*ro*r
        ox,oy=math.cos(t)*hw*r, -math.sin(t)*hw*r
        pts=f"{bx+ox:.1f},{by+oy:.1f} {tx:.1f},{ty:.1f} {bx-ox:.1f},{by-oy:.1f}"
        out.append(f'<polygon points="{pts}" fill="#ffcf67" stroke="#ffcf67" stroke-width="{0.05*r:.1f}" stroke-linejoin="round"/>')
    return "\n".join(out)

def hero(width, blue_y, dy, r, cx, blue_thick, yel_thick, ctrl_y):
    # arch: M -100 blue_y C w*0.28 ctrl_y, w*0.78 ctrl_y, width+100 blue_y
    def arch(y0, cy_): return f"M-100 {y0} C {width*0.28:.0f} {cy_}, {width*0.78:.0f} {cy_}, {width+100} {y0}"
    # sun center sits on the blue line at x=cx: approximate bezier y at that x
    # sample bezier to find y at cx
    def bez(t,p0,p1,p2,p3): return (1-t)**3*p0+3*(1-t)**2*t*p1+3*(1-t)*t*t*p2+t**3*p3
    best=None
    for i in range(2001):
        t=i/2000; x=bez(t,-100,width*0.28,width*0.78,width+100)
        if best is None or abs(x-cx)<abs(best[0]-cx): best=(x,bez(t,blue_y,ctrl_y,ctrl_y,blue_y))
    cy=best[1]
    clip_off=0.6*r
    s=f'''<defs>
  <clipPath id="sunclip"><path d="{arch(blue_y+clip_off, ctrl_y+clip_off)} L {width+100} -200 L -100 -200 Z"/></clipPath>
  <clipPath id="blueclip"><rect x="-100" y="-200" width="{cx-r+100:.0f}" height="1000"/></clipPath>
</defs>
<g clip-path="url(#sunclip)">
  <circle cx="{cx}" cy="{cy:.1f}" r="{r}" fill="#ffcf67"/>
</g>
{sun_svg(cx,cy,r)}
<path d="{arch(blue_y, ctrl_y)}" fill="none" stroke="#a9c4e0" stroke-width="{blue_thick}" stroke-linecap="round" clip-path="url(#blueclip)"/>
<path d="{arch(blue_y+dy, ctrl_y+dy)}" fill="none" stroke="#ffcf67" stroke-width="{yel_thick}" stroke-linecap="round"/>'''
    return s

import sys
which=sys.argv[1]
if which=='hero':
    body=hero(1400, 190, 41, 52, 1000, 11, 14, 78)
    print(f'    <svg class="sunrise" viewBox="0 -40 1400 300" aria-hidden="true" focusable="false">\n{body}\n    </svg>')
elif which=='og':
    body=hero(1200, 168, 41, 52, 960, 11, 14, 58)
    print(f'<svg viewBox="0 -40 1200 270">\n{body}\n</svg>')
elif which=='compare':
    # isolated sun at logo-like scale for side-by-side
    body=hero(700, 200, 41, 52, 480, 11, 14, 150)
    print(f'<svg viewBox="100 40 500 260" width="1000" height="520">{body}</svg>')
