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
            $vNum1 = !empty($v1[$i]) ? intval($v1[$i]) : 0;
            $vNum2 = !empty($v2[$i]) ? intval($v2[$i]) : 0;
            
            if($vNum1 < $vNum2){
                return -1;
            }
            elseif($vNum1 > $vNum2){
                return 1;
            }
        }
        
        return 0;
        
        
        /*
        if ($version1===$version2) return 0;
		$v1 = explode('.', $version1);
		$v2 = explode('.', $version2);
		$l1 =count($v1);
		$l2 =count($v2);
		$len = min($l1, $l2);
		$i=0;
		while ($i<$len)  {
			$t1 =  intval($v1[$i], 10);
			$t2 =  intval($v2[$i++], 10);
			if ($t1<$t2) return -1;
			elseif ($t1>$t2) return 1;
		}
		if ($l1===$l2) return 0;
		$i=$len;
		if ($l1<$l2) {
			while ( $i<$l2) {
				if (intval($v2[$i++], 10)>0) return -1;
			}
		} else {
			while ( $i<$l1) {
				if (intval($v1[$i++], 10)>0) return 1;
			}
		}
		return 0;
        */
    }
}