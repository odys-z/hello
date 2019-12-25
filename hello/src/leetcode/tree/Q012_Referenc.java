package leetcode.tree;

public class Q012_Referenc extends Q012_int2roman {

	@Override
    public String intToRoman(int num) {
        int a[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String b[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int index = 0;
        StringBuilder sb = new StringBuilder();
        while(num > 0) {
            while(num >= a[index]) {
                sb.append(b[index]);
                num-=a[index];
            }
            index++;
        }
        return sb.toString();
    }
}