<?php

$data = array(5, 2, 3, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14);
print_r($data);
$length = count($data);
// merge(array_slice($data, 0, $length / 2), array_slice($data, $length / 2));

$l = divide(array_slice($data, 0, $length / 2));
$r = divide(array_slice($data, $length / 2));

print_r(mmerge($l, $r));

function divide($item) {
    $length = count($item);
    if ($length == 2) {
        return conquer($item[0], $item[1]);
    }

    $left = array_slice($item, 0, $length / 2);
    $right = array_slice($item, $length / 2);

    return merge($left, $right);
}

function conquer($left, $right) {
    return
        $left < $right
            ? array($left, $right)
            : array($right, $left);
}

function mmerge($left, $right) {
    $item = array();
    $i=0; $j=0;
    while (count($item) < (count($left) + count($right))) {
        if ($i >= count($left)) {
            $item[] = $right[$j++];
            continue;
        } elseif ($j>=count($right)) {
            $item[] = $left[$i++];
            continue;
        }
        // elseif (count($left) == $i && count($right) == $j) {
        //     break;
        // } else {
            if ($left[$i] < $right[$j]) {
                $item[] = $left[$i++];
            } else {
                $item[] = $right[$j++];
            }
        // }
    }

    return $item;

}
function merge($left, $right) {
    print_r(array($left, $right));
    if (count($left) > 2) {
        divide($left);
    }
    if (count($right) > 2) {
        divide($right);
    }

    if (count($left) == 2) {
        $left = conquer($left[0], $left[1]);
    }

    if (count($right) == 2) {
        $right = conquer($right[0],$right[1]);
    }

    return mmerge($left, $right);
    }
