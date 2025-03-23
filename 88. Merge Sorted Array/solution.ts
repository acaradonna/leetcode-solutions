/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    // First let's make 3 pointers - one for the end of nums1, one for the end of nums2 and one for the end of our returned array
    let p1 = m - 1;
    let p2 = n - 1;
    let p = m + n - 1;

    // Now we can iterate through the arrays, comparing the values at the end of each and placing the largest value at the end of nums1
    while (p2 >= 0) {
        if (p1 >= 0 && nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1];
            p1--;
        } else {
            nums1[p] = nums2[p2];
            p2--;
        }
        p--;
    }
};