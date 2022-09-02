class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $collection = [];
        foreach($nums as $i=>$v){
            $remain = $target - $v;
            
            if(isset($collection[$remain])){
                return [$i, $collection[$remain]];
            }
            else{
                $collection[$v] = $i;
            }
        }
        
        return [0, 0];
    }
}