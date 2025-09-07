package companies.oracle.java;

class Solution2 {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int numIslands = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    explore(grid, r, c);
                    numIslands++;
                }
            }
        }
        return numIslands;
    }

    public boolean explore(char[][] grid, int row, int col) {
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length) {
            return false;
        }
        if (grid[row][col] == '0') {
            return false;
        }
        grid[row][col] = '0';
        explore(grid, row - 1, col);
        explore(grid, row + 1, col);
        explore(grid, row, col - 1);
        explore(grid, row, col + 1);

        return true;
    }

    public static void main(String[] args) {
        Solution2 sol = new Solution2();
        char[][] arr = {{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}};
        System.out.println(sol.numIslands(arr));
        char[][] arr2 = {{'1','1','0','0','0'},{'1','1','0','0','0'},{'0','0','1','0','0'},{'0','0','0','1','1'}};
        System.out.println(sol.numIslands(arr2));
    }
}
