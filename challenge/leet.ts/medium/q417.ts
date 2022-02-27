/**
 * 417. Pacific Atlantic Water Flow
 * https://leetcode.com/problems/pacific-atlantic-water-flow/
 */

class Land {
    x: number;
    y: number;
    h: number;
    vp: boolean;
    va: boolean;
    p: boolean;
    a: boolean;

    constructor(x: number, y: number, h: number) {
        this.x = x, this.y = y, this.h = h;
        this.vp = false, this.va = false, this.p = false, this.a = false;
    }
}

type Dxy = {
    x: -1 | 0 | 1;
    y: -1 | 0 | 1;
}

/**
 *  70.21%
 * @param heights 
 * @returns 
 */
function pacificAtlantic(heights: Array<Array<number | Land>>) : Array<number[]> {
    if (!heights || heights.length == 0)
        return [];

    let X = heights[0].length, Y = heights.length;

    // let lands = new Land[Y][X]; // [ [Land(x, y, heights[y][x]) for y in range(Y)] for x in range(X) ]
    
    function flow2Pacific(land: Land, d: Dxy) : Land | undefined {
        let x = land.x,  y = land.y, h = land.h;
        let x1 = x + d.x, y1 = y + d.y;

        if (0 <= x1 && x1 < X && 0 <= y1 && y1 < Y) {
            let nxtland = heights[y1][x1] as Land;
            if (h > nxtland.h || nxtland.vp)
                return undefined;
            else
                return nxtland;
        }
        else return undefined;
    }

    function flow2Atlantic(land: Land, d: Dxy) : Land | number {
        let x = land.x, y = land.y, h = land.h;
        let x1 = x + d.x, y1 = y + d.y;

        if (0 <= x1 && x1 < X && 0 <= y1 && y1 < Y) {
            let nxtland = heights[y1][x1] as Land;
            if (h > nxtland.h || nxtland.va)
                return undefined;
            else
                return nxtland;
        }
        else return undefined;
    }

    // Pacific, Atlantic
    let P = [];
    let A = [];
    
    for( let x = 0; x < X; x++ )
    for( let y = 0; y < Y; y++ ) {
        let h = heights[y][x] as number;
        let land = new Land(x, y, h);

        if (x == 0 || y == 0) {
            land.vp = true, land.p = true;
            P.push(land);
        }
        if (y == Y-1 || x == X-1) {
            land.va = true, land.a = true;
            A.push(land);
        }
        heights[y][x] = land;
    }

    // Pacific flood - unknown Atlantic
    while ( P.length > 0 ) {
        let P_ = [] 
        
        for (var p of P) {
            for (var dxy of [{x: 0, y: 1}, {x: 1, y: 0}, {x: 0, y: -1}, {x: -1, y: 0}] as Dxy[]) {
                let nxt = flow2Pacific(p, dxy);
                
                if (nxt) {
                    nxt.p = true;
                    nxt.vp = true;
                    P_.push(nxt);
                }
            }
        }
        P = P_;
    }
        
    let both = [] as Array<number[]>;
    // Atlantic flood - known Pacific
    while (A.length > 0) {
        let A_ = [] 
        
        for (let a of A) {
            for (var dxy of [{x: 0, y: 1}, {x: 1, y: 0}, {x: 0, y: -1}, {x: -1, y: 0}] as Dxy[]) {
                let nxt = flow2Atlantic(a, dxy);
                
                if (nxt) {
                    (nxt as Land).a = true;
                    (nxt as Land).va = true;
                    A_.push(nxt)
                }
            }
            
            if (a.a && a.p)
                both.push([a.y, a.x])
        }

        A = A_;
    }
    console.log(both);
    return both
}

export default pacificAtlantic;