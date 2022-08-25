class Solution {

    /**
     * @param String $version1
     * @param String $version2
     * @return Integer
     */
    function compareVersion($version1, $version2) {
        $v1 = explode('.', $version1);
        $v2 = explode('.', $version2);
            
        $max = max(count($v1), count($v2));
        
        for($i=0; $i<$max; $i++){
            $vNum1 = !empty($v1[$i]) ? (int) $v1[$i] : 0;
            $vNum2 = !empty($v2[$i]) ? (int) $v2[$i] : 0;
            
            if($vNum1 < $vNum2){
                return -1;
            }
            elseif($vNum1 > $vNum2){
                return 1;
            }
        }
        
        return 0;
    }
}