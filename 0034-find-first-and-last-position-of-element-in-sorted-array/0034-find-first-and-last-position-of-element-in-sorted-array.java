class Solution {
    public int[] searchRange(int[] nums, int target) {
        int arr[]=new int[2];
        arr[0]=-1;
        arr[1]=-1;

        for(int i=0;i<nums.length;i++){
            if(target==nums[i]){
                arr[1]=i;
            }
        }

        for(int i=(nums.length)-1;i>=0;i--){
            if(target==nums[i]){
                arr[0]=i;
            }
        }

        return arr;
    }
}