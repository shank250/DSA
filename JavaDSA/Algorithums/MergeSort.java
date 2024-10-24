public class MergeSort {
    private static void divide(int[] arr, int start, int end){
        if(start < end){
            int mid = start + (end - start)/2;
            
            divide(arr, start, mid);
            divide(arr, mid + 1, end);
        
            conquer(arr, start, mid, end);
        }
    }
    private static void conquer(int[] arr, int start, int mid, int end){

        int[] merged = new int[end - start + 1];

        int ind1 = start, ind2 = mid + 1, k = 0;
        
        while(ind1 <= mid && ind2 <= end){
            if(arr[ind1] <= arr[ind2]){
                merged[k] = arr[ind1];
                ind1++; 
            }else{
                merged[k] = arr[ind2];
                ind2++;
            }
            k++;
        }

        while (ind1 <= mid) {
            merged[k] = arr[ind1];
            k++;
            ind1++;
        }

        while (ind2 <= end) {
            merged[k] = arr[ind2];
            k++;
            ind2++;
        }
        k = 0;
        for(int j = start; k <= end - start; k++, j++){
            arr[j] = merged[k];
        }
        
        return;
    }

    public static void main(String[] args) {
        int[] dummyarr = new int[]{2, 6, 1, 7, 2, 5};
        
        divide(dummyarr, 0, dummyarr.length - 1);

        for(int ele: dummyarr){
            System.out.print(ele);
        }
        
        System.out.println();        

    }
}
