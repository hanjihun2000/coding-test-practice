
int maxArea(int* h, int l){
    int m = 0;
    int n = l-1;
    
    // find area between two endpoints
    int line = h[m] < h[n] ? h[m] : h[n];
    int x = line * abs(n-m);
    int area = area < x ? x : area;
    
    for (int i = 1; i < l; i++){
        if (n == m){
            break;
        }
        while (h[n] == line && n > m){
            n = n-1;
            line = h[m] < h[n] ? h[m] : h[n];
            x = line * abs(n-m);
            area = area < x ? x : area;
        }
        if (h[i] >= line && h[m] == line){
            m = i;
            line = h[m] < h[n] ? h[m] : h[n];
            x = line * abs(n-m);
            area = area < x ? x : area;
        }
    }
    return area;
}