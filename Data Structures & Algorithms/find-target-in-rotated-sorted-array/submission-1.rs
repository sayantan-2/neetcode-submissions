impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut l, mut r) = (0i32, nums.len() as i32 - 1);

        while l <= r {
            let mid = (l + r) / 2;
            if target == nums[mid as usize] {
                return mid;
            }

            if nums[l as usize] <= nums[mid as usize] {
                if target > nums[mid as usize] || target < nums[l as usize] {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                if target < nums[mid as usize] || target > nums[r as usize] {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        -1
    }
}