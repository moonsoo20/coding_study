class Solution {
    public int solution(int n, int t) {
        int temp = n;

        for (int i = 0; i < t; i++) {
            temp *= 2; 
        }
        return temp;
    }
}