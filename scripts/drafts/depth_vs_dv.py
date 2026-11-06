"""DRAFT, not used on the site: absolute DV versus surface depth for the coordinates page. Not ready (2026-11-06). Run: python scripts/drafts/depth_vs_dv.py out.svg"""
import math, sys
FONT = "Roboto, 'Helvetica Neue', Arial, sans-serif"
INK, GREY, DV = "#1d1d1f", "#5c5c66", "#4b5ba0"
SKULL, SKULL_S, BRAIN, BRAIN_S, PROBE = "#e9dabb", "#b59f74", "#dcb6ae", "#a7756c", "#3a3a40"

def q(p0, p1, p2, t):
    return tuple((1 - t) ** 2 * a + 2 * (1 - t) * t * b + t ** 2 * c for a, b, c in zip(p0, p1, p2))

def y_at(p0, p1, p2, x):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        if q(p0, p1, p2, m)[0] < x: lo = m
        else: hi = m
    return q(p0, p1, p2, lo)[1]

def panel(ox, mode):
    out = []
    a = lambda s: out.append(s)
    S0, S1, S2 = (ox + 96, 236), (ox + 370, 66), (ox + 690, 196)          # outer skull, over the cortex and cerebellum
    B0, B1, B2 = (ox + 126, 270), (ox + 372, 112), (ox + 612, 214)        # dorsal brain surface
    a(f'<ellipse cx="{ox+86}" cy="{304}" rx="46" ry="30" fill="{BRAIN}" stroke="{BRAIN_S}" stroke-width="2"/>')
    a(f'<path d="M{ox+640} {300} C{ox+680} {330} {ox+700} {380} {ox+736} {440} L{ox+700} {452} C{ox+676} {410} {ox+650} {380} {ox+600} {372} Z" fill="{BRAIN}" stroke="{BRAIN_S}" stroke-width="2"/>')
    a(f'<path d="M{ox+600} {206} C{ox+660} {196} {ox+712} {236} {ox+704} {300} C{ox+700} {340} {ox+650} {350} {ox+606} {336} Z" fill="{BRAIN}" stroke="{BRAIN_S}" stroke-width="2"/>')
    a(f'<path d="M{ox+626} {232} Q{ox+668} {226} {ox+690} {256} M{ox+620} {262} Q{ox+668} {256} {ox+694} {284} M{ox+616} {292} Q{ox+660} {290} {ox+690} {312}" fill="none" stroke="{BRAIN_S}" stroke-width="1.5" opacity="0.7"/>')
    a(f'<path d="M{B0[0]} {B0[1]} Q{B1[0]} {B1[1]} {B2[0]} {B2[1]} C{ox+640} {260} {ox+640} {340} {ox+600} {372} C{ox+520} {420} {ox+330} {430} {ox+210} {400} C{ox+150} {384} {ox+112} {330} {B0[0]} {B0[1]} Z" fill="{BRAIN}" stroke="{BRAIN_S}" stroke-width="2"/>')
    a(f'<path d="M{S0[0]} {S0[1]} Q{S1[0]} {S1[1]} {S2[0]} {S2[1]} L{S2[0]-6} {S2[1]+22} Q{S1[0]} {S1[1]+24} {S0[0]+8} {S0[1]+20} Z" fill="{SKULL}" stroke="{SKULL_S}" stroke-width="2"/>')
    # bregma and its level
    bx = ox + 300; by = y_at(S0, S1, S2, bx)
    a(f'<path d="M{ox+20} {by:.1f} L{ox+740} {by:.1f}" stroke="{DV}" stroke-width="2" stroke-dasharray="8 7" opacity="0.8"/>')
    # probe: positive AP angle, top leaning anterior (left), tip pointing posterior (right)
    th = math.radians(20); d = (math.sin(th), math.cos(th))
    ex = ox + 400; ey = y_at(B0, B1, B2, ex)
    L = 200; tx, ty = ex + L * d[0], ey + L * d[1]
    sx, sy = ex - 120 * d[0], ey - 120 * d[1]
    a(f'<path d="M{sx:.1f} {sy:.1f} L{tx:.1f} {ty:.1f}" stroke="{PROBE}" stroke-width="5" stroke-linecap="round"/>')
    a(f'<circle cx="{bx}" cy="{by:.1f}" r="7" fill="{INK}"/>')
    a(f'<text x="{bx-14}" y="{by-22:.0f}" font-size="26" text-anchor="end" fill="{INK}">Bregma</text>')
    a(f'<path d="M{bx-12} {by-18:.0f} L{bx-4} {by-8:.0f}" stroke="{INK}" stroke-width="2"/>')
    # AP dimension along the bottom
    yb = 512
    def hdim(x1, x2, label):
        a(f'<path d="M{x1:.1f} {yb-14} L{x1:.1f} {yb+14} M{x2:.1f} {yb-14} L{x2:.1f} {yb+14}" stroke="{INK}" stroke-width="2"/>')
        a(f'<path d="M{x1+4:.1f} {yb} L{x2-4:.1f} {yb}" stroke="{INK}" stroke-width="2" marker-start="url(#ah)" marker-end="url(#ah)"/>')
        a(f'<text x="{(x1+x2)/2:.1f}" y="{yb+40}" font-size="24" text-anchor="middle" fill="{INK}">{label}</text>')
    a(f'<path d="M{bx} {by+8:.1f} L{bx} {yb-14}" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    if mode == "absolute":
        a(f'<path d="M{tx:.1f} {by:.1f} L{tx:.1f} {yb-14}" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="4 5"/>')
        hdim(bx, tx, "AP of the target")
        a(f'<path d="M{tx+34:.1f} {by+4:.1f} L{tx+34:.1f} {ty-4:.1f}" stroke="{DV}" stroke-width="3" marker-end="url(#ahdv)"/>')
        a(f'<path d="M{tx+22:.1f} {by:.1f} L{tx+46:.1f} {by:.1f}" stroke="{DV}" stroke-width="3"/>')
        a(f'<text x="{tx+50:.1f}" y="{(by+ty)/2:.0f}" font-size="26" fill="{DV}">DV</text>')
        a(f'<text x="{tx+50:.1f}" y="{(by+ty)/2+28:.0f}" font-size="20" fill="{DV}">from Bregma level,</text>')
        a(f'<text x="{tx+50:.1f}" y="{(by+ty)/2+52:.0f}" font-size="20" fill="{DV}">positive ventral</text>')
        a(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="8" fill="#fff" stroke="{INK}" stroke-width="3"/>')
        a(f'<text x="{tx-16:.1f}" y="{ty+8:.0f}" font-size="22" text-anchor="end" fill="{INK}">target</text>')
        title = "Absolute coordinates: AP, ML, DV"
        sub = "locate the target; DV is vertical, from Bregma"
    else:
        a(f'<path d="M{ex:.1f} {ey:.1f} L{ex:.1f} {yb-14}" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="4 5"/>')
        hdim(bx, ex, "AP of the entry point")
        nx, ny = d[1], -d[0]                      # offset the depth arrow beside the probe
        o = 26
        a(f'<path d="M{ex+o*nx:.1f} {ey+o*ny:.1f} L{tx+o*nx-6*d[0]:.1f} {ty+o*ny-6*d[1]:.1f}" stroke="{INK}" stroke-width="3" marker-end="url(#ah)"/>')
        a(f'<path d="M{ex+(o-12)*nx:.1f} {ey+(o-12)*ny:.1f} L{ex+(o+12)*nx:.1f} {ey+(o+12)*ny:.1f}" stroke="{INK}" stroke-width="3"/>')
        a(f'<text x="{tx+o*nx+10:.1f}" y="{(ey+ty)/2+10:.0f}" font-size="26" fill="{INK}">Depth</text>')
        a(f'<text x="{tx+o*nx+10:.1f}" y="{(ey+ty)/2+38:.0f}" font-size="20" fill="{INK}">along the probe,</text>')
        a(f'<text x="{tx+o*nx+10:.1f}" y="{(ey+ty)/2+62:.0f}" font-size="20" fill="{INK}">from brain contact</text>')
        a(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="8" fill="#fff" stroke="{INK}" stroke-width="3"/>')
        a(f'<path d="M{ex+7:.1f} {ey-7:.1f} L{ex+44:.1f} {ey-46:.1f}" stroke="{INK}" stroke-width="1.5"/>')
        a(f'<text x="{ex+48:.1f}" y="{ey-50:.0f}" font-size="22" fill="{INK}">entry point</text>')
        a(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="5" fill="{INK}"/>')
        title = "Surface coordinates with depth: AP, ML, depth"
        sub = "locate the entry point on the brain; depth follows the probe"
    a(f'<text x="{ox+30}" y="40" font-size="30" font-weight="500" fill="{INK}">{title}</text>')
    a(f'<text x="{ox+30}" y="600" font-size="22" fill="{GREY}">{sub}</text>')
    return out

W, H = 1640, 640
parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="{FONT}">',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#1d1d1f"/></marker>',
         f'<marker id="ahdv" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{DV}"/></marker></defs>',
         f'<rect width="{W}" height="{H}" fill="#fff"/>']
parts += panel(0, "absolute") + panel(860, "surface")
# anterior marker
parts.append(f'<text x="{W/2:.0f}" y="{H-8}" font-size="20" text-anchor="middle" fill="{GREY}">anterior ← sagittal section → posterior; positive AP angle: the top of the probe leans anterior</text>')
parts.append('</svg>')
open(sys.argv[1], "w").write("\n".join(parts))
